```bash
❯ kubectl get namespaces
NAME                 STATUS   AGE
default              Active   31h
gke-managed-cim      Active   31h
gke-managed-system   Active   31h
gmp-public           Active   31h
gmp-system           Active   31h
kube-node-lease      Active   31h
kube-public          Active   31h
kube-system          Active   31h
pingpong-log         Active   30h
todo-main            Active   10m
todo-test            Active   6m14s
todo-test2           Active   118s
```

```bash
❯ kubectl get pods -n todo-main
kubectl get pods -n todo-test
kubectl get pods -n todo-test2

NAME                            READY   STATUS    RESTARTS      AGE
todo-app-55d89f8549-76xvz       1/1     Running   0             10m
todo-backend-7bbb969785-w52dd   1/1     Running   2 (10m ago)   10m
todo-db-stset-0                 1/1     Running   0             10m
NAME                            READY   STATUS    RESTARTS        AGE
todo-app-554d9bd45b-6ptbs       1/1     Running   0               6m17s
todo-backend-7ff6fc6956-vdlpw   1/1     Running   2 (5m38s ago)   6m17s
todo-db-stset-0                 1/1     Running   0               6m16s
NAME                            READY   STATUS    RESTARTS       AGE
todo-app-847dc4d9d4-jw55t       1/1     Running   0              2m2s
todo-backend-577569c9f4-wktzn   1/1     Running   2 (108s ago)   2m2s
todo-db-stset-0                 1/1     Running   0              2m2s

```

```bash
❯ kubectl get services -n todo-main
kubectl get services -n todo-test
kubectl get services -n todo-test2

NAME                   TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
todo-app-service       LoadBalancer   34.118.229.211   <pending>     80:32749/TCP     11m
todo-backend-service   LoadBalancer   34.118.225.230   <pending>     5001:32142/TCP   11m
todo-db-service        ClusterIP      None             <none>        5432/TCP         11m
NAME                   TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
todo-app-service       LoadBalancer   34.118.226.177   <pending>     80:30130/TCP     6m56s
todo-backend-service   LoadBalancer   34.118.231.35    34.88.20.33   5001:31628/TCP   6m56s
todo-db-service        ClusterIP      None             <none>        5432/TCP         6m56s
NAME                   TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
todo-app-service       LoadBalancer   34.118.229.79    <pending>     80:31898/TCP     2m42s
todo-backend-service   LoadBalancer   34.118.232.180   <pending>     5001:31511/TCP   2m41s
todo-db-service        ClusterIP      None             <none>        5432/TCP         2m41s
❯ kubectl get ingress -n todo-main
kubectl get ingress -n todo-test
kubectl get ingress -n todo-test2

NAME                   CLASS    HOSTS   ADDRESS   PORTS   AGE
todo-app-ingress       <none>   *                 80      11m
todo-backend-ingress   <none>   *                 80      11m
NAME                   CLASS    HOSTS   ADDRESS          PORTS   AGE
todo-app-ingress       <none>   *                        80      7m
todo-backend-ingress   <none>   *       34.107.131.134   80      7m
NAME                   CLASS    HOSTS   ADDRESS   PORTS   AGE
todo-app-ingress       <none>   *                 80      2m46s
todo-backend-ingress   <none>   *                 80      2m45s

```

