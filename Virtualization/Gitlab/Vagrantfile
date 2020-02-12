# -*- mode: ruby -*-
# vi: set ft=ruby :

# Please see the Vagrant section in the docs for caveats and tips
# https://gitlab.com/gitlab-org/gitlab-development-kit/blob/master/doc/vagrant.md

Vagrant.require_version ">= 1.6.0"
VAGRANTFILE_API_VERSION = "2".freeze

def enable_shares(config, nfs)
  # paths must be listed as shortest to longest per bug: https://github.com/GM-Alex/vagrant-winnfsd/issues/12#issuecomment-78195957
  config.vm.synced_folder ".", "/vagrant", type: "rsync",
                                          rsync__exclude: ['gitlab', 'postgresql', 'gitlab-shell', 'gitlab-runner', 'gitlab-workhorse'],
                                          rsync__auto: false
  config.vm.synced_folder "gitlab/", "/vagrant/gitlab", create: true, nfs: nfs
  config.vm.synced_folder "go-gitlab-shell/", "/vagrant/go-gitlab-shell", create: true, nfs: nfs
  config.vm.synced_folder "gitlab-runner/", "/vagrant/gitlab-runner", create: true, nfs: nfs
  config.vm.synced_folder "gitlab-workhorse/", "/vagrant/gitlab-workhorse", create: true, nfs: nfs
end

def running_in_admin_mode?
  return false unless Vagrant::Util::Platform.windows?

  (`reg query HKU\\S-1-5-19 2>&1` =~ /ERROR/).nil?
end

if Vagrant::Util::Platform.windows? && !running_in_admin_mode?
  raise Vagrant::Errors::VagrantError.new, "You must run the GitLab Vagrant from an elevated command prompt"
end

required_plugins = %w[vagrant-share vagrant-disksize]
required_plugins_non_windows = %w[facter]
required_plugins_windows = %w[] # %w(vagrant-winnfsd) if https://github.com/GM-Alex/vagrant-winnfsd/issues/50 gets fixed

if Vagrant::Util::Platform.windows?
  required_plugins.concat required_plugins_windows
else
  required_plugins.concat required_plugins_non_windows
end

# thanks to https://stackoverflow.com/a/28801317/1233435
required_plugins.each do |plugin|
  need_restart = false
  unless Vagrant.has_plugin? plugin
    system "vagrant plugin install #{plugin}"
    need_restart = true
  end
  exec "vagrant #{ARGV.join(' ')}" if need_restart
end

$apt_reqs = <<EOT
  apt-add-repository -y ppa:rael-gc/rvm
  apt-add-repository -y ppa:ubuntu-lxc/lxd-stable
  add-apt-repository -y ppa:longsleep/golang-backports
  add-apt-repository -y ppa:git-core/ppa
  wget -qO- https://deb.nodesource.com/setup_12.x | bash -
  wget -qO- https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
  echo "deb http://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list
  export DEBIAN_FRONTEND=noninteractive
  export RUNLEVEL=1
  apt-get update && apt-get -y install git graphicsmagick postgresql postgresql-contrib libpq-dev libimage-exiftool-perl redis-server libicu-dev cmake g++ nodejs libkrb5-dev curl ruby ed golang-go nginx libgmp-dev rvm yarn libre2-dev docker.io runit
  curl https://dl.min.io/server/minio/release/linux-amd64/minio --output /usr/local/bin/minio && chmod +x /usr/local/bin/minio
  apt-get -y upgrade
EOT

# Set up swap when using a full VM
$swap_setup = <<EOT
  # create a swapfile
  sudo fallocate -l 4G /swapfile
  sudo chmod 600 /swapfile
  sudo mkswap /swapfile
  # enable swap now
  sudo swapon /swapfile
  # and on reboot
  echo '/swapfile   none    swap    sw    0   0' | sudo tee --append /etc/fstab
EOT

$user_setup = <<EOT
  DEV_USER=$(stat -c %U /vagrant)
  echo "$DEV_USER ALL=(ALL) NOPASSWD:ALL" | tee /etc/sudoers.d/$DEV_USER
  sudo addgroup $DEV_USER rvm
  sudo addgroup $DEV_USER docker
  sudo -u $DEV_USER -i bash -l -c "rvm install 2.6.5 && rvm use 2.6.5 --default && gem install bundler -v 1.17.3"
  sudo chown -R $DEV_USER:$DEV_USER /home/$DEV_USER
  sudo ln -s /vagrant /home/$DEV_USER/gitlab-development-kit

  # automatically move into the gitlab-development-kit folder, but only add the command
  # if it's not already there
  if [ -f /home/$DEV_USER/.bash_profile ]; then
    sudo -u $DEV_USER -i bash -c "grep -q \"cd /home/$DEV_USER/gitlab-development-kit/\" /home/$DEV_USER/.bash_profile || echo \"cd /home/$DEV_USER/gitlab-development-kit/\" >> /home/$DEV_USER/.bash_profile"
  else
    sudo -u $DEV_USER -i bash -c "touch /home/$DEV_USER/.bash_profile && echo \"cd /home/$DEV_USER/gitlab-development-kit/\" >> /home/$DEV_USER/.bash_profile"
  fi

  # set up gdk
  echo '/vagrant' > /vagrant/.gdk-install-root
  sudo -u $DEV_USER -i bash -c "gem install gitlab-development-kit"
  sudo -u $DEV_USER -i bash -c "gdk trust /vagrant"

  # set git defaults
  sudo -u $DEV_USER -i bash -c "git config --global user.name 'GitLab Development'"
  sudo -u $DEV_USER -i bash -c "git config --global user.email gitlab@local.local"
EOT

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.provision "shell", inline: $apt_reqs
  config.vm.provision "shell", inline: $user_setup
  unless Vagrant::Util::Platform.windows?
    # NFS setup
    config.vm.network "private_network", type: "dhcp"
  end

  config.vm.network "forwarded_port", guest: 3000, host: 3000, auto_correct: true

  # Forward SSH agent to allow SSH git operations
  config.ssh.forward_agent = true

  config.vm.provider "docker" do |d, override|
    d.build_dir = "vagrant"
    d.privileged      = true
    d.has_ssh         = true
    d.remains_running = true
    enable_shares(override, false)
  end

  config.vm.provider "lxc" do |v, override|
    override.vm.box = "fgrehm/trusty64-lxc"
    enable_shares(override, true)
  end

  config.vm.provider "virtualbox" do |vb, override|
    override.vm.box = "ubuntu/xenial64"
    override.disksize.size = "15GB"
    if Vagrant::Util::Platform.windows?
      # thanks to https://github.com/rdsubhas/vagrant-faster/blob/master/lib/vagrant/faster/action.rb
      # current bug in Facter requires detecting Windows core count separately - https://tickets.puppetlabs.com/browse/FACT-959
      cpus = `wmic cpu Get NumberOfCores`.split[1].to_i
      # current bug in Facter requires detecting Windows memory separately - https://tickets.puppetlabs.com/browse/FACT-960
      mem = `wmic computersystem Get TotalPhysicalMemory`.split[1].to_i / 1024 / 1024
      enable_shares(override, false)
    else
      cpus = Facter.value('processors')['count']
      if facter_mem = Facter.value('memory')
        mem = facter_mem.slice! " GiB".to_i * 1024
      elsif facter_mem = Facter.value('memorysize_mb')
        mem = facter_mem.to_i
      else
        raise "unable to determine total host RAM size"
      end

      # disables NFS on macOS to prevent UID / GID issues with mounted shares
      enable_nfs = Vagrant::Util::Platform.platform =~ /darwin/ ? false : true
      enable_shares(override, enable_nfs)
    end

    # use 1/4 of memory or 6 GB, whichever is greatest
    mem = [mem / 4, 6144].max

    # Set up swap
    override.vm.provision "shell", inline: $swap_setup

    # performance tweaks
    # per https://www.virtualbox.org/manual/ch03.html#settings-processor set cpus to real cores, not hyperthreads
    vb.cpus = cpus
    vb.memory = mem
    vb.customize ["modifyvm", :id, "--nestedpaging", "on"]
    vb.customize ["modifyvm", :id, "--largepages", "on"]
    vb.customize ["modifyvm", :id, "--ioapic", "on"] if cpus > 1

    # uncomment if you don't want to use all of host machines CPU
    # vb.customize ["modifyvm", :id, "--cpuexecutioncap", "50"]

    # uncomment if you need to troubleshoot using a GUI
    # vb.gui = true
  end
end
