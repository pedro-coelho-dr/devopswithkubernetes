```bash

❯ k3d cluster delete my-cluster
k3d cluster create my-cluster --port 8082:30081@agent:0 -p 8081:80@loadbalancer --agents 2

INFO[0000] Deleting cluster 'my-cluster'                
INFO[0004] Deleting cluster network 'k3d-my-cluster'    
INFO[0004] Deleting 1 attached volumes...               
INFO[0004] Removing cluster details from default kubeconfig... 
INFO[0004] Removing standalone kubeconfig file (if there is one)... 
INFO[0004] Successfully deleted cluster my-cluster!     
INFO[0000] portmapping '8081:80' targets the loadbalancer: defaulting to [servers:*:proxy agents:*:proxy] 
INFO[0000] Prep: Network                                
INFO[0000] Created network 'k3d-my-cluster'             
INFO[0000] Created image volume k3d-my-cluster-images   
INFO[0000] Starting new tools node...                   
INFO[0000] Starting node 'k3d-my-cluster-tools'         
INFO[0001] Creating node 'k3d-my-cluster-server-0'      
INFO[0001] Creating node 'k3d-my-cluster-agent-0'       
INFO[0001] Creating node 'k3d-my-cluster-agent-1'       
INFO[0001] Creating LoadBalancer 'k3d-my-cluster-serverlb' 
INFO[0001] Using the k3d-tools node to gather environment information 
INFO[0001] Starting new tools node...                   
INFO[0002] Starting node 'k3d-my-cluster-tools'         
INFO[0003] Starting cluster 'my-cluster'                
INFO[0003] Starting servers...                          
INFO[0003] Starting node 'k3d-my-cluster-server-0'      
INFO[0006] Starting agents...                           
INFO[0006] Starting node 'k3d-my-cluster-agent-1'       
INFO[0006] Starting node 'k3d-my-cluster-agent-0'       
INFO[0010] Starting helpers...                          
INFO[0010] Starting node 'k3d-my-cluster-serverlb'      
INFO[0016] Injecting records for hostAliases (incl. host.k3d.internal) and for 5 network members into CoreDNS configmap... 
INFO[0018] Cluster 'my-cluster' created successfully!   
INFO[0018] You can now use it like this:                
kubectl cluster-info

❯ kubectl apply -f manifests/deployment.yaml
deployment.apps/todo-app created

❯ kubectl apply -f manifests/service.yaml
service/todo-app-service created

❯ kubectl get pods
NAME                        READY   STATUS    RESTARTS   AGE
todo-app-844c9d7d45-6cfzz   1/1     Running   0          30s

❯ kubectl get services
NAME               TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)        AGE
kubernetes         ClusterIP   10.43.0.1      <none>        443/TCP        74s
todo-app-service   NodePort    10.43.89.197   <none>        80:30081/TCP   15s

❯ docker ps
CONTAINER ID   IMAGE                            COMMAND                  CREATED              STATUS              PORTS                                                                    NAMES
7ae21a47bbef   ghcr.io/k3d-io/k3d-tools:5.7.5   "/app/k3d-tools noop"    About a minute ago   Up About a minute                                                                            k3d-my-cluster-tools
f60e900547e0   ghcr.io/k3d-io/k3d-proxy:5.7.5   "/bin/sh -c nginx-pr…"   About a minute ago   Up About a minute   0.0.0.0:8081->80/tcp, 0.0.0.0:40213->6443/tcp, 0.0.0.0:8082->30081/tcp   k3d-my-cluster-serverlb
e47b622bc4c6   rancher/k3s:v1.30.6-k3s1         "/bin/k3d-entrypoint…"   About a minute ago   Up About a minute                                                                            k3d-my-cluster-agent-1
22a7e6e465c0   rancher/k3s:v1.30.6-k3s1         "/bin/k3d-entrypoint…"   About a minute ago   Up About a minute                                                                            k3d-my-cluster-agent-0
d30bf1de2bbb   rancher/k3s:v1.30.6-k3s1         "/bin/k3d-entrypoint…"   About a minute ago   Up About a minute                                                                            k3d-my-cluster-server-0

```