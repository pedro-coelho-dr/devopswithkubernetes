# DevOps with Kubernetes
This course is an introductory course to Kubernetes with K3s and GKE.

University of Helsinki

https://devopswithkubernetes.com/




k3d cluster start my-cluster


kubectl apply -f manifests/log-output/deployment.yaml
kubectl apply -f manifests/todo-app/deployment.yaml


kubectl get deployments


kubectl get pods


kubectl logs -l app=log-output
kubectl logs -l app=todo-app
