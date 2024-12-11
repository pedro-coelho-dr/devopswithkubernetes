```bash
❯ kubectl get svc

NAME               TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)             AGE
kubernetes         ClusterIP   10.43.0.1       <none>        443/TCP             30h
log-output-svc     ClusterIP   10.43.54.214    <none>        2345/TCP,2346/TCP   30h
pingpong-service   ClusterIP   10.43.56.255    <none>        2345/TCP            30h
todo-app-service   ClusterIP   10.43.103.221   <none>        80/TCP              30h
❯ kubectl get pods

NAME                          READY   STATUS    RESTARTS       AGE
busybox                       1/1     Running   0              22m
log-output-68847f6cc6-9nd8s   2/2     Running   0              3m5s
ping-pong-6ccc865f6d-tvrjx    1/1     Running   0              57m
todo-app-7859747b5c-rl54r     1/1     Running   1 (117m ago)   16h


❯ kubectl logs log-output-68847f6cc6-9nd8s -c reader

 * Serving Flask app 'reader'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:3002
 * Running on http://10.42.0.27:3002
Press CTRL+C to quit
10.42.1.22 - - [11/Dec/2024 12:21:40] "GET /log HTTP/1.1" 200 -
10.42.0.1 - - [11/Dec/2024 12:21:43] "POST /update HTTP/1.1" 200 -
10.42.1.22 - - [11/Dec/2024 12:21:45] "GET /log HTTP/1.1" 200 -
10.42.1.22 - - [11/Dec/2024 12:21:46] "GET /log HTTP/1.1" 200 -
10.42.1.22 - - [11/Dec/2024 12:21:48] "GET /log HTTP/1.1" 200 -
10.42.0.1 - - [11/Dec/2024 12:21:48] "POST /update HTTP/1.1" 200 -


❯ kubectl logs ping-pong-6ccc865f6d-tvrjx

 * Serving Flask app 'app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:3000
 * Running on http://10.42.0.22:3000
Press CTRL+C to quit
10.42.1.22 - - [11/Dec/2024 11:42:24] "GET /pingpong HTTP/1.1" 200 -
10.42.1.22 - - [11/Dec/2024 11:42:26] "GET /pingpong HTTP/1.1" 200 -
10.42.1.22 - - [11/Dec/2024 11:42:27] "GET /pingpong HTTP/1.1" 200 -
10.42.1.22 - - [11/Dec/2024 11:43:08] "GET /pingpong HTTP/1.1" 200 -
10.42.1.22 - - [11/Dec/2024 11:55:35] "GET /pingpong HTTP/1.1" 200 -
10.42.1.22 - - [11/Dec/2024 11:56:55] "GET /pingpong HTTP/1.1" 200 -
10.42.1.22 - - [11/Dec/2024 11:56:56] "GET /pingpong HTTP/1.1" 200 -
127.0.0.1 - - [11/Dec/2024 12:04:35] "GET /getpong HTTP/1.1" 200 -
10.42.1.22 - - [11/Dec/2024 12:07:37] "GET /pingpong HTTP/1.1" 200 -
10.42.2.7 - - [11/Dec/2024 12:17:42] "GET /getpong HTTP/1.1" 200 -
10.42.0.27 - - [11/Dec/2024 12:21:40] "GET /getpong HTTP/1.1" 200 -

```


