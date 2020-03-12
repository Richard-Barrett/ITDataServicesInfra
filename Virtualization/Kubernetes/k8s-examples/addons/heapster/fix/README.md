## Fix

* Fixing broken hpa

- When we do a "kubectl get hpa" we see that Target is unknown.
- If we do a "kubectl describe hpa" we see the error "unable to get metrics for resource cpu"
- We can google heapster and the error to find [Issue 57673](https://github.com/kubernetes/kubernetes/issues/57673)
- The fix is to modify kube-controller-manager's parameter --horizontal-pod-autoscaler-use-rest-clients to be false. Default is true.
- sudo cp /etc/kubernetes/manifests/kube-controller-manager.yaml .
- edit and an argument:
```
*** kube-controller-manager.yaml.bak    2018-03-27 19:59:19.640107458 +0000
--- kube-controller-manager.yaml        2018-03-27 19:59:24.744057990 +0000
*************** spec:
*** 25,30 ****
--- 25,31 ----
      - --allocate-node-cidrs=true
      - --cluster-cidr=192.168.0.0/16
      - --node-cidr-mask-size=24
+     - --horizontal-pod-autoscaler-use-rest-clients=false
      image: gcr.io/google_containers/kube-controller-manager-amd64:v1.9.3
      livenessProbe:
        failureThreshold: 8
```

- sudo cp kube-controller-manager.yaml /etc/kubernetes/manifests/
