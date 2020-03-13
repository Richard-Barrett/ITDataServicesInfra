## Vagrant

## Installing Vagrant

## Using Vagrant
In order to use Vagrant you first have to install it, see the above on how to install Vagrant.
to get started move into the Vagrant Directory that contains the **`Vagrantfile`**

Example:
1. Move into the Directory **`~/Git/ITDataServicesInfra/Virtualization/Vagrant/Ubuntu/bionic64`**
```
cd ~/Git/ITDataServicesInfra/Virtualization/Vagrant/Ubuntu/bionic64
```

2. Initialize the Vagrant Box with **`vagrant up`**
```
vagrant up
```

Expected Output:
```
 ✘ jessicarey@Jessicas-MacBook-Pro  ~/Git/ITDataServicesInfra/Virtualization/Vagrant/Ubuntu/bionic64   master  vagrant up
==> vagrant: A new version of Vagrant is available: 2.2.7 (installed version: 2.2.4)!
==> vagrant: To upgrade visit: https://www.vagrantup.com/downloads.html

Bringing machine 'default' up with 'virtualbox' provider...
==> default: Box 'ubuntu/bionic64' could not be found. Attempting to find and install...
    default: Box Provider: virtualbox
    default: Box Version: >= 0
==> default: Loading metadata for box 'ubuntu/bionic64'
    default: URL: https://vagrantcloud.com/ubuntu/bionic64
==> default: Adding box 'ubuntu/bionic64' (v20200311.0.0) for provider: virtualbox
    default: Downloading: https://vagrantcloud.com/ubuntu/boxes/bionic64/versions/20200311.0.0/providers/virtualbox.box
    default: Download redirected to host: cloud-images.ubuntu.com
==> default: Successfully added box 'ubuntu/bionic64' (v20200311.0.0) for 'virtualbox'!
==> default: Importing base box 'ubuntu/bionic64'...
==> default: Matching MAC address for NAT networking...
==> default: Checking if box 'ubuntu/bionic64' version '20200311.0.0' is up to date...
==> default: Setting the name of the VM: bionic64_default_1584061724054_99877
Vagrant is currently configured to create VirtualBox synced folders with
the `SharedFoldersEnableSymlinksCreate` option enabled. If the Vagrant
guest is not trusted, you may want to disable this option. For more
information on this option, please refer to the VirtualBox manual:

  https://www.virtualbox.org/manual/ch04.html#sharedfolders

This option can be disabled globally with an environment variable:

  VAGRANT_DISABLE_VBOXSYMLINKCREATE=1

or on a per folder basis within the Vagrantfile:

  config.vm.synced_folder '/host/path', '/guest/path', SharedFoldersEnableSymlinksCreate: false
==> default: Clearing any previously set network interfaces...
==> default: Preparing network interfaces based on configuration...
    default: Adapter 1: nat
==> default: Forwarding ports...
    default: 22 (guest) => 2222 (host) (adapter 1)
==> default: Running 'pre-boot' VM customizations...
==> default: Booting VM...
==> default: Waiting for machine to boot. This may take a few minutes...
    default: SSH address: 127.0.0.1:2222
    default: SSH username: vagrant
    default: SSH auth method: private key
    default: Warning: Connection reset. Retrying...
    default: Warning: Remote connection disconnect. Retrying...
    default:
    default: Vagrant insecure key detected. Vagrant will automatically replace
    default: this with a newly generated keypair for better security.
    default:
    default: Inserting generated public key within guest...
    default: Removing insecure key from the guest if it's present...
    default: Key inserted! Disconnecting and reconnecting using new SSH key...
==> default: Machine booted and ready!
==> default: Checking for guest additions in VM...
    default: The guest additions on this VM do not match the installed version of
    default: VirtualBox! In most cases this is fine, but in rare cases it can
    default: prevent things such as shared folders from working properly. If you see
    default: shared folder errors, please make sure the guest additions within the
    default: virtual machine match the version of VirtualBox you have installed on
    default: your host and reload your VM.
    default:
    default: Guest Additions Version: 5.2.8_KernelUbuntu r120774
    default: VirtualBox Version: 6.0
==> default: Mounting shared folders...
    default: /vagrant => /Users/jessicarey/Git/ITDataServicesInfra/Virtualization/Vagrant/Ubuntu/bionic64
```

## How To see the list of running Vagrant Boxes
To see a list of Vagrant Boxes running locally you can initiate the following command:
```
vagrant box list
```

Expected Output:
```
jessicarey@Jessicas-MacBook-Pro  ~/Git/ITDataServicesInfra/Virtualization/Vagrant/Ubuntu/bionic64   master  vagrant box list
ubuntu/bionic64 (virtualbox, 20200311.0.0)
```

**Vagrantfile Template**

```
# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

$script = <<SCRIPT
# TODO: Put your install script here.
SCRIPT

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  # All Vagrant configuration is done here. The most common configuration
  # options are documented and commented below. For a complete reference,
  # please see the online documentation at vagrantup.com.

  # Every Vagrant virtual environment requires a box to build off of.
  # Official boxes are here: https://atlas.hashicorp.com/boxes/search
  # Additional boxes here: http://www.vagrantbox.es/
  config.vm.box = "ubuntu/trusty64"
  #config.vm.box = "hashicorp/precise64"

  # You can shell scripts when `vagrant up` or `vagrant provision` is run.
  # Just put scripts in the same directory as this `Vagrantfile`.
  #config.vm.provision "shell", privileged: false, path: "vagrant-bootstrap.sh"
  # You can do multiple scripts, if you want:
  #config.vm.provision "shell", privileged: false, path: "vagrant-bootstrap2.sh"
  config.vm.provision "shell", privileged: true, inline: $script

  # Port forwarding examples
  # Just in case you need to run a database server, web server, etc.
  #config.vm.network "forwarded_port", guest: 8080, host: 8080
  #config.vm.network "forwarded_port", guest: 5000, host: 5000
  #config.vm.network "forwarded_port", guest: 35357, host: 35357

  # Mem/cpu config example.
  # If you need more CPUs/RAM, uncomment the next 4 lines and edit as needed.
  #config.vm.provider "virtualbox" do |v|
  #  v.memory = 1024
  #  v.cpus = 2
  #end

  # Shared folders:
  #
  # Setting the workspace to the current dir allows you to do editing/
  # development on host environment (OSX, etc.) and then actually run/
  # test things inside the virtual environvment.
  # You can map multiple folders in this way.
  # In this case, the ".", "/workspace" indicates that we want to map
  # the current directory on the host machine to the "/workspace" directory
  # on the guest/VM.
  #config.vm.synced_folder ".", "/proj"

end
```
