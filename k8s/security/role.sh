echo -n "
kind: ClusterRoleBinding
apiVersion: rbac.authorization.k8s.io/v1beta1
metadata:
  name: cluster-admin-user
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: cluster-admin
subjects:
- kind: User
  name: <the current user using kubectl> # usually the Google account
                                         # eg: harry@konghq.com
  namespace: kube-system" | kubectl apply -f -