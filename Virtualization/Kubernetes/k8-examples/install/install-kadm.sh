#!/bin/bash -e
if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root"
   exit 1
fi

# Save input arguments for debug and diagnosis
echo "Running: $0 $@" >> .install.log

# https://packages.cloud.google.com/apt/dists/kubernetes-xenial/main/binary-amd64/Packages
#K8SVER=${1:-"1.7.5-00"}
#K8SVER=${1:-"1.9.1-00"}
#K8SVER=${1:-"1.9.3-00"}
#K8SVER=${1:-"1.11.1-00"}
K8SVER=${1:-"1.13.6-00"}

#KADMVER=${K8SVER}
#KADMVER=1.10.5-00
#KADMVER="1.11.1-00"
KADMVER="1.14.1-00"
DOMNAME="training.local"

# https://kubernetes.io/docs/setup/independent/install-kubeadm/
# -------------------------------------------------------------
install_kubeadm()
{
    apt-get install -y apt-transport-https
    curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add -
    echo deb http://apt.kubernetes.io/ kubernetes-xenial main | tee /etc/apt/sources.list.d/kubernetes.list
    apt-get update
    apt-get install -y kubernetes-cni=0.6.0-00
    apt-get install -y kubeadm=${1} kubectl=${2} kubelet=${2} --allow-downgrades
    kubeadm version
    kubelet --version

    # customize out k8s installation
    cat <<EOF > /etc/default/kubelet
KUBELET_EXTRA_ARGS="--read-only-port=10255"
EOF
}

change_domainname()
{
    sed -i "s/cluster.local/${1}/" /etc/systemd/system/kubelet.service.d/10-kubeadm.conf
    #sed -i 's/10.96/10.99/' /etc/systemd/system/kubelet.service.d/10-kubeadm.conf
    systemctl daemon-reload
    systemctl restart kubelet.service
}

install_kubeadm $KADMVER $K8SVER
