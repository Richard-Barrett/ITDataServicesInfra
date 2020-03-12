## Calico

```
kubectl get node -o yaml | grep IP -A 1 -B 1
kubectl get pod -n kube-system -l k8s-app=calico-node -o json | jq ".items[] | select(.status.podIP == \"$PrivateIP\") | .metadata.name" | tr -d '"'
POD=$(kubectl get pod -n kube-system -l k8s-app=calico-node -o json | jq ".items[] | select(.status.podIP == \"$PrivateIP\") | .metadata.name" | tr -d '"')

kubectl logs -n kube-system $POD -c calico-node | grep 172
kubectl logs -n kube-system $POD -c calico-node | grep bird | less

kubectl get -n kube-system pods -l k8s-app=calico-etcd --show-labels
ETC=$(kubectl get pod -n kube-system -l k8s-app=calico-etcd -o json | jq ".items[] | .metadata.name" | tr -d '"')

kubectl exec -n kube-system $ETC -- sh -c "ETCDCTL_API=3 etcdctl version"
kubectl exec -n kube-system $ETC -- sh -c 'ETCDCTL_API=3 etcdctl get "" --prefix=true' | less

sudo ETCD_ENDPOINTS=http://10.96.232.136:6666 ./calicoctl node status

----------------------------------

sudo ETCD_ENDPOINTS=http://10.96.232.136:6666 ./calicoctl node show
sudo ETCD_ENDPOINTS=http://10.96.232.136:6666 ./calicoctl get node -o yaml
sudo ETCD_ENDPOINTS=http://10.96.232.136:6666 ./calicoctl get ipPool -o yaml
sudo ETCD_ENDPOINTS=http://10.96.232.136:6666 ./calicoctl get bgpconfig default
sudo ETCD_ENDPOINTS=http://10.96.232.136:6666 ./calicoctl get bgpPeer --scope=global -o yaml
sudo ETCD_ENDPOINTS=http://10.96.232.136:6666 ./calicoctl get bgpPeer --node=master
sudo ETCD_ENDPOINTS=http://10.96.232.136:6666 ./calicoctl node diags
sudo ETCD_ENDPOINTS=http://10.96.232.136:6666 ./calicoctl node checksystem


sudo ETCD_ENDPOINTS=http://10.96.232.136:6666 /home/stack/calico/calicoctl apply -f - << EOF
- apiVersion: v1
  kind: node
  metadata:
    name: master
  spec:
    bgp:
      ipv4Address: 172.16.1.207/24
EOF

--------------------------------------------------
curl -LO http://docs.projectcalico.org/v2.6/getting-started/kubernetes/installation/hosted/kubeadm/1.6/calico.yaml
curl -LO https://github.com/projectcalico/calicoctl/releases/download/v1.3.0/calicoctl
chmod +x ./calicoctl


--------------------------------------------------
kubectl get -n kube-system pods -l k8s-app=calico-node -o wide
kubectl get -n kube-system pods -l k8s-app=calico-etcd -o wide

--------------------------------------------------
sudo route del -net 172.19.0.0 netmask 255.255.0.0

```
