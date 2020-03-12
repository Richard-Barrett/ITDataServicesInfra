kubectl run -i --tty load-generator --image=busybox /bin/sh
kubectl describe hpa php-apache
kubectl get node -o wide
kubectl -v 8 top pod
kubectl run php-apache --image=gcr.io/google_containers/hpa-example --requests=cpu=200m --expose --port=80
kubectl get pods -l run=php-apache
curl http://$(kubectl get svc php-apache -o jsonpath={..clusterIP}):80
kubectl autoscale deployment php-apache --cpu-percent=50 --min=1 --max=10
kubectl get hpa php-apache -o wide -w
