Vagrant.configure(2) do |config|
  config.vm.box = "centos/7"

  config.vm.provider :virtualbox do |virtualbox, override|
    virtualbox.memory = 1024
    override.vm.box_download_checksum_type = "sha256"
    override.vm.box_download_checksum = "b24c912b136d2aa9b7b94fc2689b2001c8d04280cf25983123e45b6a52693fb3"
    override.vm.box_url = "https://cloud.centos.org/centos/7/vagrant/x86_64/images/CentOS-7-x86_64-Vagrant-1803_01.VirtualBox.box"
  end
end
