# DevOps with Kubernetes
This course is an introductory course to Kubernetes with K3s and GKE.

University of Helsinki

https://devopswithkubernetes.com/



```bash
k3d cluster start my-cluster


kubectl apply -f manifests/deployment.yaml 


kubectl get deployments


kubectl get pods


kubectl logs -l app=log-output
kubectl logs -l app=todo-app



k3d cluster stop my-cluster


k3d cluster delete my-cluster

k3d cluster create my-cluster --port 8082:30080@agent:0 -p 8081:80@loadbalancer --agents 2
```