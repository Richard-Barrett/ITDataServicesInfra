#!/bin/bash -ex

IP=$(ip a sh dev eth0 | awk '/inet / {print $2}' | cut -d/ -f1)
cd
kubectl config set-cluster work --server=https://${IP}:6443 --certificate-authority=keys/ca.crt --embed-certs=true
kubectl cluster-info || true
kubectl config set-credentials alice --client-certificate=keys/alice.crt --client-key=keys/alice.key
kubectl config set-context work --cluster=work --user=alice --namespace=development
kubectl config use-context work
kubectl auth can-i create pod
kubectl auth can-i list deployment
kubectl auth can-i get pod --subresource=log
kubectl auth can-i create pod --subresource=exec
