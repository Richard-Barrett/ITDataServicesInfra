kubectl create configmap ghost-v0.11-config --from-file=configs
kubectl apply -f ghost-deployment.yaml
kubectl get pods

# -- debug
# kubectl logs ghost-v0.11-6b8cf5f98d-xxxxx -c ghost
# kubectl exec -it ghost-v0.11-5db67447c9-xxxxx -c ghost -- bash
