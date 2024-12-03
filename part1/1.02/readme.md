```bash
docker run -e PORT=8080 -p 8080:8080 todo-app
```

```bash
kubectl get deployments
kubectl get pods

NAME         READY   UP-TO-DATE   AVAILABLE   AGE
log-output   1/1     1            1           169m
todo-app     1/1     1            1           3m9s
NAME                          READY   STATUS    RESTARTS   AGE
log-output-689484f579-dd2wv   1/1     Running   0          166m
todo-app-f58cd6f98-fbcpc      1/1     Running   0          2m35s
❯ kubectl logs todo-app-f58cd6f98-fbcpc
Server started in port 8080
 * Serving Flask app 'app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:8080
 * Running on http://10.42.2.10:8080
Press CTRL+C to quit
```