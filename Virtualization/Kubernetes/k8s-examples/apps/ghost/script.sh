kubectl create secret generic ghost-secrets --from-env-file=ghost-secrets.txt
kubectl apply -f mysql.yaml
kubectl exec mysql-deployment-d78d7879f-vsx5w -it -- mysql -u student -psecret -e "show databases;"
kubectl exec mysql-deployment-d78d7879f-vsx5w -it -- mysql -u student -psecret -e "use ghost_db; show tables;"

