```bash
❯ kubectl apply -f manifests/deployment.yaml
deployment.apps/todo-app configured


❯ kubectl get pods

NAME                                 READY   STATUS        RESTARTS      AGE
hashgenerator-dep-7c5cfb9744-mvc2m   1/1     Running       0             4d12h
hashresponse-dep-755b5b5dd7-cjkkd    1/1     Running       0             58m
log-output-b86c9c469-mg694           1/1     Running       2 (62m ago)   4d14h
todo-app-84486c5868-lt48c            1/1     Terminating   0             4d12h
todo-app-844c9d7d45-b6b8x            1/1     Running       0             18s

❯ kubectl port-forward deployment/todo-app 8081:5000

Forwarding from 127.0.0.1:8081 -> 5000
Forwarding from [::1]:8081 -> 5000
Handling connection for 8081
Handling connection for 8081
Handling connection for 8081
```