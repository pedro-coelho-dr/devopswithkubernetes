```bash
❯ kubectl create namespace pingpong-log


❯ kubens

default
kube-node-lease
kube-public
kube-system
pingpong-log

❯ kubens pingpong-log

✔ Active namespace is "pingpong-log"

❯ kubectl get all -n pingpong-log

NAME                              READY   STATUS    RESTARTS   AGE
pod/log-output-68847f6cc6-c67pg   2/2     Running   0          3m5s
pod/ping-pong-6ccc865f6d-gfqv2    1/1     Running   0          2m51s

NAME                       TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)             AGE
service/log-output-svc     ClusterIP   10.43.214.252   <none>        2345/TCP,2346/TCP   3m5s
service/pingpong-service   ClusterIP   10.43.61.1      <none>        2345/TCP            2m51s

NAME                         READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/log-output   1/1     1            1           3m5s
deployment.apps/ping-pong    1/1     1            1           2m51s

NAME                                    DESIRED   CURRENT   READY   AGE
replicaset.apps/log-output-68847f6cc6   1         1         1       3m5s
replicaset.apps/ping-pong-6ccc865f6d    1         1         1       2m51s

❯ kubectl get pods
NAME                          READY   STATUS    RESTARTS   AGE
log-output-68847f6cc6-c67pg   2/2     Running   0          3m25s
ping-pong-6ccc865f6d-gfqv2    1/1     Running   0          3m11s

❯ kubectx

k3d-k3s-default
k3d-my-cluster

```


