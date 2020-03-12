Docs:
https://github.com/kubernetes/ingress-nginx/tree/master/docs
https://github.com/kubernetes/ingress-nginx/tree/master/docs/user-guide
https://github.com/kubernetes/ingress-nginx/blob/master/docs/examples/external-auth/README.md
https://docs.giantswarm.io/guides/advanced-ingress-configuration/

Deployment:
```
https://github.com/kubernetes/ingress-nginx/tree/master/deploy
```

Get version:
```
kubectl exec -it $POD_NAME -n $POD_NAMESPACE -- /nginx-ingress-controller --version
```

Get config:
```
kubectl -n <namespace> exec <nginx-ingress-controller-pod-name> -- cat /etc/nginx/nginx.conf
```

Dashboard:
https://github.com/kubernetes/ingress-nginx/tree/master/docs/examples/customization/custom-vts-metrics-prometheus#nginx-vts-dashboard
