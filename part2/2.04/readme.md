```bash
❯ kubens
default
kube-node-lease
kube-public
kube-system
pingpong-log
todo
❯ kubectl get all
NAME                 TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)   AGE
service/kubernetes   ClusterIP   10.43.0.1    <none>        443/TCP   4m2s
❯ kubectl get all --all-namespaces
NAMESPACE      NAME                                          READY   STATUS      RESTARTS       AGE
kube-system    pod/coredns-7b98449c4-jq4kg                   1/1     Running     12 (17m ago)   5d11h
kube-system    pod/helm-install-traefik-crd-wb8v8            0/1     Completed   0              5d11h
kube-system    pod/local-path-provisioner-595dcfc56f-lcgtz   1/1     Running     13 (17m ago)   5d11h
kube-system    pod/metrics-server-cdcc87586-xwg4f            1/1     Running     15 (17m ago)   5d11h
kube-system    pod/svclb-traefik-44b4a939-hxthd              2/2     Running     24 (17m ago)   5d11h
kube-system    pod/svclb-traefik-44b4a939-nxzj6              2/2     Running     24 (17m ago)   5d11h
kube-system    pod/svclb-traefik-44b4a939-zm52k              2/2     Running     24 (18m ago)   5d11h
kube-system    pod/traefik-d7c9c5778-5zzgb                   1/1     Running     12 (17m ago)   5d11h
pingpong-log   pod/log-output-6d4b6dc778-fg4zz               2/2     Running     4 (17m ago)    39m
pingpong-log   pod/ping-pong-6ccc865f6d-gfqv2                1/1     Running     6 (17m ago)    41h
todo           pod/todo-app-6fc6696cc8-pjftn                 1/1     Running     0              97s
todo           pod/todo-backend-646c7f6dff-8vwhq             1/1     Running     0              53s

NAMESPACE      NAME                           TYPE           CLUSTER-IP      EXTERNA'L-IP                        PORT(S)                      AGE
default        service/kubernetes             ClusterIP      10.43.0.1       <none>                             443/TCP                      4m9s
kube-system    service/kube-dns               ClusterIP      10.43.0.10      <none>                             53/UDP,53/TCP,9153/TCP       5d11h
kube-system    service/metrics-server         ClusterIP      10.43.65.137    <none>                             443/TCP                      5d11h
kube-system    service/traefik                LoadBalancer   10.43.207.187   172.19.0.3,172.19.0.4,172.19.0.5   80:30827/TCP,443:30215/TCP   5d11h
pingpong-log   service/log-output-svc         ClusterIP      10.43.214.252   <none>                             3002/TCP,3001/TCP            41h
pingpong-log   service/pingpong-service       ClusterIP      10.43.61.1      <none>                             3000/TCP                     41h
todo           service/todo-app-service       ClusterIP      10.43.46.146    <none>                             5000/TCP                     91s
todo           service/todo-backend-service   ClusterIP      10.43.138.217   <none>                             5001/TCP                     48s

NAMESPACE     NAME                                    DESIRED   CURRENT   READY   UP-TO-DATE   AVAILABLE   NODE SELECTOR   AGE
kube-system   daemonset.apps/svclb-traefik-44b4a939   3         3         3       3            3           <none>          5d11h

NAMESPACE      NAME                                     READY   UP-TO-DATE   AVAILABLE   AGE
kube-system    deployment.apps/coredns                  1/1     1            1           5d11h
kube-system    deployment.apps/local-path-provisioner   1/1     1            1           5d11h
kube-system    deployment.apps/metrics-server           1/1     1            1           5d11h
kube-system    deployment.apps/traefik                  1/1     1            1           5d11h
pingpong-log   deployment.apps/log-output               1/1     1            1           41h
pingpong-log   deployment.apps/ping-pong                1/1     1            1           41h
todo           deployment.apps/todo-app                 1/1     1            1           97s
todo           deployment.apps/todo-backend             1/1     1            1           53s

NAMESPACE      NAME                                                DESIRED   CURRENT   READY   AGE
kube-system    replicaset.apps/coredns-7b98449c4                   1         1         1       5d11h
kube-system    replicaset.apps/local-path-provisioner-595dcfc56f   1         1         1       5d11h
kube-system    replicaset.apps/metrics-server-cdcc87586            1         1         1       5d11h
kube-system    replicaset.apps/traefik-d7c9c5778                   1         1         1       5d11h
pingpong-log   replicaset.apps/log-output-597b5fcd4c               0         0         0       3h41m
pingpong-log   replicaset.apps/log-output-68847f6cc6               0         0         0       41h
pingpong-log   replicaset.apps/log-output-6d4b6dc778               1         1         1       3h3m
pingpong-log   replicaset.apps/ping-pong-6ccc865f6d                1         1         1       41h
todo           replicaset.apps/todo-app-6fc6696cc8                 1         1         1       97s
todo           replicaset.apps/todo-backend-646c7f6dff             1         1         1       53s

NAMESPACE     NAME                                 STATUS     COMPLETIONS   DURATION   AGE
kube-system   job.batch/helm-install-traefik       Complete   1/1           32s        5d11h
kube-system   job.batch/helm-install-traefik-crd   Complete   1/1           19s        5d11h
❯ kubens todo
✔ Active namespace is "todo"
❯ kubectl get all
NAME                                READY   STATUS    RESTARTS   AGE
pod/todo-app-6fc6696cc8-pjftn       1/1     Running   0          2m12s
pod/todo-backend-646c7f6dff-8vwhq   1/1     Running   0          88s

NAME                           TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)    AGE
service/todo-app-service       ClusterIP   10.43.46.146    <none>        5000/TCP   2m6s
service/todo-backend-service   ClusterIP   10.43.138.217   <none>        5001/TCP   83s

NAME                           READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/todo-app       1/1     1            1           2m12s
deployment.apps/todo-backend   1/1     1            1           88s

NAME                                      DESIRED   CURRENT   READY   AGE
replicaset.apps/todo-app-6fc6696cc8       1         1         1       2m12s
replicaset.apps/todo-backend-646c7f6dff   1         1         1       88s

```