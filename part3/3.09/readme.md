```bash
❯ kubectl top pods
kubectl top nodes
NAME                          CPU(cores)   MEMORY(bytes)   
log-output-5c5b8655fc-sx4qc   2m           39Mi            
postgres-stset-0              114m         37Mi            
NAME                                         CPU(cores)   CPU%   MEMORY(bytes)   MEMORY%   
gke-dwk-cluster-default-pool-33d4db8c-fwlb   121m         12%    1106Mi          39%       
gke-dwk-cluster-default-pool-33d4db8c-h4nf   573m         60%    1226Mi          43%       
gke-dwk-cluster-default-pool-33d4db8c-m2g0   125m         13%    1092Mi          38%       
gke-dwk-cluster-default-pool-33d4db8c-m778   94m          10%    1087Mi          38%       
❯ kubectl describe pod log-output-5c5b8655fc-sx4qc -n pingpong-log
Name:             log-output-5c5b8655fc-sx4qc
Namespace:        pingpong-log
Priority:         0
Service Account:  default
Node:             gke-dwk-cluster-default-pool-33d4db8c-h4nf/10.166.0.27
Start Time:       Mon, 13 Jan 2025 16:16:15 -0300
Labels:           app=log-output
                  pod-template-hash=5c5b8655fc
Annotations:      <none>
Status:           Running
IP:               10.116.3.9
IPs:
  IP:           10.116.3.9
Controlled By:  ReplicaSet/log-output-5c5b8655fc
Containers:
  writer:
    Container ID:   containerd://190daf617e177818eb1a890b32ede0a294d371e2d63c14fcf4de887bec8740c1
    Image:          pedrocoelhodr/log-output:writer-1.7
    Image ID:       docker.io/pedrocoelhodr/log-output@sha256:7577309c4fcc7a5f254b996f90d2b11dbe82c5f5e032928075da0ec5f783ae96
    Port:           3001/TCP
    Host Port:      0/TCP
    State:          Running
      Started:      Mon, 13 Jan 2025 16:16:25 -0300
    Ready:          True
    Restart Count:  0
    Limits:
      cpu:     100m
      memory:  64Mi
    Requests:
      cpu:        50m
      memory:     32Mi
    Environment:  <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-5rj9c (ro)
  reader:
    Container ID:   containerd://6a9a8255687e051ceb4504d4fc92c4dc40ce61254adfbff3f876ed9a013a6219
    Image:          pedrocoelhodr/log-output:reader-1.8
    Image ID:       docker.io/pedrocoelhodr/log-output@sha256:9e48bb6e0b3c6c451cc17b7f42bd264cac273cdca85645ffe32cfe652910a312
    Port:           3002/TCP
    Host Port:      0/TCP
    State:          Running
      Started:      Mon, 13 Jan 2025 16:16:31 -0300
    Ready:          True
    Restart Count:  0
    Limits:
      cpu:     100m
      memory:  64Mi
    Requests:
      cpu:     50m
      memory:  32Mi
    Environment:
      MESSAGE:  <set to the key 'MESSAGE' of config map 'log-output-configmap'>  Optional: false
    Mounts:
      /config from config-volume (ro)
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-5rj9c (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   True 
  Initialized                 True 
  Ready                       True 
  ContainersReady             True 
  PodScheduled                True 
Volumes:
  config-volume:
    Type:      ConfigMap (a volume populated by a ConfigMap)
    Name:      log-output-configmap
    Optional:  false
  kube-api-access-5rj9c:
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
  Normal  Scheduled  2m29s  default-scheduler  Successfully assigned pingpong-log/log-output-5c5b8655fc-sx4qc to gke-dwk-cluster-default-pool-33d4db8c-h4nf
  Normal  Pulling    2m28s  kubelet            Pulling image "pedrocoelhodr/log-output:writer-1.7"
  Normal  Pulled     2m19s  kubelet            Successfully pulled image "pedrocoelhodr/log-output:writer-1.7" in 9.177s (9.177s including waiting)
  Normal  Created    2m19s  kubelet            Created container writer
  Normal  Started    2m19s  kubelet            Started container writer
  Normal  Pulling    2m19s  kubelet            Pulling image "pedrocoelhodr/log-output:reader-1.8"
  Normal  Pulled     2m13s  kubelet            Successfully pulled image "pedrocoelhodr/log-output:reader-1.8" in 5.811s (5.811s including waiting)
  Normal  Created    2m13s  kubelet            Created container reader
  Normal  Started    2m13s  kubelet            Started container reader
  ```