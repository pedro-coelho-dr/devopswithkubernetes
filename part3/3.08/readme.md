```bash
❯ kubectl top pods
kubectl top nodes

NAME                            CPU(cores)   MEMORY(bytes)   
todo-app-5dbd6d786c-299d4       1m           24Mi            
todo-backend-79df878b87-z9jls   1m           22Mi            
todo-db-stset-0                 1m           22Mi            
NAME                                         CPU(cores)   CPU%   MEMORY(bytes)   MEMORY%   
gke-dwk-cluster-default-pool-33d4db8c-fwlb   108m         11%    1116Mi          39%       
gke-dwk-cluster-default-pool-33d4db8c-h4nf   111m         11%    1015Mi          36%       
gke-dwk-cluster-default-pool-33d4db8c-m2g0   74m          7%     1001Mi          35%       
gke-dwk-cluster-default-pool-33d4db8c-m778   91m          9%     891Mi           31%       
❯ kubectl describe pod todo-app-5dbd6d786c-299d4 -n todo-main

Name:             todo-app-5dbd6d786c-299d4
Namespace:        todo-main
Priority:         0
Service Account:  default
Node:             gke-dwk-cluster-default-pool-33d4db8c-h4nf/10.166.0.27
Start Time:       Mon, 13 Jan 2025 15:59:03 -0300
Labels:           app=todo-app
                  pod-template-hash=5dbd6d786c
Annotations:      <none>
Status:           Running
IP:               10.116.3.7
IPs:
  IP:           10.116.3.7
Controlled By:  ReplicaSet/todo-app-5dbd6d786c
Containers:
  todo-app:
    Container ID:   containerd://98465fc37fa8f322c25f41ef4eb146affebc65d5eca9e67cdb8430d8d0769b5a
    Image:          gcr.io/dwk-gke-445103/todo-app-frontend:main-3c50aa1aec69b7d535439607f93a88413806f017
    Image ID:       gcr.io/dwk-gke-445103/todo-app-frontend@sha256:455c12d6f0a49707347b3d4ef4e39601ba529dea88baabd8c35d3356dbc1716b
    Port:           5000/TCP
    Host Port:      0/TCP
    State:          Running
      Started:      Mon, 13 Jan 2025 15:59:10 -0300
    Ready:          True
    Restart Count:  0
    Limits:
      cpu:     300m
      memory:  128Mi
    Requests:
      cpu:        150m
      memory:     64Mi
    Environment:  <none>
    Mounts:
      /usr/src/app/data from todo-images (rw)
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-zsprk (ro)
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
  kube-api-access-zsprk:
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
  Normal  Scheduled  3m13s  default-scheduler  Successfully assigned todo-main/todo-app-5dbd6d786c-299d4 to gke-dwk-cluster-default-pool-33d4db8c-h4nf
  Normal  Pulling    3m12s  kubelet            Pulling image "gcr.io/dwk-gke-445103/todo-app-frontend:main-3c50aa1aec69b7d535439607f93a88413806f017"
  Normal  Pulled     3m7s   kubelet            Successfully pulled image "gcr.io/dwk-gke-445103/todo-app-frontend:main-3c50aa1aec69b7d535439607f93a88413806f017" in 4.932s (4.932s including waiting)
  Normal  Created    3m7s   kubelet            Created container todo-app
  Normal  Started    3m6s   kubelet            Started container todo-app
  ``` 