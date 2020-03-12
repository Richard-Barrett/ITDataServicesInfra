For more information read: https://kubernetes.io/docs/tasks/debug-application-cluster/audit/

1. Find out where apiserver is running and copy /etc/kubernetes/manifests/kube-apiserver.yaml to your local directory:
```
kubectl get pods --namespace kube-system -o wide | grep apiserver
kubectl describe node/master | grep InternalIP -A 1
sudo cp /etc/kubernetes/manifests/kube-apiserver.yaml .
sudo chown stack ./kube-apiserver.yaml
```

2. Modify the file to enable auditing and set audit-policy:

3. First copy the audit-policy file to /etc/kubernetes.

4. Watch kubelet logs and then overwrite kube-apiserver.yaml in /etc/kubernetes/manifests. Keep a backup of it just in case.
```
sudo journalctl -f -u kubelet | grep apiserv
```

5. Watch kube-apiserver logs, and launch/delete some pods to see audit messages:
```
kubectl logs --follow kube-apiserver-master --namespace=kube-system
```
