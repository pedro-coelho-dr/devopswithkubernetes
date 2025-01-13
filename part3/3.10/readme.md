❯ kubectl get namespaces
NAME                 STATUS   AGE
default              Active   65m
gke-managed-system   Active   64m
gmp-public           Active   64m
gmp-system           Active   64m
kube-node-lease      Active   65m
kube-public          Active   65m
kube-system          Active   65m
monitoring           Active   65s
pingpong-log         Active   38m
todo-main            Active   62m
❯ kubectl get pods -n monitoring

NAME                                                     READY   STATUS    RESTARTS   AGE
alertmanager-prometheus-kube-prometheus-alertmanager-0   2/2     Running   0          38s
prometheus-grafana-599f549cd4-hqkd4                      3/3     Running   0          46s
prometheus-kube-prometheus-operator-6f5db974db-mkcc2     1/1     Running   0          46s
prometheus-kube-state-metrics-cb98bff75-vcx6j            1/1     Running   0          46s
prometheus-prometheus-kube-prometheus-prometheus-0       2/2     Running   0          37s
prometheus-prometheus-node-exporter-8n56f                1/1     Running   0          47s
prometheus-prometheus-node-exporter-hjvl5                1/1     Running   0          46s
prometheus-prometheus-node-exporter-hz5tp                1/1     Running   0          46s
prometheus-prometheus-node-exporter-k5mkl                1/1     Running   0          46s