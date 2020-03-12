kubectl create namespace vote
kubectl config set-context vote --cluster=kubernetes --user=kubernetes-admin --namespace=vote
kubectl config use-context vote
cd db-data/
kubectl create -f db-data-persistentvolume.yaml 
kubectl create -f db-data-persistentvolumeclaim.yaml 
kubectl create -f db-deployment.yaml 
kubectl create -f db-service.yaml 
kubectl get pod
kubectl get svc
cd ../redis/
kubectl create -f redis-deployment.yaml 
kubectl create -f redis-service.yaml 
cd ../worker/
kubectl create -f worker-deployment.yaml 
cd ../vote/
kubectl create -f .
cd ../result/
kubectl create -f .
