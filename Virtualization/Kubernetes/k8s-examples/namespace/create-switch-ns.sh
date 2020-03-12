#!/bin/bash -ex

usage() {
    echo "Usage: $0 -n <namespace-to-create> [-u <context-user> -c <context-cluster>]"
    echo "Creates a new namespace and context for it, and switches to the context"
    exit -1
}

while getopts ":n:u:c:d" opt; do
    case "${opt}" in
        n)
            ns=${OPTARG}
            ;;
        u)
            u=${OPTARG}
            ;;
        c)
            c=${OPTARG}
            ;;
        d)
            d="y"
            ;;
        *)
            usage
            ;;
    esac
done
shift $((OPTIND-1))

if [ -z "$ns" ]; then
    echo "Must specify a namespace name to create"
    usage
fi

create_ns() {
    user=${u:-"$(kubectl config view -o jsonpath={.users[0].name})"}
    cluster=${c:-"$(kubectl config view -o jsonpath={.clusters[0].name})"}
    kubectl create namespace $ns
    kubectl config set-context $ns --cluster=$cluster --user=$user --namespace=$ns
    kubectl config use-context $ns
}

delete_ns() {
    kubectl delete namespace $ns
    kubectl config delete-context $ns
    if [ $(kubectl config view -o jsonpath={.current-context}) == $ns ]; then
        kubectl config use-context $(kubectl config view -o jsonpath={.contexts[0].name})
    fi
}

if [ -z "$d" ]; then
    create_ns
else
    delete_ns
fi
