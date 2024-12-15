```bash
❯ kubectl get configmap log-output-configmap -n pingpong-log -o yaml

apiVersion: v1
data:
  MESSAGE: hello world
  information.txt: |
    this text is from file
kind: ConfigMap
metadata:
  annotations:
    kubectl.kubernetes.io/last-applied-configuration: |
      {"apiVersion":"v1","data":{"MESSAGE":"hello world","information.txt":"this text is from file\n"},"kind":"ConfigMap","metadata":{"annotations":{},"name":"log-output-configmap","namespace":"pingpong-log"}}
  creationTimestamp: "2024-12-15T18:48:11Z"
  name: log-output-configmap
  namespace: pingpong-log
  resourceVersion: "35513"
  uid: c0b04225-78c9-4652-901b-0f2a195e1cee
❯ kubectl get pods -n pingpong-log --show-labels

NAME                          READY   STATUS    RESTARTS       AGE     LABELS
log-output-85d67fb69b-xq2vs   2/2     Running   0              5m20s   app=log-output,pod-template-hash=85d67fb69b
ping-pong-6ccc865f6d-gfqv2    1/1     Running   6 (119m ago)   43h     app=ping-pong,pod-template-hash=6ccc865f6d
❯ curl http://localhost:8081/log

{"env variable":"MESSAGE=hello world","file content":"this text is from file","hash":"50d474ef28d3bad52ab8e3c55130dcd2ba6a725b95e98c23bfc2dcdff33b2904","ping_pongs":17,"status":"verified","timestamp":"2024-12-15T19:21:28.610544+00:00"}
❯ curl http://localhost:8081/pingpong
curl http://localhost:8081/getpong

{"response":"pong 18"}
{"count":18}

❯ curl http://localhost:8081/log
{"env variable":"MESSAGE=hello world","file content":"this text is from file","hash":"c9b5c8ecdc4bf700fb8d568201a621c089c81cc46c63d755389a3785b46f902b","ping_pongs":18,"status":"verified","timestamp":"2024-12-15T19:21:58.508650+00:00"}

```


