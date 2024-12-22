# DevOps with Kubernetes
This course is an introductory course to Kubernetes with K3s and GKE.

University of Helsinki

https://devopswithkubernetes.com/



```bash
gcloud container clusters create dwk-cluster --zone=europe-north1-b --cluster-version=1.29 --disk-size=32 --num-nodes=3 --machine-type=e2-micro

gcloud services enable container.googleapis.com

gcloud container clusters create dwk-cluster --zone=europe-north1-b --cluster-version=1.29

gcloud container clusters get-credentials dwk-cluster --zone=europe-north1-b

kubectl apply -f https://raw.githubusercontent.com/kubernetes-hy/material-example/e11a700350aede132b62d3b5fd63c05d6b976394/app6/manifests/deployment.yaml

kubectl cluster-info

kubectl get svc --watch

gcloud container clusters delete dwk-cluster --zone=europe-north1-b

gcloud container clusters create dwk-cluster --zone=europe-north1-b --cluster-version=1.29

```