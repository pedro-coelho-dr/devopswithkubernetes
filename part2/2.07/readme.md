```bash
❯ kubectl get all --show-labels -n pingpong-log

NAME                              READY   STATUS    RESTARTS      AGE     LABELS
pod/log-output-85d67fb69b-xq2vs   2/2     Running   6 (10m ago)   23h     app=log-output,pod-template-hash=85d67fb69b
pod/ping-pong-6ccc865f6d-gfqv2    1/1     Running   9 (10m ago)   2d18h   app=ping-pong,pod-template-hash=6ccc865f6d
pod/postgres-stset-0              1/1     Running   0             13m     app=postgres,apps.kubernetes.io/pod-index=0,controller-revision-hash=postgres-stset-7cdcfcd65c,statefulset.kubernetes.io/pod-name=postgres-stset-0

NAME                       TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)             AGE     LABELS
service/log-output-svc     ClusterIP   10.43.214.252   <none>        3002/TCP,3001/TCP   2d18h   app=log-output
service/pingpong-service   ClusterIP   10.43.61.1      <none>        3000/TCP            2d18h   app=ping-pong
service/postgres-service   ClusterIP   None            <none>        5432/TCP            13m     app=postgres

NAME                         READY   UP-TO-DATE   AVAILABLE   AGE     LABELS
deployment.apps/log-output   1/1     1            1           2d18h   app=log-output
deployment.apps/ping-pong    1/1     1            1           2d18h   app=ping-pong

NAME                                    DESIRED   CURRENT   READY   AGE     LABELS
replicaset.apps/log-output-55f4ff88b7   0         0         0       23h     app=log-output,pod-template-hash=55f4ff88b7
replicaset.apps/log-output-597b5fcd4c   0         0         0       28h     app=log-output,pod-template-hash=597b5fcd4c
replicaset.apps/log-output-68847f6cc6   0         0         0       2d18h   app=log-output,pod-template-hash=68847f6cc6
replicaset.apps/log-output-69554c6fb6   0         0         0       23h     app=log-output,pod-template-hash=69554c6fb6
replicaset.apps/log-output-6d4b6dc778   0         0         0       28h     app=log-output,pod-template-hash=6d4b6dc778
replicaset.apps/log-output-7f47cf4597   0         0         0       23h     app=log-output,pod-template-hash=7f47cf4597
replicaset.apps/log-output-85d67fb69b   1         1         1       23h     app=log-output,pod-template-hash=85d67fb69b
replicaset.apps/ping-pong-6ccc865f6d    1         1         1       2d18h   app=ping-pong,pod-template-hash=6ccc865f6d

NAME                              READY   AGE     LABELS
statefulset.apps/postgres-stset   1/1     3m18s   app=postgres





```



```bash
❯ kubectl describe pod -n pingpong-log postgres-stset-0
kubectl logs -n pingpong-log postgres-stset-0
Name:             postgres-stset-0
Namespace:        pingpong-log
Priority:         0
Service Account:  default
Node:             k3d-my-cluster-agent-1/172.19.0.3
Start Time:       Mon, 16 Dec 2024 15:23:10 -0300
Labels:           app=postgres
                  apps.kubernetes.io/pod-index=0
                  controller-revision-hash=postgres-stset-7cdcfcd65c
                  statefulset.kubernetes.io/pod-name=postgres-stset-0
Annotations:      <none>
Status:           Running
IP:               10.42.1.93
IPs:
  IP:           10.42.1.93
Controlled By:  StatefulSet/postgres-stset
Containers:
  postgres:
    Container ID:   containerd://504a9ab4fac3f6617fc4d0d722201fb8ebd753b7fa3f6d6e951bee86af8f63b6
    Image:          postgres:17.2
    Image ID:       docker.io/library/postgres@sha256:fe4efc6901dda0d952306fd962643d8022d7bb773ffe13fe8a21551b9276e50c
    Port:           5432/TCP
    Host Port:      0/TCP
    State:          Running
      Started:      Mon, 16 Dec 2024 15:26:21 -0300
    Ready:          True
    Restart Count:  0
    Environment:
      POSTGRES_USER:      <set to the key 'POSTGRES_USER' in secret 'postgres-secret'>      Optional: false
      POSTGRES_PASSWORD:  <set to the key 'POSTGRES_PASSWORD' in secret 'postgres-secret'>  Optional: false
      POSTGRES_DB:        <set to the key 'POSTGRES_DB' in secret 'postgres-secret'>        Optional: false
    Mounts:
      /var/lib/postgresql/data from postgres-data (rw,path="postgres")
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-qclr4 (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   True 
  Initialized                 True 
  Ready                       True 
  ContainersReady             True 
  PodScheduled                True 
Volumes:
  postgres-data:
    Type:       PersistentVolumeClaim (a reference to a PersistentVolumeClaim in the same namespace)
    ClaimName:  postgres-data-postgres-stset-0
    ReadOnly:   false
  kube-api-access-qclr4:
    Type:                    Projected (a volume that contains injected data from multiple sources)
    TokenExpirationSeconds:  3607
    ConfigMapName:           kube-root-ca.crt
    ConfigMapOptional:       <nil>
    DownwardAPI:             true
QoS Class:                   BestEffort
Node-Selectors:              <none>
Tolerations:                 node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
                             node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
Events:
  Type    Reason          Age   From               Message
  ----    ------          ----  ----               -------
  Normal  Scheduled       14m   default-scheduler  Successfully assigned pingpong-log/postgres-stset-0 to k3d-my-cluster-agent-1
  Normal  Pulling         14m   kubelet            Pulling image "postgres:17.2"
  Normal  SandboxChanged  11m   kubelet            Pod sandbox changed, it will be killed and re-created.
  Normal  Pulling         11m   kubelet            Pulling image "postgres:17.2"
  Normal  Pulled          11m   kubelet            Successfully pulled image "postgres:17.2" in 8.175s (8.175s including waiting). Image size: 153816116 bytes.
  Normal  Created         11m   kubelet            Created container postgres
  Normal  Started         11m   kubelet            Started container postgres
The files belonging to this database system will be owned by user "postgres".
This user must also own the server process.

The database cluster will be initialized with locale "en_US.utf8".
The default database encoding has accordingly been set to "UTF8".
The default text search configuration will be set to "english".

Data page checksums are disabled.

fixing permissions on existing directory /var/lib/postgresql/data ... ok
creating subdirectories ... ok
selecting dynamic shared memory implementation ... posix
selecting default "max_connections" ... 100
selecting default "shared_buffers" ... 128MB
selecting default time zone ... Etc/UTC
creating configuration files ... ok
running bootstrap script ... ok
performing post-bootstrap initialization ... ok
initdb: warning: enabling "trust" authentication for local connections
initdb: hint: You can change this by editing pg_hba.conf or using the option -A, or --auth-local and --auth-host, the next time you run initdb.
syncing data to disk ... ok


Success. You can now start the database server using:

    pg_ctl -D /var/lib/postgresql/data -l logfile start

waiting for server to start....2024-12-16 18:26:23.457 UTC [49] LOG:  starting PostgreSQL 17.2 (Debian 17.2-1.pgdg120+1) on x86_64-pc-linux-gnu, compiled by gcc (Debian 12.2.0-14) 12.2.0, 64-bit
2024-12-16 18:26:23.461 UTC [49] LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
2024-12-16 18:26:23.471 UTC [52] LOG:  database system was shut down at 2024-12-16 18:26:22 UTC
2024-12-16 18:26:23.477 UTC [49] LOG:  database system is ready to accept connections
 done
server started
CREATE DATABASE


/usr/local/bin/docker-entrypoint.sh: ignoring /docker-entrypoint-initdb.d/*

waiting for server to shut down....2024-12-16 18:26:23.649 UTC [49] LOG:  received fast shutdown request
2024-12-16 18:26:23.653 UTC [49] LOG:  aborting any active transactions
2024-12-16 18:26:23.654 UTC [49] LOG:  background worker "logical replication launcher" (PID 55) exited with exit code 1
2024-12-16 18:26:23.654 UTC [50] LOG:  shutting down
2024-12-16 18:26:23.657 UTC [50] LOG:  checkpoint starting: shutdown immediate
2024-12-16 18:26:23.995 UTC [50] LOG:  checkpoint complete: wrote 921 buffers (5.6%); 0 WAL file(s) added, 0 removed, 0 recycled; write=0.014 s, sync=0.312 s, total=0.342 s; sync files=301, longest=0.004 s, average=0.002 s; distance=4238 kB, estimate=4238 kB; lsn=0/1908978, redo lsn=0/1908978
2024-12-16 18:26:23.999 UTC [49] LOG:  database system is shut down
 done
server stopped

PostgreSQL init process complete; ready for start up.

2024-12-16 18:26:24.070 UTC [1] LOG:  starting PostgreSQL 17.2 (Debian 17.2-1.pgdg120+1) on x86_64-pc-linux-gnu, compiled by gcc (Debian 12.2.0-14) 12.2.0, 64-bit
2024-12-16 18:26:24.071 UTC [1] LOG:  listening on IPv4 address "0.0.0.0", port 5432
2024-12-16 18:26:24.071 UTC [1] LOG:  listening on IPv6 address "::", port 5432
2024-12-16 18:26:24.077 UTC [1] LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
2024-12-16 18:26:24.085 UTC [65] LOG:  database system was shut down at 2024-12-16 18:26:23 UTC
2024-12-16 18:26:24.090 UTC [1] LOG:  database system is ready to accept connections
2024-12-16 18:31:24.595 UTC [63] LOG:  checkpoint starting: time
2024-12-16 18:31:29.079 UTC [63] LOG:  checkpoint complete: wrote 47 buffers (0.3%); 0 WAL file(s) added, 0 removed, 0 recycled; write=4.449 s, sync=0.017 s, total=4.485 s; sync files=12, longest=0.005 s, average=0.002 s; distance=269 kB, estimate=269 kB; lsn=0/194C0C8, redo lsn=0/194C070
```



```bash

❯ kubectl run -it --rm --restart=Never --image postgres:17.2 psql-debug -- sh

If you don't see a command prompt, try pressing enter.

# psql -h postgres-service.pingpong-log.svc.cluster.local -U XXXX pingpong-log-db
Password for user xxxxx:
psql (17.2 (Debian 17.2-1.pgdg120+1))
Type "help" for help.

pingpong-log-db=# \d
Did not find any relations.
pingpong-log-db=# CREATE TABLE test_table (id SERIAL PRIMARY KEY, message TEXT);
CREATE TABLE
pingpong-log-db=# INSERT INTO test_table (message) VALUES ('Hello, PostgreSQL!');
INSERT 0 1
pingpong-log-db=# SELECT * FROM test_table;
 id |      message       
----+--------------------
  1 | Hello, PostgreSQL!
(1 row)

```



```bash

❯ curl -X GET http://localhost:8081/pingpong

{"response":"pong 8"}
❯ curl -X GET http://localhost:8081/getpong

{"count":8}
❯ curl -X GET http://localhost:8081/log

{"env variable":"MESSAGE=hello world","file content":"this text is from file","hash":"8423e94cbea21a5b321466a75c751e78aa98417ac24aa222e2412e89b3bf06dc","ping_pongs":8,"status":"verified","timestamp":"2024-12-16T19:09:47.300250+00:00"}
❯ kubectl exec -it postgres-stset-0 -n pingpong-log -- bash

root@postgres-stset-0:/# psql -U admin -d pingpong-log-db
psql (17.2 (Debian 17.2-1.pgdg120+1))
Type "help" for help.

pingpong-log-db=# \dt
          List of relations
 Schema |    Name    | Type  | Owner 
--------+------------+-------+-------
 public | counter    | table | admin
 public | test_table | table | admin
(2 rows)

pingpong-log-db=# SELECT * FROM counter;
 id | count 
----+-------
  1 |     8
(1 row)

```
