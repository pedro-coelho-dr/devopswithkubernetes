```bash

❯ curl http://34.160.208.107/
curl http://34.160.208.107/log

{"message":"Log Output Service is running"}
{"env variable":"MESSAGE=hello world","file content":"this text is from file","hash":"281d1b0dbd3d40e4b4278a843bf9698b4718e8768f9181ead72e0ae03b07d389","ping_pongs":0,"status":"verified","timestamp":"2024-12-22T21:13:48.921448+00:00"}
❯ curl http://34.120.142.238/
curl http://34.120.142.238/pingpong
curl http://34.120.142.238/getpong

{"message":"Welcome to Ping-Pong Service"}
{"response":"pong 7"}
{"count":7}

```



```bash
❯ kubectl get all -n pingpong-log

NAME                             READY   STATUS    RESTARTS   AGE
pod/log-output-8ff54b9c5-snvgg   2/2     Running   0          21m
pod/ping-pong-68778f8568-mr5gr   1/1     Running   0          4m35s
pod/postgres-stset-0             1/1     Running   0          5h43m

NAME                       TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)                         AGE
service/log-output-svc     NodePort    34.118.227.253   <none>        3002:30515/TCP,3001:30584/TCP   41m
service/pingpong-service   NodePort    34.118.238.29    <none>        3000:32420/TCP                  5h42m
service/postgres-service   ClusterIP   None             <none>        5432/TCP                        5h43m

NAME                         READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/log-output   1/1     1            1           41m
deployment.apps/ping-pong    1/1     1            1           5h42m

NAME                                    DESIRED   CURRENT   READY   AGE
replicaset.apps/log-output-5458959c88   0         0         0       41m
replicaset.apps/log-output-8ff54b9c5    1         1         1       21m
replicaset.apps/ping-pong-57949794dd    0         0         0       103m
replicaset.apps/ping-pong-68778f8568    1         1         1       4m36s
replicaset.apps/ping-pong-76b597f4f7    0         0         0       99m
replicaset.apps/ping-pong-76f48c88d7    0         0         0       5h42m
replicaset.apps/ping-pong-d69bbc67d     0         0         0       5h32m

NAME                              READY   AGE
statefulset.apps/postgres-stset   1/1     5h43m

```


```bash

❯ kubectl describe ingress log-output-ingress -n pingpong-log

Name:             log-output-ingress
Labels:           <none>
Namespace:        pingpong-log
Address:          34.160.208.107
Ingress Class:    <none>
Default backend:  <default>
Rules:
  Host        Path  Backends
  ----        ----  --------
  *           
              /      log-output-svc:reader (10.16.0.9:3002)
              /log   log-output-svc:reader (10.16.0.9:3002)
Annotations:  ingress.kubernetes.io/backends:
                {"k8s1-324ca321-kube-system-default-http-backend-80-9082e8cf":"HEALTHY","k8s1-324ca321-pingpong-log-log-output-svc-3002-3e83b203":"HEALTHY...
              ingress.kubernetes.io/forwarding-rule: k8s2-fr-ccboch3c-pingpong-log-log-output-ingress-2ru68ljr
              ingress.kubernetes.io/target-proxy: k8s2-tp-ccboch3c-pingpong-log-log-output-ingress-2ru68ljr
              ingress.kubernetes.io/url-map: k8s2-um-ccboch3c-pingpong-log-log-output-ingress-2ru68ljr
Events:
  Type    Reason     Age                   From                     Message
  ----    ------     ----                  ----                     -------
  Normal  Sync       37m                   loadbalancer-controller  UrlMap "k8s2-um-ccboch3c-pingpong-log-log-output-ingress-2ru68ljr" created
  Normal  Sync       37m                   loadbalancer-controller  TargetProxy "k8s2-tp-ccboch3c-pingpong-log-log-output-ingress-2ru68ljr" created
  Normal  Sync       37m                   loadbalancer-controller  ForwardingRule "k8s2-fr-ccboch3c-pingpong-log-log-output-ingress-2ru68ljr" created
  Normal  IPChanged  37m                   loadbalancer-controller  IP is now 34.160.208.107
  Normal  Sync       20m                   loadbalancer-controller  UrlMap "k8s2-um-ccboch3c-pingpong-log-log-output-ingress-2ru68ljr" updated
  Normal  Sync       6m57s (x11 over 40m)  loadbalancer-controller  Scheduled for sync
❯ kubectl describe ingress pingpong-ingress -n pingpong-log

Name:             pingpong-ingress
Labels:           <none>
Namespace:        pingpong-log
Address:          34.120.142.238
Ingress Class:    <none>
Default backend:  <default>
Rules:
  Host        Path  Backends
  ----        ----  --------
  *           
              /           pingpong-service:3000 (10.16.1.26:3000)
              /pingpong   pingpong-service:3000 (10.16.1.26:3000)
              /getpong    pingpong-service:3000 (10.16.1.26:3000)
Annotations:  ingress.kubernetes.io/backends:
                {"k8s1-324ca321-kube-system-default-http-backend-80-9082e8cf":"HEALTHY","k8s1-324ca321-pingpong-log-pingpong-service-3000-4e9ad854":"HEALT...
              ingress.kubernetes.io/forwarding-rule: k8s2-fr-ccboch3c-pingpong-log-pingpong-ingress-byj0gvtv
              ingress.kubernetes.io/target-proxy: k8s2-tp-ccboch3c-pingpong-log-pingpong-ingress-byj0gvtv
              ingress.kubernetes.io/url-map: k8s2-um-ccboch3c-pingpong-log-pingpong-ingress-byj0gvtv
Events:
  Type    Reason     Age                   From                     Message
  ----    ------     ----                  ----                     -------
  Normal  Sync       39m                   loadbalancer-controller  UrlMap "k8s2-um-ccboch3c-pingpong-log-pingpong-ingress-byj0gvtv" created
  Normal  Sync       39m                   loadbalancer-controller  TargetProxy "k8s2-tp-ccboch3c-pingpong-log-pingpong-ingress-byj0gvtv" created
  Normal  Sync       38m                   loadbalancer-controller  ForwardingRule "k8s2-fr-ccboch3c-pingpong-log-pingpong-ingress-byj0gvtv" created
  Normal  IPChanged  38m                   loadbalancer-controller  IP is now 34.120.142.238
  Normal  Sync       3m46s                 loadbalancer-controller  UrlMap "k8s2-um-ccboch3c-pingpong-log-pingpong-ingress-byj0gvtv" updated
  Normal  Sync       3m40s (x10 over 41m)  loadbalancer-controller  Scheduled for sync
❯ kubectl get endpoints pingpong-service -n pingpong-log

NAME               ENDPOINTS         AGE
pingpong-service   10.16.1.26:3000   5h42m
❯ kubectl get endpoints log-output-svc -n pingpong-log

NAME             ENDPOINTS                       AGE
log-output-svc   10.16.0.9:3001,10.16.0.9:3002   41m


```