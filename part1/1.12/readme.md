```bash
❯ kubectl get pods -o wide
kubectl get services
kubectl get ingress
NAME                          READY   STATUS    RESTARTS      AGE     IP           NODE                     NOMINATED NODE   READINESS GATES
log-output-75758b6b6c-p4t7b   2/2     Running   4 (60m ago)   13h     10.42.0.15   k3d-my-cluster-agent-0   <none>           <none>
ping-pong-66d748ff54-pwxwg    1/1     Running   2 (60m ago)   13h     10.42.0.16   k3d-my-cluster-agent-0   <none>           <none>
todo-app-fcb69cb6d-mzgmr      1/1     Running   0             3m20s   10.42.1.17   k3d-my-cluster-agent-1   <none>           <none>
NAME               TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)    AGE
kubernetes         ClusterIP   10.43.0.1       <none>        443/TCP    13h
log-output-svc     ClusterIP   10.43.54.214    <none>        2345/TCP   13h
pingpong-service   ClusterIP   10.43.56.255    <none>        2345/TCP   13h
todo-app-service   ClusterIP   10.43.103.221   <none>        80/TCP     13h
NAME                 CLASS     HOSTS   ADDRESS                            PORTS   AGE
log-output-ingress   traefik   *       172.19.0.3,172.19.0.4,172.19.0.5   80      13h
pingpong-ingress     traefik   *       172.19.0.3,172.19.0.4,172.19.0.5   80      13h
todo-app-ingress     traefik   *       172.19.0.3,172.19.0.4,172.19.0.5   80      13h
❯ kubectl describe pod todo-app-fcb69cb6d-mzgmr
Name:             todo-app-fcb69cb6d-mzgmr
Namespace:        default
Priority:         0
Service Account:  default
Node:             k3d-my-cluster-agent-1/172.19.0.4
Start Time:       Tue, 10 Dec 2024 16:13:24 -0300
Labels:           app=todo-app
                  pod-template-hash=fcb69cb6d
Annotations:      <none>
Status:           Running
IP:               10.42.1.17
IPs:
  IP:           10.42.1.17
Controlled By:  ReplicaSet/todo-app-fcb69cb6d
Containers:
  todo-app:
    Container ID:   containerd://e0a5bdaea371680be16f2a0b83b7c512ae335ccad98d5186ee05ace5512fb627
    Image:          pedrocoelhodr/todo-app:1.5
    Image ID:       docker.io/pedrocoelhodr/todo-app@sha256:b9d763dd72427c4756311eb2c6e38e99b37dd37a32a49469a2438a2105369712
    Port:           5000/TCP
    Host Port:      0/TCP
    State:          Running
      Started:      Tue, 10 Dec 2024 16:13:24 -0300
    Ready:          True
    Restart Count:  0
    Limits:
      cpu:     500m
      memory:  128Mi
    Requests:
      cpu:     250m
      memory:  64Mi
    Environment:
      PORT:  5000
    Mounts:
      /usr/src/app/data from todo-images (rw)
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-5srtk (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   True 
  Initialized                 True 
  Ready                       True 
  ContainersReady             True 
  PodScheduled                True 
Volumes:
  todo-images:
    Type:       PersistentVolumeClaim (a reference to a PersistentVolumeClaim in the same namespace)
    ClaimName:  todo-pvc
    ReadOnly:   false
  kube-api-access-5srtk:
    Type:                    Projected (a volume that contains injected data from multiple sources)
    TokenExpirationSeconds:  3607
    ConfigMapName:           kube-root-ca.crt
    ConfigMapOptional:       <nil>
    DownwardAPI:             true
QoS Class:                   Burstable
Node-Selectors:              project=todo
Tolerations:                 node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
                             node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
Events:
  Type    Reason     Age    From               Message
  ----    ------     ----   ----               -------
  Normal  Scheduled  3m42s  default-scheduler  Successfully assigned default/todo-app-fcb69cb6d-mzgmr to k3d-my-cluster-agent-1
  Normal  Pulled     3m42s  kubelet            Container image "pedrocoelhodr/todo-app:1.5" already present on machine
  Normal  Created    3m42s  kubelet            Created container todo-app
  Normal  Started    3m42s  kubelet            Started container todo-app
❯ kubectl logs -l app=todo-app

10.42.1.13 - - [10/Dec/2024 19:15:44] "GET /image.jpg HTTP/1.1" 304 -
10.42.1.13 - - [10/Dec/2024 19:15:55] "GET /todo HTTP/1.1" 200 -
10.42.1.13 - - [10/Dec/2024 19:15:55] "GET /static/style.css HTTP/1.1" 304 -
10.42.1.13 - - [10/Dec/2024 19:15:55] "GET /image.jpg HTTP/1.1" 304 -
10.42.1.13 - - [10/Dec/2024 19:15:56] "GET /todo HTTP/1.1" 200 -
10.42.1.13 - - [10/Dec/2024 19:15:56] "GET /static/style.css HTTP/1.1" 304 -
10.42.1.13 - - [10/Dec/2024 19:15:56] "GET /image.jpg HTTP/1.1" 304 -
10.42.1.13 - - [10/Dec/2024 19:16:25] "GET /todo HTTP/1.1" 200 -
10.42.1.13 - - [10/Dec/2024 19:16:25] "GET /static/style.css HTTP/1.1" 304 -
10.42.1.13 - - [10/Dec/2024 19:16:25] "GET /image.jpg HTTP/1.1" 200 -
❯ kubectl exec -it todo-app-fcb69cb6d-mzgmr -- /bin/sh

> cd /usr/src/app/data
ls -l
> total 48
-rw-r--r-- 1 root root 47903 Dec 10 19:16 image.jpg
> stat image.jpg
  File: image.jpg
  Size: 47903           Blocks: 96         IO Block: 4096   regular file
Device: 0,168   Inode: 4468        Links: 1
Access: (0644/-rw-r--r--)  Uid: (    0/    root)   Gid: (    0/    root)
Access: 2024-12-10 19:16:25.281641452 +0000
Modify: 2024-12-10 19:16:25.260959628 +0000
Change: 2024-12-10 19:16:25.260959628 +0000
 Birth: 2024-12-10 19:14:11.879435578 +0000

```


