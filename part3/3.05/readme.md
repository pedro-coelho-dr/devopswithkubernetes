```bash
❯ kubectl get pods -n todo

NAME                            READY   STATUS      RESTARTS        AGE
todo-app-644586bc56-76mw6       1/1     Running     0               7m21s
todo-backend-77f69b4476-hnf62   1/1     Running     5 (6m16s ago)   7m52s
todo-cronjob-28915440-9vkxs     0/1     Completed   4               5m51s
todo-db-stset-0                 1/1     Running     0               5m26s
❯ kubectl describe service todo-app-service -n todo

Name:                     todo-app-service
Namespace:                todo
Labels:                   <none>
Annotations:              cloud.google.com/neg: {"ingress":true}
Selector:                 app=todo-app
Type:                     LoadBalancer
IP Family Policy:         SingleStack
IP Families:              IPv4
IP:                       34.118.231.246
IPs:                      34.118.231.246
LoadBalancer Ingress:     35.228.81.130
Port:                     <unset>  80/TCP
TargetPort:               5000/TCP
NodePort:                 <unset>  32663/TCP
Endpoints:                10.16.1.15:5000
Session Affinity:         None
External Traffic Policy:  Cluster
Internal Traffic Policy:  Cluster
Events:                   <none>

```

```bash
❯ kubectl get services -n todo

NAME                   TYPE           CLUSTER-IP       EXTERNAL-IP     PORT(S)          AGE
todo-app-service       LoadBalancer   34.118.231.246   35.228.81.130   80:32663/TCP     71m
todo-backend-service   LoadBalancer   34.118.231.61    35.228.95.56    5001:30827/TCP   71m
todo-db-service        ClusterIP      None             <none>          5432/TCP         71m
❯ kubectl get ingress -n todo

NAME                   CLASS    HOSTS   ADDRESS   PORTS   AGE
todo-app-ingress       <none>   *                 80      71m
todo-backend-ingress   <none>   *                 80      71m
❯ kubectl get deployments -n todo

NAME           READY   UP-TO-DATE   AVAILABLE   AGE
todo-app       1/1     1            1           71m
todo-backend   1/1     1            1           71m

```

```bash

❯ kubectl get all -n todo

NAME                                READY   STATUS      RESTARTS        AGE
pod/todo-app-644586bc56-76mw6       1/1     Running     0               8m22s
pod/todo-backend-77f69b4476-hnf62   1/1     Running     5 (7m17s ago)   8m53s
pod/todo-cronjob-28915440-9vkxs     0/1     Completed   4               6m52s
pod/todo-db-stset-0                 1/1     Running     0               6m27s

NAME                           TYPE           CLUSTER-IP       EXTERNAL-IP     PORT(S)          AGE
service/todo-app-service       LoadBalancer   34.118.231.246   35.228.81.130   80:32663/TCP     72m
service/todo-backend-service   LoadBalancer   34.118.231.61    35.228.95.56    5001:30827/TCP   72m
service/todo-db-service        ClusterIP      None             <none>          5432/TCP         72m

NAME                           READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/todo-app       1/1     1            1           72m
deployment.apps/todo-backend   1/1     1            1           72m

NAME                                      DESIRED   CURRENT   READY   AGE
replicaset.apps/todo-app-5c899689d9       0         0         0       20m
replicaset.apps/todo-app-644586bc56       1         1         1       8m23s
replicaset.apps/todo-app-6c56978767       0         0         0       69m
replicaset.apps/todo-app-7cff59b8f9       0         0         0       72m
replicaset.apps/todo-app-d6bc6b7b6        0         0         0       56m
replicaset.apps/todo-backend-5645555bd5   0         0         0       72m
replicaset.apps/todo-backend-646d9f496f   0         0         0       69m
replicaset.apps/todo-backend-77f69b4476   1         1         1       8m54s
replicaset.apps/todo-backend-79f74cf5c8   0         0         0       56m
replicaset.apps/todo-backend-9bdb78465    0         0         0       20m

NAME                             READY   AGE
statefulset.apps/todo-db-stset   1/1     6m30s

NAME                         SCHEDULE    SUSPEND   ACTIVE   LAST SCHEDULE   AGE
cronjob.batch/todo-cronjob   0 * * * *   False     0        6m54s           72m

NAME                              COMPLETIONS   DURATION   AGE
job.batch/todo-cronjob-28915380   0/1           66m        66m
job.batch/todo-cronjob-28915440   1/1           99s        6m54s
```

