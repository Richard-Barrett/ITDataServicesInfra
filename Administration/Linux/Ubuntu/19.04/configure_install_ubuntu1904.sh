#!/bin/bash

# Make a Git Directory for Git Clones && Subsequent Directories for Repository Work
cd ~
  mkdir Git
    cd ~
  mkdir Packages
    cd ~
  mkdir Drivers
    cd ~
  mkdir .ssh
    cd ~
  mkdir .docker 
    cd ~
  mkdir .vagrant
    cd ~
  mkdir Scripts
    cd ~
  mkdir Projects
    cd ~
  mkdir Documents
cd ~


# Update and Upgrade to Current Release
sudo apt-get update -y
sudo apt-get upgrade -y

# Install Packages 
for i in $(cat ITDataServicesInfra/tree/master/Administration/Linux/Ubuntu/packages.txt;
        do sudo apt-get install $i -y;
done
# Make an Passwordless SSH Key
  cd /.ssh
    ssh-keygen -t rsa -f ~/.ssh/id_rsa -q -P ""
  cd ~ 
  
# Install Time Shift
  sudo add-apt-repository -y ppa:teejee2008/ppa
  sudo apt-get update
  sudo apt-get install timeshift
# Install Google Chrome 
cd ~ 
  cd /Packages
    wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
    sudo apt install ./google-chrome-stable_current_amd64.deb
  cd ~
cat /etc/apt/sources.list.d/google-chrome.list
# Ensure Switch in to Git Directory 
cd ~ && cd /Git
# Git Clone on ITDataServicesInfra
git clone https://github.com/Richard-Barrett/ITDataServicesInfra.git
cd ~
# Clean Obsolete Packages
sudo apt-get clean -y
sudo apt-get autoremove -y
sudo apt-get autoclean -y
# Find and remove duplicate repository outside of Git Directory
# Set Up Crontab
# cat cronjobs into system crontab with cat <<EOF>
#EOF
# Set Up Logrotation
# Cat information for applications and system logs with cat <<EOF>>
#EOF
# Check If UFW Firewall Is Active and Set Up Firewall 
sudo ufw status verbose
  for i in $(cat ITDataServicesInfra/tree/master/Administration/Linux/Ubuntu/firewall.txt;
          do sudo ufw allow $i;
  done
sudo ufw enable 
# Enable Certain Essential System Services for Start on Bootup
for i in $(cat ITDataServicesInfra/tree/master/Administration/Linux/Ubuntu/services.txt;
        do sudo systemctl enable $i;
done
