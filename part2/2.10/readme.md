```bash

❯ curl -X POST http://localhost:8081/todos \
     -H "Content-Type: application/json" \
     -d '{"todo": "123456789011121314"}'
{"id":16,"message":"Todo added"}

❯ kubectl logs -n todo -l app=todo-backend --tail=50 -f

Server started in port 5001
 * Serving Flask app 'app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5001
 * Running on http://10.42.1.131:5001
Press CTRL+C to quit
10.42.1.126 - - [17/Dec/2024 20:55:12] "GET /todos HTTP/1.1" 200 -
10.42.1.126 - - [17/Dec/2024 20:55:15] "GET /todos HTTP/1.1" 200 -
10.42.1.126 - - [17/Dec/2024 20:55:16] "GET /todos HTTP/1.1" 200 -
10.42.1.126 - - [17/Dec/2024 20:55:24] "POST /todos HTTP/1.1" 201 -
10.42.1.126 - - [17/Dec/2024 20:55:24] "GET /todos HTTP/1.1" 200 -
10.42.1.125 - - [17/Dec/2024 20:56:57] "GET /todos HTTP/1.1" 200 -
10.42.1.125 - - [17/Dec/2024 20:58:44] "POST /todos?content="123456789011121314"&id="99" HTTP/1.1" 415 -
10.42.1.125 - - [17/Dec/2024 20:59:43] "POST /todos HTTP/1.1" 201 -
10.42.2.67 - - [17/Dec/2024 21:00:01] "POST /todos HTTP/1.1" 201 -
10.42.1.125 - - [17/Dec/2024 21:00:25] "POST /todos HTTP/1.1" 201 -
10.42.1.125 - - [17/Dec/2024 21:00:28] "POST /todos HTTP/1.1" 201 -
10.42.1.125 - - [17/Dec/2024 21:00:52] "GET /todos HTTP/1.1" 200 -
10.42.1.125 - - [17/Dec/2024 21:01:12] "GET /todos HTTP/1.1" 200 -
10.42.1.125 - - [17/Dec/2024 21:01:17] "POST /todos HTTP/1.1" 400 -
10.42.1.125 - - [17/Dec/2024 21:01:29] "POST /todos HTTP/1.1" 400 -
10.42.1.125 - - [17/Dec/2024 21:01:48] "POST /todos HTTP/1.1" 400 -
10.42.1.125 - - [17/Dec/2024 21:01:53] "POST /todos HTTP/1.1" 201 -


```

```bash
Common labels: {"app":"todo-backend","container":"todo-backend","filename":"/var/log/pods/todo_todo-backend-77c68dffd-lv9sh_329922ee-3c40-4a41-9ccc-84338b2c8ae0/todo-backend/0.log","job":"todo/todo-backend","namespace":"todo","node_name":"k3d-my-cluster-agent-1","pod":"todo-backend-77c68dffd-lv9sh","stream":"stderr"}
Line limit: "1000 (10 displayed)"
Total bytes processed: "3.24  kB"


2024-12-17 18:01:53.956	10.42.1.125 - - [17/Dec/2024 21:01:53] "POST /todos HTTP/1.1" 201 -
2024-12-17 18:01:48.411	10.42.1.125 - - [17/Dec/2024 21:01:48] "POST /todos HTTP/1.1" 400 -
2024-12-17 18:01:29.871	10.42.1.125 - - [17/Dec/2024 21:01:29] "POST /todos HTTP/1.1" 400 -
2024-12-17 18:01:17.945	10.42.1.125 - - [17/Dec/2024 21:01:17] "POST /todos HTTP/1.1" 400 -
2024-12-17 18:00:28.969	10.42.1.125 - - [17/Dec/2024 21:00:28] "POST /todos HTTP/1.1" 201 -
2024-12-17 18:00:25.732	10.42.1.125 - - [17/Dec/2024 21:00:25] "POST /todos HTTP/1.1" 201 -
2024-12-17 18:00:01.122	10.42.2.67 - - [17/Dec/2024 21:00:01] "POST /todos HTTP/1.1" 201 -
2024-12-17 17:59:43.277	10.42.1.125 - - [17/Dec/2024 20:59:43] "POST /todos HTTP/1.1" 201 -
2024-12-17 17:58:44.444	10.42.1.125 - - [17/Dec/2024 20:58:44] "POST /todos?content="123456789011121314"&id="99" HTTP/1.1" 415 -
2024-12-17 17:55:24.077	10.42.1.126 - - [17/Dec/2024 20:55:24] "POST /todos HTTP/1.1" 201 -

```


```bash


❯ kubectl get nodes && kubectl get namespaces

NAME                      STATUS   ROLES                  AGE     VERSION
k3d-my-cluster-agent-0    Ready    <none>                 7d15h   v1.30.6+k3s1
k3d-my-cluster-agent-1    Ready    <none>                 7d15h   v1.30.6+k3s1
k3d-my-cluster-server-0   Ready    control-plane,master   7d15h   v1.30.6+k3s1
NAME              STATUS   AGE
default           Active   7d15h
kube-node-lease   Active   7d15h
kube-public       Active   7d15h
kube-system       Active   7d15h
loki-stack        Active   96m
pingpong-log      Active   3d20h
prometheus        Active   7h15m
todo              Active   2d7h



❯ kubectl get pods --all-namespaces

NAMESPACE      NAME                                                     READY   STATUS      RESTARTS        AGE
kube-system    coredns-7b98449c4-jq4kg                                  1/1     Running     18 (110m ago)   7d15h
kube-system    helm-install-traefik-crd-wb8v8                           0/1     Completed   0               7d15h
kube-system    local-path-provisioner-595dcfc56f-lcgtz                  1/1     Running     22 (109m ago)   7d15h
kube-system    metrics-server-cdcc87586-xwg4f                           1/1     Running     23 (109m ago)   7d15h
kube-system    svclb-traefik-44b4a939-hxthd                             2/2     Running     36 (109m ago)   7d15h
kube-system    svclb-traefik-44b4a939-nxzj6                             2/2     Running     36 (110m ago)   7d15h
kube-system    svclb-traefik-44b4a939-zm52k                             2/2     Running     36 (110m ago)   7d15h
kube-system    traefik-d7c9c5778-5zzgb                                  1/1     Running     18 (110m ago)   7d15h
loki-stack     loki-0                                                   1/1     Running     0               96m
loki-stack     loki-promtail-9qqpx                                      1/1     Running     0               96m
loki-stack     loki-promtail-rd5bp                                      1/1     Running     0               96m
loki-stack     loki-promtail-sbwz9                                      1/1     Running     0               96m
pingpong-log   log-output-85d67fb69b-xq2vs                              2/2     Running     12 (109m ago)   2d1h
pingpong-log   ping-pong-6c4ddcfd76-5ltcj                               1/1     Running     6 (109m ago)    26h
pingpong-log   postgres-stset-0                                         1/1     Running     3 (110m ago)    26h
prometheus     alertmanager-prometheus-kube-prometheus-alertmanager-0   2/2     Running     4 (110m ago)    7h14m
prometheus     prometheus-grafana-5857d645d-sdwpv                       3/3     Running     3 (110m ago)    5h54m
prometheus     prometheus-kube-prometheus-operator-564bf674f4-l7488     1/1     Running     1 (110m ago)    6h24m
prometheus     prometheus-kube-state-metrics-d85c885bd-s9sn4            1/1     Running     2 (109m ago)    6h24m
prometheus     prometheus-prometheus-kube-prometheus-prometheus-0       2/2     Running     2 (110m ago)    6h24m
prometheus     prometheus-prometheus-node-exporter-n7xhj                1/1     Running     2 (110m ago)    7h14m
prometheus     prometheus-prometheus-node-exporter-tc5nr                1/1     Running     6 (108m ago)    7h14m
prometheus     prometheus-prometheus-node-exporter-vbxs4                1/1     Running     2 (110m ago)    7h14m
todo           todo-app-7646d9cdd7-xwcfd                                1/1     Running     2 (110m ago)    8h
todo           todo-backend-77c68dffd-lv9sh                             1/1     Running     0               17m
todo           todo-cronjob-28907700-b4jpr                              0/1     Completed   2               109m
todo           todo-cronjob-28907760-bz2pr                              0/1     Completed   0               72m
todo           todo-cronjob-28907820-nvlvh                              0/1     Completed   0               12m
todo           todo-db-stset-0                                          1/1     Running     1 (110m ago)    6h24m



❯ kubectl get pods -n prometheus

NAME                                                     READY   STATUS    RESTARTS       AGE
alertmanager-prometheus-kube-prometheus-alertmanager-0   2/2     Running   4 (110m ago)   7h14m
prometheus-grafana-5857d645d-sdwpv                       3/3     Running   3 (110m ago)   5h54m
prometheus-kube-prometheus-operator-564bf674f4-l7488     1/1     Running   1 (110m ago)   6h24m
prometheus-kube-state-metrics-d85c885bd-s9sn4            1/1     Running   2 (110m ago)   6h24m
prometheus-prometheus-kube-prometheus-prometheus-0       2/2     Running   2 (110m ago)   6h24m
prometheus-prometheus-node-exporter-n7xhj                1/1     Running   2 (110m ago)   7h14m
prometheus-prometheus-node-exporter-tc5nr                1/1     Running   6 (109m ago)   7h14m
prometheus-prometheus-node-exporter-vbxs4                1/1     Running   2 (110m ago)   7h14m
❯ kubectl get pods -n loki-stack

NAME                  READY   STATUS    RESTARTS   AGE
loki-0                1/1     Running   0          97m
loki-promtail-9qqpx   1/1     Running   0          97m
loki-promtail-rd5bp   1/1     Running   0          97m
loki-promtail-sbwz9   1/1     Running   0          97m




❯ kubectl get svc -n prometheus && kubectl get svc -n loki-stack

NAME                                      TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)                      AGE
alertmanager-operated                     ClusterIP   None            <none>        9093/TCP,9094/TCP,9094/UDP   7h14m
prometheus-grafana                        ClusterIP   10.43.189.9     <none>        80/TCP                       7h14m
prometheus-kube-prometheus-alertmanager   ClusterIP   10.43.179.189   <none>        9093/TCP,8080/TCP            7h14m
prometheus-kube-prometheus-operator       ClusterIP   10.43.77.220    <none>        443/TCP                      7h14m
prometheus-kube-prometheus-prometheus     ClusterIP   10.43.28.240    <none>        9090/TCP,8080/TCP            7h14m
prometheus-kube-state-metrics             ClusterIP   10.43.37.124    <none>        8080/TCP                     7h14m
prometheus-operated                       ClusterIP   None            <none>        9090/TCP                     7h14m
prometheus-prometheus-node-exporter       ClusterIP   10.43.58.28     <none>        9100/TCP                     7h14m
NAME              TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)    AGE
loki              ClusterIP   10.43.121.156   <none>        3100/TCP   97m
loki-headless     ClusterIP   None            <none>        3100/TCP   97m
loki-memberlist   ClusterIP   None            <none>        7946/TCP   97m

```


```
Common labels: {"app":"todo-backend","container":"todo-backend","filename":"/var/log/pods/todo_todo-backend-77c68dffd-lv9sh_329922ee-3c40-4a41-9ccc-84338b2c8ae0/todo-backend/0.log","job":"todo/todo-backend","namespace":"todo","node_name":"k3d-my-cluster-agent-1","pod":"todo-backend-77c68dffd-lv9sh","stream":"stderr"}
Line limit: "1000 (10 displayed)"
Total bytes processed: "3.24  kB"


2024-12-17 18:01:53.956	10.42.1.125 - - [17/Dec/2024 21:01:53] "POST /todos HTTP/1.1" 201 -
2024-12-17 18:01:48.411	10.42.1.125 - - [17/Dec/2024 21:01:48] "POST /todos HTTP/1.1" 400 -
2024-12-17 18:01:29.871	10.42.1.125 - - [17/Dec/2024 21:01:29] "POST /todos HTTP/1.1" 400 -
2024-12-17 18:01:17.945	10.42.1.125 - - [17/Dec/2024 21:01:17] "POST /todos HTTP/1.1" 400 -
2024-12-17 18:00:28.969	10.42.1.125 - - [17/Dec/2024 21:00:28] "POST /todos HTTP/1.1" 201 -
2024-12-17 18:00:25.732	10.42.1.125 - - [17/Dec/2024 21:00:25] "POST /todos HTTP/1.1" 201 -
2024-12-17 18:00:01.122	10.42.2.67 - - [17/Dec/2024 21:00:01] "POST /todos HTTP/1.1" 201 -
2024-12-17 17:59:43.277	10.42.1.125 - - [17/Dec/2024 20:59:43] "POST /todos HTTP/1.1" 201 -
2024-12-17 17:58:44.444	10.42.1.125 - - [17/Dec/2024 20:58:44] "POST /todos?content="123456789011121314"&id="99" HTTP/1.1" 415 -
2024-12-17 17:55:24.077	10.42.1.126 - - [17/Dec/2024 20:55:24] "POST /todos HTTP/1.1" 201 -

```