#!/bin/bash -e
kubectl create serviceaccount -n default $1
kubectl get serviceaccount -n default $1 -o yaml
kubectl create clusterrolebinding ${1}-bind --clusterrole=cluster-admin --serviceaccount=default:$1
secret=$(kubectl get serviceaccount -n default $1 -o jsonpath='{.secrets[0].name}')
token=$(kubectl get secret $secret -n default -ojsonpath='{.data.token}' | base64 --decode)
echo $token
