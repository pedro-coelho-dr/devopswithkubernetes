```bash
❯ kubectl get nodes

NAME                      STATUS   ROLES                  AGE    VERSION
k3d-my-cluster-agent-0    Ready    <none>                 128m   v1.30.6+k3s1
k3d-my-cluster-agent-1    Ready    <none>                 128m   v1.30.6+k3s1
k3d-my-cluster-server-0   Ready    control-plane,master   128m   v1.30.6+k3s1
❯ kubectl cluster-info

Kubernetes control plane is running at https://0.0.0.0:40213
CoreDNS is running at https://0.0.0.0:40213/api/v1/namespaces/kube-system/services/kube-dns:dns/proxy
Metrics-server is running at https://0.0.0.0:40213/api/v1/namespaces/kube-system/services/https:metrics-server:https/proxy

To further debug and diagnose cluster problems, use 'kubectl cluster-info dump'.
❯ kubectl get ingress

NAME                 CLASS     HOSTS   ADDRESS                            PORTS   AGE
log-output-ingress   traefik   *       172.19.0.3,172.19.0.4,172.19.0.5   80      58m
todo-app-ingress     <none>    *       172.19.0.3,172.19.0.4,172.19.0.5   80      32m
❯ kubectl describe ingress todo-app-ingress

Name:             todo-app-ingress
Labels:           <none>
Namespace:        default
Address:          172.19.0.3,172.19.0.4,172.19.0.5
Ingress Class:    <none>
Default backend:  <default>
Rules:
  Host        Path  Backends
  ----        ----  --------
  *           
              /todo     todo-app-service:80 (10.42.0.5:5000)
              /static   todo-app-service:80 (10.42.0.5:5000)
Annotations:  kubernetes.io/ingress.class: traefik
Events:       <none>
❯ kubectl get services

NAME               TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)    AGE
kubernetes         ClusterIP   10.43.0.1       <none>        443/TCP    129m
log-output-svc     ClusterIP   10.43.141.156   <none>        2345/TCP   59m
todo-app-service   ClusterIP   10.43.89.197    <none>        80/TCP     128m
❯ kubectl get endpoints

NAME               ENDPOINTS         AGE
kubernetes         172.19.0.3:6443   129m
log-output-svc     10.42.2.6:3000    59m
todo-app-service   10.42.0.5:5000    128m
                                                                 k3d-my-cluster-server-0

```