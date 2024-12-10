


```bash

❯ kubectl get nodes --show-labels
NAME                      STATUS   ROLES                  AGE   VERSION        LABELS
k3d-my-cluster-agent-0    Ready    <none>                 25m   v1.30.6+k3s1   beta.kubernetes.io/arch=amd64,beta.kubernetes.io/instance-type=k3s,beta.kubernetes.io/os=linux,kubernetes.io/arch=amd64,kubernetes.io/hostname=k3d-my-cluster-agent-0,kubernetes.io/os=linux,node.kubernetes.io/instance-type=k3s,project=pingpong-log
k3d-my-cluster-agent-1    Ready    <none>                 25m   v1.30.6+k3s1   beta.kubernetes.io/arch=amd64,beta.kubernetes.io/instance-type=k3s,beta.kubernetes.io/os=linux,kubernetes.io/arch=amd64,kubernetes.io/hostname=k3d-my-cluster-agent-1,kubernetes.io/os=linux,node.kubernetes.io/instance-type=k3s,project=todo
k3d-my-cluster-server-0   Ready    control-plane,master   25m   v1.30.6+k3s1   beta.kubernetes.io/arch=amd64,beta.kubernetes.io/instance-type=k3s,beta.kubernetes.io/os=linux,kubernetes.io/arch=amd64,kubernetes.io/hostname=k3d-my-cluster-server-0,kubernetes.io/os=linux,node-role.kubernetes.io/control-plane=true,node-role.kubernetes.io/master=true,node.kubernetes.io/instance-type=k3s

❯ kubectl get pv
❯ kubectl get pvc
NAME        CAPACITY   ACCESS MODES   RECLAIM POLICY   STATUS   CLAIM                STORAGECLASS     VOLUMEATTRIBUTESCLASS   REASON   AGE
shared-pv   1Gi        RWX            Retain           Bound    default/shared-pvc   shared-storage   <unset>                          23m
NAME         STATUS   VOLUME      CAPACITY   ACCESS MODES   STORAGECLASS     VOLUMEATTRIBUTESCLASS   AGE
shared-pvc   Bound    shared-pv   1Gi        RWX            shared-storage   <unset>                 23m

❯ kubectl get pods -o wide
NAME                          READY   STATUS    RESTARTS   AGE   IP          NODE                     NOMINATED NODE   READINESS GATES
log-output-75758b6b6c-p4t7b   2/2     Running   0          22m   10.42.0.5   k3d-my-cluster-agent-0   <none>           <none>
ping-pong-66d748ff54-pwxwg    1/1     Running   0          22m   10.42.0.6   k3d-my-cluster-agent-0   <none>           <none>
todo-app-54c49db7fc-88dld     1/1     Running   0          22m   10.42.1.6   k3d-my-cluster-agent-1   <none>           <none>


❯ kubectl get all
NAME                              READY   STATUS    RESTARTS   AGE
pod/log-output-75758b6b6c-p4t7b   2/2     Running   0          21m
pod/ping-pong-66d748ff54-pwxwg    1/1     Running   0          21m
pod/todo-app-54c49db7fc-88dld     1/1     Running   0          21m

NAME                       TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)    AGE
service/kubernetes         ClusterIP   10.43.0.1       <none>        443/TCP    23m
service/log-output-svc     ClusterIP   10.43.54.214    <none>        2345/TCP   21m
service/pingpong-service   ClusterIP   10.43.56.255    <none>        2345/TCP   21m
service/todo-app-service   ClusterIP   10.43.103.221   <none>        80/TCP     21m

NAME                         READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/log-output   1/1     1            1           21m
deployment.apps/ping-pong    1/1     1            1           21m
deployment.apps/todo-app     1/1     1            1           21m

NAME                                    DESIRED   CURRENT   READY   AGE
replicaset.apps/log-output-75758b6b6c   1         1         1       21m
replicaset.apps/ping-pong-66d748ff54    1         1         1       21m
replicaset.apps/todo-app-54c49db7fc     1         1         1       21m

❯ curl http://localhost:8081/log
{"hash":"8143cdae7b361188f75aba552418d869a8df5a24ddeb76f00b54fbee713538b7","ping_pongs":5,"status":"verified","timestamp":"2024-12-10T06:14:08.350891+00:00"}

❯ curl http://localhost:8081/pingpong
{"response":"pong 6"}

❯ curl http://localhost:8081/log
{"hash":"e831e42334f60a77898a8696c9a9cb0382737b120a5775fb00f0890e51f9d232","ping_pongs":6,"status":"verified","timestamp":"2024-12-10T06:14:18.128668+00:00"}

❯ curl http://localhost:8081/log
{"hash":"e831e42334f60a77898a8696c9a9cb0382737b120a5775fb00f0890e51f9d232","ping_pongs":6,"status":"verified","timestamp":"2024-12-10T06:14:18.128668+00:00"}

```


