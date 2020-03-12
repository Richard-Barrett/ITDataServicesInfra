kubectl exec -it --context=myblog mysql-deployment-5d8556dbb8-zlj9f -- bash

mysql -u root -psuper-secret
mysql> 

create database yourblog_db;
grant all on yourblog_db.* to 'customer'@'%' identified by 'customersecret';
