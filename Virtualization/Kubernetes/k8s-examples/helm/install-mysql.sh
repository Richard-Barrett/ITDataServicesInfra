# create persistentvolumes
kubectl create -f ~/kd200-examples/debug/solution/database.yaml

helm install --name mydb stable/mysql
MYSQL_ROOT_PASSWORD=$(kubectl get secret --namespace default mydb-mysql -o jsonpath="{.data.mysql-root-password}" | base64 --decode; echo)
# echo $MYSQL_ROOT_PASSWORD

kubectl run -it ubuntu --image=ubuntu:16.04 --restart=Never --env="ROOT_PASSWORD=$MYSQL_ROOT_PASSWORD" -- bash -il
# apt-get update && apt-get install mysql-client -y
# mysql -h mydb-mysql -p$ROOT_PASSWORD
