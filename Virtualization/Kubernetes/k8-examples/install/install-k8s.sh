#!/bin/bash -e
if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root"
   exit 1
fi

# Save input arguments for debug and diagnosis
echo "Running: $0 $@" >> .install.log

INTF=${3:-"eth0"}
APIIP=$(ip a show dev $INTF | grep -w inet | awk -e '{print $2}' | cut -d'/' -f1)

CNIPLUG=${4:-"calico"}

USER=${5:-"stack"}

TOK=${1:-"00b851.ec0933704172bb5f"}

SVCCIDR=
DOMAIN="training.local"

#VERSION=v1.7.5
#VERSION=${6:-"v1.9.3"}
#VERSION=${6:-"v1.11.1"}
VERSION=${6:-"v1.13.6"}

# Haven't put the iptables forward in yet. With 1.7.5 k8s services were not
# accessible without it. No longer needed.
customize_for_docker()
{
    VER=$(docker version -f '{{.Server.Version}}' | cut -d'.' -f1)
    # change the policy to ACCEPT (which it was in Docker 1.12 and before)
    # iptables -P FORWARD ACCEPT
    # or
    # Docker is configured to drop external traffic. Appending the forwarding rule allows
    # access the docker0, which allows kubernetes nodePort to work.
    if( $VER <= "17" ); then
        echo "Applying network iptables workaround"
        #this test should be against the k8s version, not docker version
        #iptables -A FORWARD -i eth0 -o docker0 -j ACCEPT
    fi
}

token_create()
{
    kubeadm token create --print-join-command | awk '/kubeadm join/ {print $5 "\n" $7}'
}

# https://kubernetes.io/docs/reference/setup-tools/kubeadm/kubeadm-init/
# -------------------------------------------------------------
install_k8s_master()
{
    kubeadm init --token $5 --token-ttl 0 --kubernetes-version $1 --apiserver-advertise-address $4 --pod-network-cidr $3
    #  --service-cidr 10.99.0.0/16 --service-dns-domain example.com
    #TOK=$(kubeadm token list | grep bootstrap | awk '{print $1}')

    rm -rf $HOME/.kube && mkdir -p $HOME/.kube
    cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
    #chown $(id -u):$(id -g) $HOME/.kube/config
    chown -R ${2}:${2} $HOME/.kube
}

#CNICALICO="http://docs.projectcalico.org/v2.6/getting-started/kubernetes/installation/hosted/kubeadm/1.6/calico.yaml"
#CNICALICO="https://docs.projectcalico.org/v3.0/getting-started/kubernetes/installation/hosted/kubeadm/1.7/calico.yaml"
#CNICALICO="https://docs.projectcalico.org/v3.1/getting-started/kubernetes/installation/hosted/kubernetes-datastore/calico-networking/1.7/calico.yaml"
CNICALICO="https://docs.projectcalico.org/v3.3/getting-started/kubernetes/installation/hosted/kubernetes-datastore/calico-networking/1.7/calico.yaml"
#CNIFLANNEL="https://raw.githubusercontent.com/coreos/flannel/v0.9.1/Documentation/kube-flannel.yml"
#CNIFLANNEL="https://raw.githubusercontent.com/coreos/flannel/c5d10c8/Documentation/kube-flannel.yml"
CNIFLANNEL="https://raw.githubusercontent.com/coreos/flannel/v0.10.0/Documentation/kube-flannel.yml"
install_k8s_network()
{
    case $CNIPLUG in
        "calico")
           #kubectl apply -f https://docs.projectcalico.org/v3.1/getting-started/kubernetes/installation/hosted/rbac-kdd.yaml
            kubectl apply -f https://docs.projectcalico.org/v3.3/getting-started/kubernetes/installation/hosted/rbac-kdd.yaml
            kubectl apply -f $CNICALICO
            ;;
        *)
            kubectl apply -f $CNIFLANNEL
            ;;
    esac
}
install_k8s_node()
{
    # Have to figure out how to get the discovery-token-ca-cert-hash
##    kubeadm join --token $1 ${2}:6443 --discovery-token-ca-cert-hash sha256:489681fc136fbe64180ef6c12f62658b2f7caa107d795d3eb43fd36bbd509095
    kubeadm join --token $1 ${2}:6443 --discovery-token-unsafe-skip-ca-verification
}

install_customizations()
{
    kubectl apply -f ~/k8s-examples/extensions/metrics-server-1.8+
}

allow_master_schedule()
{
    # Untaint master node to allow workload scheduling for single-node-installation
    sudo -u ${USER} kubectl taint nodes --all node-role.kubernetes.io/master-
}

CIDR=${2:-"192.168.0.0/16"}
case $CNIPLUG in
    # for Network Policy to work correctly, you need to pass --pod-network-cidr=192.168.0.0/16 to kubeadm init
    # https://docs.projectcalico.org/v3.2/getting-started/kubernetes/installation/calico
    "calico")
        CIDR="192.168.0.0/16"
        ;;
    # For flannel to work correctly, you must pass --pod-network-cidr=10.244.0.0/16 to kubeadm init
    # https://kubernetes.io/docs/setup/independent/create-cluster-kubeadm/
    "flannel")
        CIDR="10.244.0.0/16"
        ;;
    *)
        ;;
esac

install_k8s_master $VERSION $USER $CIDR $APIIP $TOK
install_k8s_network $CNIPLUG
install_customizations
allow_master_schedule
