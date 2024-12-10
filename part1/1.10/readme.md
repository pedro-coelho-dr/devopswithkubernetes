```bash
❯ kubectl get pods

NAME                           READY   STATUS    RESTARTS      AGE
log-output-54c89b69db-8zt9n    2/2     Running   0             2m14s
pingpong-app-5d47c8c7f-hswng   1/1     Running   1 (45m ago)   13h
todo-app-644f75fdc9-wsdxp      1/1     Running   1 (45m ago)   13h


❯ kubectl describe pod log-output-54c89b69db-8zt9n

Name:             log-output-54c89b69db-8zt9n
Namespace:        default
Priority:         0
Service Account:  default
Node:             k3d-my-cluster-server-0/172.19.0.3
Start Time:       Tue, 10 Dec 2024 00:24:45 -0300
Labels:           app=log-output
                  pod-template-hash=54c89b69db
Annotations:      <none>
Status:           Running
IP:               10.42.2.11
IPs:
  IP:           10.42.2.11
Controlled By:  ReplicaSet/log-output-54c89b69db
Containers:
  writer:
    Container ID:   containerd://16d103b9251def8ca1f810a5336a33f0a16efeb4b8897a209a01aef050c2ce7a
    Image:          pedrocoelhodr/log-output:writer-1.0
    Image ID:       docker.io/pedrocoelhodr/log-output@sha256:fea10fe8906292679e2545b1ffea0df6c241c9472d4e5f6c76bd1e0eaf4720e0
    Port:           <none>
    Host Port:      <none>
    State:          Running
      Started:      Tue, 10 Dec 2024 00:24:49 -0300
    Ready:          True
    Restart Count:  0
    Limits:
      cpu:     500m
      memory:  128Mi
    Requests:
      cpu:        250m
      memory:     64Mi
    Environment:  <none>
    Mounts:
      /usr/src/app/data from shared-logs (rw)
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-c646h (ro)
  reader:
    Container ID:   containerd://4519d163eb33d425347024aaf6b0e7d39752f78ef494dbc11a5eccfd1cbbaa15
    Image:          pedrocoelhodr/log-output:reader-1.1
    Image ID:       docker.io/pedrocoelhodr/log-output@sha256:221305f8422e1458fdedbc291f289b9b6ab2397aefc5caa9d2398c78a67454ae
    Port:           <none>
    Host Port:      <none>
    State:          Running
      Started:      Tue, 10 Dec 2024 00:24:52 -0300
    Ready:          True
    Restart Count:  0
    Limits:
      cpu:     500m
      memory:  128Mi
    Requests:
      cpu:        250m
      memory:     64Mi
    Environment:  <none>
    Mounts:
      /usr/src/app/data from shared-logs (rw)
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-c646h (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   True 
  Initialized                 True 
  Ready                       True 
  ContainersReady             True 
  PodScheduled                True 
Volumes:
  shared-logs:
    Type:       EmptyDir (a temporary directory that shares a pod's lifetime)
    Medium:     
    SizeLimit:  <unset>
  kube-api-access-c646h:
    Type:                    Projected (a volume that contains injected data from multiple sources)
    TokenExpirationSeconds:  3607
    ConfigMapName:           kube-root-ca.crt
    ConfigMapOptional:       <nil>
    DownwardAPI:             true
QoS Class:                   Burstable
Node-Selectors:              <none>
Tolerations:                 node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
                             node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
Events:
  Type    Reason     Age    From               Message
  ----    ------     ----   ----               -------
  Normal  Scheduled  2m30s  default-scheduler  Successfully assigned default/log-output-54c89b69db-8zt9n to k3d-my-cluster-server-0
  Normal  Pulling    2m31s  kubelet            Pulling image "pedrocoelhodr/log-output:writer-1.0"
  Normal  Pulled     2m27s  kubelet            Successfully pulled image "pedrocoelhodr/log-output:writer-1.0" in 3.039s (3.039s including waiting). Image size: 44140801 bytes.
  Normal  Created    2m27s  kubelet            Created container writer
  Normal  Started    2m27s  kubelet            Started container writer
  Normal  Pulling    2m27s  kubelet            Pulling image "pedrocoelhodr/log-output:reader-1.1"
  Normal  Pulled     2m24s  kubelet            Successfully pulled image "pedrocoelhodr/log-output:reader-1.1" in 3.586s (3.586s including waiting). Image size: 49127062 bytes.
  Normal  Created    2m24s  kubelet            Created container reader
  Normal  Started    2m24s  kubelet            Started container reader


```