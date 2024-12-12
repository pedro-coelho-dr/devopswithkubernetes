```bash
❯ kubectl run my-busybox --image=busybox --restart=Never --command -- sleep 3600

pod/my-busybox created
❯ kubectl exec -it my-busybox -- sh

/ # wget -qO - http://todo-backend-service:5001/todos
["10","learn kubernetes"]
/ # exit

❯ kubectl logs todo-app-6fc6696cc8-9rtvr

Server started in port 5000
 * Serving Flask app 'app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://10.42.1.34:5000
Press CTRL+C to quit
10.42.1.31 - - [12/Dec/2024 18:16:01] "GET /todo HTTP/1.1" 200 -
10.42.1.31 - - [12/Dec/2024 18:16:01] "GET /static/style.css HTTP/1.1" 200 -
10.42.1.31 - - [12/Dec/2024 18:16:01] "GET /image.jpg HTTP/1.1" 200 -
10.42.1.31 - - [12/Dec/2024 18:18:18] "GET /todo HTTP/1.1" 200 -
10.42.1.31 - - [12/Dec/2024 18:18:18] "GET /static/style.css HTTP/1.1" 304 -
10.42.1.31 - - [12/Dec/2024 18:18:18] "GET /image.jpg HTTP/1.1" 200 -
10.42.1.31 - - [12/Dec/2024 18:18:22] "POST /add-todo HTTP/1.1" 201 -
10.42.1.31 - - [12/Dec/2024 18:18:30] "GET /todo HTTP/1.1" 200 -
10.42.1.31 - - [12/Dec/2024 18:18:30] "GET /static/style.css HTTP/1.1" 304 -
10.42.1.31 - - [12/Dec/2024 18:18:30] "GET /image.jpg HTTP/1.1" 304 -
10.42.1.31 - - [12/Dec/2024 18:19:09] "POST /add-todo HTTP/1.1" 201 -
10.42.1.31 - - [12/Dec/2024 18:19:13] "GET /todo HTTP/1.1" 200 -
10.42.1.31 - - [12/Dec/2024 18:19:13] "GET /static/style.css HTTP/1.1" 304 -
10.42.1.31 - - [12/Dec/2024 18:19:13] "GET /image.jpg HTTP/1.1" 304 -
❯ kubectl logs todo-backend-646c7f6dff-llbbd

Server started in port 5001
 * Serving Flask app 'app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5001
 * Running on http://10.42.1.33:5001
Press CTRL+C to quit
10.42.1.31 - - [12/Dec/2024 18:13:09] "GET /todos HTTP/1.1" 200 -
10.42.1.34 - - [12/Dec/2024 18:16:01] "GET /todos HTTP/1.1" 200 -
10.42.1.34 - - [12/Dec/2024 18:18:18] "GET /todos HTTP/1.1" 200 -
10.42.1.34 - - [12/Dec/2024 18:18:22] "POST /todos HTTP/1.1" 201 -
10.42.1.34 - - [12/Dec/2024 18:18:30] "GET /todos HTTP/1.1" 200 -
10.42.1.34 - - [12/Dec/2024 18:19:09] "POST /todos HTTP/1.1" 201 -
10.42.1.34 - - [12/Dec/2024 18:19:13] "GET /todos HTTP/1.1" 200 -
10.42.2.11 - - [12/Dec/2024 18:30:54] "GET /todos HTTP/1.1" 200 -
❯ kubectl get pods
NAME                            READY   STATUS    RESTARTS      AGE
log-output-68847f6cc6-9nd8s     2/2     Running   4 (20m ago)   30h
my-busybox                      1/1     Running   0             107s
ping-pong-6ccc865f6d-tvrjx      1/1     Running   2 (20m ago)   31h
todo-app-6fc6696cc8-9rtvr       1/1     Running   0             16m
todo-backend-646c7f6dff-llbbd   1/1     Running   0             19m

```