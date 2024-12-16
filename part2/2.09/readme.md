```bash
❯ kubectl get all -n todo --show-labels

NAME                                READY   STATUS    RESTARTS       AGE     LABELS
pod/todo-app-6fc6696cc8-pjftn       1/1     Running   3 (152m ago)   27h     app=todo-app,pod-template-hash=6fc6696cc8
pod/todo-backend-68c8cc775f-hbjdl   1/1     Running   0              3m51s   app=todo-backend,pod-template-hash=68c8cc775f
pod/todo-db-stset-0                 1/1     Running   0              33m     app=todo-db,apps.kubernetes.io/pod-index=0,controller-revision-hash=todo-db-stset-596575f9c7,statefulset.kubernetes.io/pod-name=todo-db-stset-0

NAME                           TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)    AGE   LABELS
service/todo-app-service       ClusterIP   10.43.46.146    <none>        5000/TCP   27h   app=todo-app
service/todo-backend-service   ClusterIP   10.43.138.217   <none>        5001/TCP   27h   app=todo-backend
service/todo-db-service        ClusterIP   None            <none>        5432/TCP   39m   app=todo-db

NAME                           READY   UP-TO-DATE   AVAILABLE   AGE   LABELS
deployment.apps/todo-app       1/1     1            1           27h   app=todo-app
deployment.apps/todo-backend   1/1     1            1           27h   app=todo-backend

NAME                                      DESIRED   CURRENT   READY   AGE     LABELS
replicaset.apps/todo-app-6fc6696cc8       1         1         1       27h     app=todo-app,pod-template-hash=6fc6696cc8
replicaset.apps/todo-backend-646c7f6dff   0         0         0       27h     app=todo-backend,pod-template-hash=646c7f6dff
replicaset.apps/todo-backend-68c8cc775f   1         1         1       3m51s   app=todo-backend,pod-template-hash=68c8cc775f

NAME                             READY   AGE   LABELS
statefulset.apps/todo-db-stset   1/1     39m   app=todo-db

```

```bash
❯ curl -X POST -H "Content-Type: application/json" -d '{"todo": "Test Todo"}' http://localhost:8081/todos

{"id":3,"message":"Todo added"}
❯ curl -X GET http://localhost:8081/todos

[{"content":"teste","id":1},{"content":"teste2","id":2},{"content":"Test Todo","id":3}]
❯ kubectl exec -it todo-db-stset-0 -n todo -- /bin/bash

root@todo-db-stset-0:/# psql -U admin -d todo-db
psql (17.2 (Debian 17.2-1.pgdg120+1))
Type "help" for help.

todo-db=# SELECT * FROM todos;
 id |  content  
----+-----------
  1 | teste
  2 | teste2
  3 | Test Todo
(3 rows)
```
