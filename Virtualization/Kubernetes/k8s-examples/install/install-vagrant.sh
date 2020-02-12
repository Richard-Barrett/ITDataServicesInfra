#!/bin/bash -ex
# https://docs.cumulusnetworks.com/display/VX/Vagrant+and+Libvirt+with+KVM+or+QEMU
sudo apt-get install -y vagrant
sudo apt-get update -y
sudo apt-get install -y libvirt-bin libvirt-dev qemu-utils qemu
sudo /etc/init.d/libvirt-bin restart
libvirtd --version
sudo addgroup libvirtd || true
sudo usermod -a -G libvirtd ${USER}
#wget https://releases.hashicorp.com/vagrant/2.0.2/vagrant_2.0.2_x86_64.deb
#sudo dpkg -i vagrant_2.0.2_x86_64.deb
wget https://releases.hashicorp.com/vagrant/2.2.4/vagrant_2.2.4_x86_64.deb
sudo dpkg -i vagrant_2.2.4_x86_64.deb
vagrant --version
vagrant plugin install vagrant-libvirt
#vagrant plugin install vagrant-mutate

# vagrant shared folder feature requires NFS server
sudo apt-get -y install nfs-kernel-server
