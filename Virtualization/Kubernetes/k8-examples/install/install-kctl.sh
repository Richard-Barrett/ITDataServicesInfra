#!/bin/bash -e
if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root"
   exit 1
fi

# Save input arguments for debug and diagnosis
echo "Running: $0 $@" >> .install.log

#K8SVER=${1:-"1.7.5-00"}
#K8SVER=${1:-"1.9.1-00"}
#K8SVER=${1:-"1.9.3-00"}
#K8SVER=${1:-"1.11.1-00"}
K8SVER=${1:-"1.13.6-00"}

# https://kubernetes.io/docs/setup/independent/install-kubeadm/
# -------------------------------------------------------------
install_kubectl()
{
    # On the minimal ubuntu image bash-completion is not installed
    apt install -y bash-completion

    # NOT needed since apt-get install of kubeadm installs kubelet and kubectl also
    # apt-get install -y apt-transport-https
    # curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add -
    # echo deb http://apt.kubernetes.io/ kubernetes-xenial main | tee /etc/apt/sources.list.d/kubernetes.list
    # apt-get update
    # apt-get install -y kubectl=$1

    # This is getting overwritten by AWS, because we are too fast.
    # AWS is too slow and overwrites the .profile with it's own after we are done.
    echo 'source <(kubectl completion bash)' | tee --append $HOME/.bashrc
}

install_kubectl $K8SVER
