```bash
❯ kubectl apply -f manifests/deployment.yaml

deployment.apps/log-output created
❯ kubectl get pods

NAME                         READY   STATUS    RESTARTS   AGE
log-output-b86c9c469-pwncz   1/1     Running   0          11s
todo-app-844c9d7d45-6cfzz    1/1     Running   0          17m



```