DOCKER_REGISTRY_SERVER=
DOCKER_USER=
DOCKER_PASSWORD=
DOCKER_EMAIL=
kubectl create secret docker-registry myregistrykey --docker-server=$DOCKER_REGISTRY_SERVER --docker-username=$DOCKER_USER --docker-password=$DOCKER_PASSWORD --docker-email=$DOCKER_EMAIL

