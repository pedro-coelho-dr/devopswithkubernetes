```bash
❯ kubectl get all -n todo-main
kubectl get hpa -n todo-main

NAME                                READY   STATUS      RESTARTS   AGE
pod/todo-app-54c98864f9-dz4ks       1/1     Running     0          42s
pod/todo-backend-574b5cfd55-bvfk2   1/1     Running     0          74s
pod/todo-cronjob-28940700-6zn5z     0/1     Completed   0          138m
pod/todo-cronjob-28940760-fgk6q     0/1     Completed   0          78m
pod/todo-cronjob-28940820-9pr5b     0/1     Completed   0          18m
pod/todo-db-stset-0                 1/1     Running     0          18h

NAME                           TYPE           CLUSTER-IP       EXTERNAL-IP    PORT(S)          AGE
service/todo-app-service       LoadBalancer   34.118.225.246   <pending>      80:31123/TCP     16d
service/todo-backend-service   LoadBalancer   34.118.227.228   35.228.95.56   5001:31242/TCP   16d
service/todo-db-service        ClusterIP      None             <none>         5432/TCP         16d

NAME                           READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/todo-app       1/1     1            1           16d
deployment.apps/todo-backend   1/1     1            1           16d

NAME                                      DESIRED   CURRENT   READY   AGE
replicaset.apps/todo-app-54856ff5d4       0         0         0       16d
replicaset.apps/todo-app-54c98864f9       1         1         1       44s
replicaset.apps/todo-app-54d4667cd7       0         0         0       16d
replicaset.apps/todo-app-587b979748       0         0         0       3m52s
replicaset.apps/todo-app-588cbd8d8        0         0         0       6m24s
replicaset.apps/todo-app-5d9899dcbb       0         0         0       33m
replicaset.apps/todo-backend-5444555fb    0         0         0       16d
replicaset.apps/todo-backend-56fcfdb85b   0         0         0       33m
replicaset.apps/todo-backend-574b5cfd55   1         1         1       76s
replicaset.apps/todo-backend-5fcbcdb759   0         0         0       16d
replicaset.apps/todo-backend-7d4f796b8b   0         0         0       6m55s
replicaset.apps/todo-backend-95c5568db    0         0         0       4m24s

NAME                             READY   AGE
statefulset.apps/todo-db-stset   1/1     16d

NAME                                                    REFERENCE                 TARGETS              MINPODS   MAXPODS   REPLICAS   AGE
horizontalpodautoscaler.autoscaling/todo-backend-hpa    Deployment/todo-backend   cpu: <unknown>/50%   1         5         1          75s
horizontalpodautoscaler.autoscaling/todo-frontend-hpa   Deployment/todo-app       cpu: <unknown>/50%   1         5         1          75s

NAME                         SCHEDULE    TIMEZONE   SUSPEND   ACTIVE   LAST SCHEDULE   AGE
cronjob.batch/todo-cronjob   0 * * * *   <none>     False     0        18m             16d

NAME                              STATUS     COMPLETIONS   DURATION   AGE
job.batch/todo-cronjob-28938240   Failed     0/1           43h        43h
job.batch/todo-cronjob-28940700   Complete   1/1           6s         138m
job.batch/todo-cronjob-28940760   Complete   1/1           7s         78m
job.batch/todo-cronjob-28940820   Complete   1/1           13s        18m
NAME                REFERENCE                 TARGETS              MINPODS   MAXPODS   REPLICAS   AGE
todo-backend-hpa    Deployment/todo-backend   cpu: <unknown>/50%   1         5         1          76s
todo-frontend-hpa   Deployment/todo-app       cpu: <unknown>/50%   1         5         1          76s
```