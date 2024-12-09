```bash
❯ kubectl get pods
NAME                           READY   STATUS    RESTARTS   AGE
log-output-c795f5c74-b26v5     1/1     Running   0          78m
pingpong-app-5d47c8c7f-hswng   1/1     Running   0          45s
todo-app-644f75fdc9-wsdxp      1/1     Running   0          29m
❯ kubectl get deployments
NAME           READY   UP-TO-DATE   AVAILABLE   AGE
log-output     1/1     1            1           129m
pingpong-app   1/1     1            1           63s
todo-app       1/1     1            1           146m
❯ kubectl get services
NAME               TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)    AGE
kubernetes         ClusterIP   10.43.0.1       <none>        443/TCP    147m
log-output-svc     ClusterIP   10.43.141.156   <none>        2345/TCP   77m
pingpong-service   ClusterIP   10.43.96.249    <none>        2345/TCP   60s
todo-app-service   ClusterIP   10.43.89.197    <none>        80/TCP     146m
❯ kubectl get endpoints
NAME               ENDPOINTS         AGE
kubernetes         172.19.0.3:6443   147m
log-output-svc     10.42.2.6:3000    78m
pingpong-service   10.42.1.9:3000    84s
todo-app-service   10.42.0.5:5000    146m
❯ kubectl get ingress
NAME                 CLASS     HOSTS   ADDRESS                            PORTS   AGE
log-output-ingress   traefik   *       172.19.0.3,172.19.0.4,172.19.0.5   80      77m
pingpong-ingress     <none>    *       172.19.0.3,172.19.0.4,172.19.0.5   80      2m
todo-app-ingress     <none>    *       172.19.0.3,172.19.0.4,172.19.0.5   80      52m
❯ curl http://localhost:8081/pingpong

{"response":"pong 7"}
❯ curl http://localhost:8081/log

{"random_string":"34fc0c2d-73e4-4ea7-9c30-c2be485b794e","timestamp":"2024-12-09T14:23:44.370627+00:00"}
```