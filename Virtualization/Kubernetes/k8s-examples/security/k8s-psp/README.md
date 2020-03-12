```
cd /etc/kubernetes/
less kubelet.conf 
getenforce 
vi /etc/selinux/semanage.conf 
pushd /etc/kubernetes/
view manifests/kube-apiserver.yaml 
ls -ltra
ls -ltra manifests/
%
ls -ltra manifests/
cp manifests/kube-apiserver.yaml .
vi manifests/kube-apiserver.yaml 
cp kube-apiserver.yaml manifests/
cp kube-apiserver.yaml 
cp kube-apiserver.yaml kube-apiserver.yaml.orig
vi kube-apiserver.yaml
diff kube-apiserver.yaml.orig kube-apiserver.yaml
cp kube-apiserver.yaml manifests/
-------------------------------------------------------------------------------
ps axf | grep apiserver
kubectl get nodes
kubectl get pods --namespace kube-system | grep kube-apiserver-master
sudo journalctl -fu kubelet
-------------------------------------------------------------------------------
sudo journalctl -fu kubelet
sudo -i
ls
vi privileged-psp.yaml
vi .profile 
source <(kubectl completion bash)
kubectl create -f privileged-psp.yaml 
kubectl get psp
kubectl get psp -o yaml
kubectl --as=system:node:master auth can-i use podsecuritypolicy/priviledged
kubectl edit clusterrole system:node 
kubectl --as=system:node:master auth can-i use podsecuritypolicy/priviledged
kubectl get clusterrolebinding 
kubectl create clusterrolebinding policy-node-binding --clusterrole=system:node --user=system:node:master
kubectl --as=system:node:master auth can-i use podsecuritypolicy/priviledged
kubectl get psp
kubectl delete clusterrolebinding policy-node-binding 
kubectl create clusterrolebinding policy-node-binding --clusterrole=system:node --user=system:node:master
kubectl --as=system:node:master auth can-i use podsecuritypolicy/privileged
kubectl get pods --namespace kube-system | grep kube-apiserver-master
kubectl create namespace psp-example
kubectl create rolebinding -n psp-example fake-editor --clusterrole=edit --serviceaccount=psp-example:fake-user
alias kubectl-admin='kubectl -n psp-example'
alias kubectl-user='kubectl --as=system:serviceaccount:psp-example:fake-user -n psp-example'
vi example-psp.yaml
kubectl-admin create -f example-psp.yaml
kubectl-admin get psp
vi example-pod-unpriv.yaml
kubectl-user create -f example-pod-unpriv.yaml
kubectl-user auth can-i use podsecuritypolicy/example
kubectl-admin create role psp:unprivileged     --verb=use     --resource=podsecuritypolicy     --resource-name=example
kubectl-admin create rolebinding fake-user:psp:unprivileged     --role=psp:unprivileged     --serviceaccount=psp-example:fake-user
kubectl-user auth can-i use podsecuritypolicy/example
kubectl-user create -f example-pod-unpriv.yaml
vi example-pod-priv.yaml
kubectl-user create -f example-pod-priv.yaml 
kubectl-user run pause --image=gcr.io/google-containers/pause
kubectl-user get pods
kubectl-user get events | head -n 2
kubectl-admin create rolebinding default:psp:unprivileged     --role=psp:unprivileged     --serviceaccount=psp-example:default
kubectl-user get pods --watch
```
