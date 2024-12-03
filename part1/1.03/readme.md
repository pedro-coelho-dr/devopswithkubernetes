```bash
❯ kubectl cluster-info

Kubernetes control plane is running at https://0.0.0.0:38067
CoreDNS is running at https://0.0.0.0:38067/api/v1/namespaces/kube-system/services/kube-dns:dns/proxy
Metrics-server is running at https://0.0.0.0:38067/api/v1/namespaces/kube-system/services/https:metrics-server:https/proxy

To further debug and diagnose cluster problems, use 'kubectl cluster-info dump'.
❯ kubectl get nodes

NAME                       STATUS   ROLES                  AGE     VERSION
k3d-k3s-default-agent-0    Ready    <none>                 4h14m   v1.30.6+k3s1
k3d-k3s-default-agent-1    Ready    <none>                 4h14m   v1.30.6+k3s1
k3d-k3s-default-server-0   Ready    control-plane,master   4h14m   v1.30.6+k3s1
❯ kubectl get deployments

NAME         READY   UP-TO-DATE   AVAILABLE   AGE
log-output   2/2     2            2           3h52m
todo-app     1/1     1            1           66m
```