
# Удалить Longhorn
kubectl -n longhorn-system edit settings.longhorn.io deleting-confirmation-flag

Change this:

apiVersion: longhorn.io/v1beta2
kind: Setting
metadata:
  name: deleting-confirmation-flag
value: "false"

To:

value: "true"

helm uninstall -n longhorn-system longhorn