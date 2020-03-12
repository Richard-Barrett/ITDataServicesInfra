#!/bin/bash -ex

kubectl create namespace development

kubectl apply -f ../k8s-user/developer-role.yaml
kubectl apply -f ../k8s-user/developer-role-binding.yaml

mkdir -p ~/users/alice && cd ~/users/alice
awk '/certificate-authority-data:/{print $2}' ~/.kube/config | base64 -d > ca.crt
openssl x509 -in ca.crt -text
openssl genrsa -out alice.key 2048
openssl req -new -key alice.key -out alice.csr -subj "/CN=alice/O=mirantis/O=developers"
cat <<EOF | kubectl create -f -
apiVersion: certificates.k8s.io/v1beta1
kind: CertificateSigningRequest
metadata:
  name: alice_csr
spec:
  groups:
  - system:authenticated
  request: $(cat alice.csr | base64 | tr -d '\n')
  usages:
  - digital signature
  - key encipherment
  - client auth
EOF

kubectl get csr
kubectl certificate approve alice_csr
kubectl get csr alice_csr -o jsonpath='{.status.certificate}' | base64 -d > alice.crt
sudo useradd -b /home -m -s /bin/bash -c "I work here" alice
sudo passwd alice
sudo mkdir -p ~alice/keys && sudo cp -a ~/users/alice/*.{key,crt} ~alice/keys
sudo chmod 400 ~alice/keys/* && sudo chown -R alice:alice ~alice/keys
sudo ls -l ~alice/keys/
kubectl cluster-info

