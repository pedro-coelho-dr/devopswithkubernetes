```bash
❯ kubectl get cronjobs -n todo

NAME           SCHEDULE    TIMEZONE   SUSPEND   ACTIVE   LAST SCHEDULE   AGE
todo-cronjob   0 * * * *   <none>     False     0        92s             26m



❯ kubectl get jobs -n todo

NAME                    STATUS     COMPLETIONS   DURATION   AGE
todo-cronjob-28907340   Complete   1/1           8s         107s


❯ kubectl get pods -n todo --selector app=todo-cronjob

NAME                          READY   STATUS      RESTARTS   AGE
todo-cronjob-28907340-47cls   0/1     Completed   0          118s



❯ kubectl logs -n todo todo-cronjob-28907340-47cls

Successfully added todo: Read https://en.wikipedia.org/wiki/2019_President%27s_Cup_(tennis)_%E2%80%93_Women%27s_singles


❯ curl http://localhost:8081/todos
[{"content":"teste","id":1},{"content":"teste2","id":2},{"content":"Test Todo","id":3},{"content":"920834123048213904812903-4812-309481230-94812-0384-0219384-0921384-091238490-21384-09218340-9281309-481230-948210-9384-90213840912384023814-","id":4},{"content":"920834123048213904812903-4812-309481230-94812-0384-0219384-0921384-091238490-21384-09218340-9281309-481230-948210-9384-902138409123840238142","id":5},{"content":"teste","id":6},{"content":"teste","id":7},{"content":"a","id":8},{"content":"teste 7","id":9},{"content":"Read https://en.wikipedia.org/wiki/2019_President%27s_Cup_(tennis)_%E2%80%93_Women%27s_singles","id":10}]
```
