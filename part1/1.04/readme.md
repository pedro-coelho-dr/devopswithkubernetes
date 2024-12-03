```bash
❯ kubectl get deployments
kubectl get pods

NAME         READY   UP-TO-DATE   AVAILABLE   AGE
log-output   2/2     2            2           4h11m
todo-app     2/2     2            2           85m
NAME                          READY   STATUS    RESTARTS   AGE
log-output-7dcc69c99f-d5hkp   1/1     Running   0          21m
log-output-7dcc69c99f-qfclv   1/1     Running   0          21m
todo-app-6fcc4f7c5c-fr7qd     1/1     Running   0          110s
todo-app-6fcc4f7c5c-rv6z9     1/1     Running   0          107s
```