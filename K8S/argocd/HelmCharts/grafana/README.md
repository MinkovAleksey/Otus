# Reset password
namespace=monitoring
kubectl exec --namespace $namespace -it $(kubectl get pods --namespace $namespace -l "app.kubernetes.io/name=grafana" -o jsonpath="{.items[0].metadata.name}") -- grafana cli admin reset-admin-password admin