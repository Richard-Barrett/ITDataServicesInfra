# API Certs

- https://kubernetes.io/docs/concepts/cluster-administration/certificates/
- https://kubernetes.io/docs/admin/accessing-the-api/
- https://kubernetes.io/docs/tasks/tls/managing-tls-in-a-cluster/
- https://kubernetes.io/docs/tasks/access-application-cluster/access-cluster/

openssl print certificate data:
```
sudo openssl x509 -in /etc/kubernetes/pki/apiserver.crt -text
```
