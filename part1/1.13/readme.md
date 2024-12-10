```bash
❯ kubectl get pods -o wide

NAME                          READY   STATUS    RESTARTS      AGE     IP           NODE                     NOMINATED NODE   READINESS GATES
log-output-75758b6b6c-p4t7b   2/2     Running   4 (86m ago)   13h     10.42.0.15   k3d-my-cluster-agent-0   <none>           <none>
ping-pong-66d748ff54-pwxwg    1/1     Running   2 (86m ago)   13h     10.42.0.16   k3d-my-cluster-agent-0   <none>           <none>
todo-app-7859747b5c-rl54r     1/1     Running   0             2m33s   10.42.1.18   k3d-my-cluster-agent-1   <none>           <none>
❯ kubectl get services

NAME               TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)    AGE
kubernetes         ClusterIP   10.43.0.1       <none>        443/TCP    13h
log-output-svc     ClusterIP   10.43.54.214    <none>        2345/TCP   13h
pingpong-service   ClusterIP   10.43.56.255    <none>        2345/TCP   13h
todo-app-service   ClusterIP   10.43.103.221   <none>        80/TCP     13h
❯ kubectl get ingress

NAME                 CLASS     HOSTS   ADDRESS                            PORTS   AGE
log-output-ingress   traefik   *       172.19.0.3,172.19.0.4,172.19.0.5   80      13h
pingpong-ingress     traefik   *       172.19.0.3,172.19.0.4,172.19.0.5   80      13h
todo-app-ingress     traefik   *       172.19.0.3,172.19.0.4,172.19.0.5   80      13h
❯ kubectl logs -l app=todo-app

10.42.1.13 - - [10/Dec/2024 19:40:57] "GET /image.jpg HTTP/1.1" 304 -
10.42.1.13 - - [10/Dec/2024 19:40:58] "GET /todo HTTP/1.1" 200 -
10.42.1.13 - - [10/Dec/2024 19:40:58] "GET /static/style.css HTTP/1.1" 304 -
10.42.1.13 - - [10/Dec/2024 19:40:58] "GET /image.jpg HTTP/1.1" 304 -
10.42.1.13 - - [10/Dec/2024 19:41:00] "GET /todo HTTP/1.1" 200 -
10.42.1.13 - - [10/Dec/2024 19:41:00] "GET /image.jpg HTTP/1.1" 304 -
10.42.1.13 - - [10/Dec/2024 19:41:00] "GET /static/style.css HTTP/1.1" 304 -
10.42.1.13 - - [10/Dec/2024 19:41:17] "GET /todo HTTP/1.1" 200 -
10.42.1.13 - - [10/Dec/2024 19:41:17] "GET /image.jpg HTTP/1.1" 200 -
10.42.1.13 - - [10/Dec/2024 19:41:17] "GET /static/style.css HTTP/1.1" 304 -

```


