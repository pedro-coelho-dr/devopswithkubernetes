```bash


❯ kubectl get all -n pingpong-log
kubectl get pods -n pingpong-log
kubectl get svc -n pingpong-log
kubectl get ingress -n pingpong-log

NAME                             READY   STATUS    RESTARTS   AGE
pod/ping-pong-76b597f4f7-4xm9f   1/1     Running   0          20m
pod/postgres-stset-0             1/1     Running   0          4h24m

NAME                       TYPE           CLUSTER-IP      EXTERNAL-IP     PORT(S)          AGE
service/pingpong-service   LoadBalancer   34.118.238.29   34.88.219.234   3000:32420/TCP   4h23m
service/postgres-service   ClusterIP      None            <none>          5432/TCP         4h23m

NAME                        READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/ping-pong   1/1     1            1           4h23m

NAME                                   DESIRED   CURRENT   READY   AGE
replicaset.apps/ping-pong-57949794dd   0         0         0       23m
replicaset.apps/ping-pong-76b597f4f7   1         1         1       20m
replicaset.apps/ping-pong-76f48c88d7   0         0         0       4h23m
replicaset.apps/ping-pong-d69bbc67d    0         0         0       4h12m

NAME                              READY   AGE
statefulset.apps/postgres-stset   1/1     4h24m
NAME                         READY   STATUS    RESTARTS   AGE
ping-pong-76b597f4f7-4xm9f   1/1     Running   0          20m
postgres-stset-0             1/1     Running   0          4h24m
NAME               TYPE           CLUSTER-IP      EXTERNAL-IP     PORT(S)          AGE
pingpong-service   LoadBalancer   34.118.238.29   34.88.219.234   3000:32420/TCP   4h23m
postgres-service   ClusterIP      None            <none>          5432/TCP         4h23m
NAME               CLASS     HOSTS   ADDRESS   PORTS   AGE
pingpong-ingress   traefik   *                 80      4h22m

❯ curl http://34.88.219.234:3000/getpong
{"count":1}

❯ curl http://34.88.219.234:3000/pingpong
{"response":"pong 2"}

❯ curl http://34.88.219.234:3000/getpong
{"count":2}




```


```bash
❯ gcloud container clusters list
gcloud container clusters describe dwk-cluster --zone=europe-north1-b
kubectl get nodes

NAME         LOCATION         MASTER_VERSION       MASTER_IP      MACHINE_TYPE  NODE_VERSION         NUM_NODES  STATUS
dwk-cluster  europe-north1-b  1.29.10-gke.1054000  35.228.142.90  e2-micro      1.29.10-gke.1054000  3          RUNNING
addonsConfig:
  gcePersistentDiskCsiDriverConfig:
    enabled: true
  kubernetesDashboard:
    disabled: true
  networkPolicyConfig:
    disabled: true
autopilot: {}
autoscaling:
  autoscalingProfile: BALANCED
clusterIpv4Cidr: 10.16.0.0/14
controlPlaneEndpointsConfig:
  dnsEndpointConfig:
    allowExternalTraffic: false
    endpoint: gke-138671ff62c848d4abcabb859201310deee9-490889871398.europe-north1-b.gke.goog
  ipEndpointsConfig:
    authorizedNetworksConfig:
      gcpPublicCidrsAccessEnabled: true
    enablePublicEndpoint: true
    enabled: true
    privateEndpoint: 10.166.0.2
    publicEndpoint: 35.228.142.90
createTime: '2024-12-22T14:11:59+00:00'
currentMasterVersion: 1.29.10-gke.1054000
currentNodeCount: 3
currentNodeVersion: 1.29.10-gke.1054000
databaseEncryption:
  currentState: CURRENT_STATE_DECRYPTED
  state: DECRYPTED
defaultMaxPodsConstraint:
  maxPodsPerNode: '110'
endpoint: 35.228.142.90
enterpriseConfig:
  clusterTier: STANDARD
etag: 6c3b6dfc-3963-4b90-8c73-9861cb9ef6d3
id: 138671ff62c848d4abcabb859201310deee9b157d9744dbe83c1d9cf5b1a4373
initialClusterVersion: 1.29.10-gke.1054000
instanceGroupUrls:
- https://www.googleapis.com/compute/v1/projects/dwk-gke-445103/zones/europe-north1-b/instanceGroupManagers/gke-dwk-cluster-default-pool-417013e7-grp
ipAllocationPolicy:
  clusterIpv4Cidr: 10.16.0.0/14
  clusterIpv4CidrBlock: 10.16.0.0/14
  clusterSecondaryRangeName: gke-dwk-cluster-pods-138671ff
  defaultPodIpv4RangeUtilization: 0.0029
  podCidrOverprovisionConfig: {}
  servicesIpv4Cidr: 34.118.224.0/20
  servicesIpv4CidrBlock: 34.118.224.0/20
  stackType: IPV4
  useIpAliases: true
labelFingerprint: a9dc16a7
legacyAbac: {}
location: europe-north1-b
locations:
- europe-north1-b
loggingConfig:
  componentConfig:
    enableComponents:
    - SYSTEM_COMPONENTS
    - WORKLOADS
loggingService: logging.googleapis.com/kubernetes
maintenancePolicy:
  resourceVersion: e3b0c442
masterAuth:
  clientCertificateConfig: {}
  clusterCaCertificate: LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tCk1JSUVMRENDQXBTZ0F3SUJBZ0lRYzhzMzliRFJnY29wNTlPT3orbFJtREFOQmdrcWhraUc5dzBCQVFzRkFEQXYKTVMwd0t3WURWUVFERXlReU1tVmhOVGszWWkxbVpUSXhMVFEzTnpVdFltUXdOaTB5T1RWa1pUUmlOMkV6WkRFdwpJQmNOTWpReE1qSXlNVE14TWpBd1doZ1BNakExTkRFeU1UVXhOREV5TURCYU1DOHhMVEFyQmdOVkJBTVRKREl5ClpXRTFPVGRpTFdabE1qRXRORGMzTlMxaVpEQTJMVEk1TldSbE5HSTNZVE5rTVRDQ0FhSXdEUVlKS29aSWh2Y04KQVFFQkJRQURnZ0dQQURDQ0FZb0NnZ0dCQUtoV2N0UkRSUjZBVEJQOGFTS3QyY1Aybk12ZDNVSzdjR2Rzc2xUWQoyZnJScys3SDh2Nnl4WUhGc1hyTEZNMUVYeFF5T1BwQ0JhclJMRjFpSytMRGZ4bEhLcnMvK0NmelJ0SmhlcFgrCkNVK3FMTUpnTlRRbzZ1clpXTHpiNE1oaDkwaXdzaDRUeUpMUlk5enBDbXdDaTByQjE5YmdyMDIvdGdKRVowMUUKa0RMd2tEVHpvMW56Si9LdjRZWWpydUhURGRsYW1USHYxNXlTWjNOMDUzekpHdVowcmZrQkNXQ0Y1WW5qdXg2ZQo5UTE3N2NxbWNFWEN0Zk1vUWloV0lybFRkM2ZGMFF2MGthOXBnWnVna3ZZYkt3V1pSS3ZNSi9RcW1NWUk1dGIrCk96dEtzcjZPTnFnTEM4NjJtUU1xd0RjcXQ4Mjk1WXJSSFpTU0NVYWEwOHRlSzZCeXgxdlVqdFdaMmppa2grWkgKRTNGbzhRbTF0Y2ZzcWxacEpJbFJKZ1RSNkdxbHNSSlhYTmxMa0VLdVd2cEFtK0pyL3AxSmt2WGlLQ1ZBR25EbAp0ZWNEajBGN01Jd1dCZEJjeDJZN1ZaMC9zVmsvalc2KzVaR0NWbVBsNGVOVlpLaTV1U3d3eXdSY1U5TmNUVkdkCjVNV1VRckhQZkJaTS9YcXZDbVJEN016enhRSURBUUFCbzBJd1FEQU9CZ05WSFE4QkFmOEVCQU1DQWdRd0R3WUQKVlIwVEFRSC9CQVV3QXdFQi96QWRCZ05WSFE0RUZnUVVNMVI3dWNSS2pqeHdXTWt6dU5zSE04Mm5Za3N3RFFZSgpLb1pJaHZjTkFRRUxCUUFEZ2dHQkFENWh5cXJreWJBQ01HbkR0MUJ0SU5YUEtscXlOL0w2WVRTMFhLSVVRVWZVCktTTVJORTNETk9vRW5lK2ZxVDdIczJRQjZnUkFLWlJWc2hvR1RXc3V3cUpwN1JjcVRHZnBSU3dldFRGSWNhUDEKVHFsUTJqVkJ2dVlXanBIM0UwTlBOeitvcWRPSGZXSURLeGxiK0VKaDlzdzhZM2tNQUZQRE9VelNzdVZzdVdQUgpjWHppSCtXVDZud1ZHOUVxdldpMkowWnpuM1JHQVg5UFA2Vk5yMU5qNGpXcmw3UnVEOW9oWU8rVnNTclptaUZWCnlQSVZIUU9xYXA5amlOYWU5SlNUTkhFVXpqbWlkc0hZZEx2MmhnR050ZEsxb3BEcWh0VjNVdkNiTmNYcGpBRHMKNW9VVWNkZUN2NDd6cWRnNGQrbFhOSFk5YkVHNGNxNHZCS0NSbVNVZThHVXVzN1cyT2MzRnppS2NVbHpFU2wrMwpiakJ2L2dGelJlNUpjWVJxV1ZaOC9HTWRMR0lkZllnSVpEYktnTDJmbVY3UGlBL3ArYWNTRTFKVVE1Y29Ydm1ZClVYQlRLbHVsdUZBdjNzbFhYTWl3RVVzRDRXSGlvMHVuSy9LaGJNSjl6MGNKSEtkRTl6ZUlOQ1BCR2E5RGlOZ3IKUFR5Mi9sQno3dTBveTc1VTA2QldEdz09Ci0tLS0tRU5EIENFUlRJRklDQVRFLS0tLS0K
masterAuthorizedNetworksConfig:
  gcpPublicCidrsAccessEnabled: true
monitoringConfig:
  advancedDatapathObservabilityConfig: {}
  componentConfig:
    enableComponents:
    - SYSTEM_COMPONENTS
    - DAEMONSET
    - DEPLOYMENT
    - STATEFULSET
    - STORAGE
    - HPA
    - POD
    - KUBELET
    - CADVISOR
  managedPrometheusConfig:
    enabled: true
monitoringService: monitoring.googleapis.com/kubernetes
name: dwk-cluster
network: default
networkConfig:
  network: projects/dwk-gke-445103/global/networks/default
  serviceExternalIpsConfig: {}
  subnetwork: projects/dwk-gke-445103/regions/europe-north1/subnetworks/default
nodeConfig:
  diskSizeGb: 32
  diskType: pd-balanced
  effectiveCgroupMode: EFFECTIVE_CGROUP_MODE_V2
  imageType: COS_CONTAINERD
  kubeletConfig:
    insecureKubeletReadonlyPortEnabled: true
  machineType: e2-micro
  metadata:
    disable-legacy-endpoints: 'true'
  oauthScopes:
  - https://www.googleapis.com/auth/devstorage.read_only
  - https://www.googleapis.com/auth/logging.write
  - https://www.googleapis.com/auth/monitoring
  - https://www.googleapis.com/auth/service.management.readonly
  - https://www.googleapis.com/auth/servicecontrol
  - https://www.googleapis.com/auth/trace.append
  serviceAccount: default
  shieldedInstanceConfig:
    enableIntegrityMonitoring: true
  windowsNodeConfig: {}
nodePoolDefaults:
  nodeConfigDefaults:
    loggingConfig:
      variantConfig:
        variant: DEFAULT
nodePools:
- autoscaling: {}
  config:
    diskSizeGb: 32
    diskType: pd-balanced
    effectiveCgroupMode: EFFECTIVE_CGROUP_MODE_V2
    imageType: COS_CONTAINERD
    kubeletConfig:
      insecureKubeletReadonlyPortEnabled: true
    machineType: e2-micro
    metadata:
      disable-legacy-endpoints: 'true'
    oauthScopes:
    - https://www.googleapis.com/auth/devstorage.read_only
    - https://www.googleapis.com/auth/logging.write
    - https://www.googleapis.com/auth/monitoring
    - https://www.googleapis.com/auth/service.management.readonly
    - https://www.googleapis.com/auth/servicecontrol
    - https://www.googleapis.com/auth/trace.append
    serviceAccount: default
    shieldedInstanceConfig:
      enableIntegrityMonitoring: true
    windowsNodeConfig: {}
  etag: cb151821-ae6c-4955-b16c-9b50a74860e5
  initialNodeCount: 3
  instanceGroupUrls:
  - https://www.googleapis.com/compute/v1/projects/dwk-gke-445103/zones/europe-north1-b/instanceGroupManagers/gke-dwk-cluster-default-pool-417013e7-grp
  locations:
  - europe-north1-b
  management:
    autoRepair: true
    autoUpgrade: true
  maxPodsConstraint:
    maxPodsPerNode: '110'
  name: default-pool
  networkConfig:
    podIpv4CidrBlock: 10.16.0.0/14
    podIpv4RangeUtilization: 0.0029
    podRange: gke-dwk-cluster-pods-138671ff
  podIpv4CidrSize: 24
  selfLink: https://container.googleapis.com/v1/projects/dwk-gke-445103/zones/europe-north1-b/clusters/dwk-cluster/nodePools/default-pool
  status: RUNNING
  upgradeSettings:
    maxSurge: 1
    strategy: SURGE
  version: 1.29.10-gke.1054000
notificationConfig:
  pubsub: {}
privateClusterConfig:
  privateEndpoint: 10.166.0.2
  publicEndpoint: 35.228.142.90
rbacBindingConfig:
  enableInsecureBindingSystemAuthenticated: true
  enableInsecureBindingSystemUnauthenticated: true
releaseChannel:
  channel: STABLE
satisfiesPzi: true
satisfiesPzs: false
securityPostureConfig:
  mode: BASIC
  vulnerabilityMode: VULNERABILITY_MODE_UNSPECIFIED
selfLink: https://container.googleapis.com/v1/projects/dwk-gke-445103/zones/europe-north1-b/clusters/dwk-cluster
servicesIpv4Cidr: 34.118.224.0/20
shieldedNodes:
  enabled: true
status: RUNNING
subnetwork: default
zone: europe-north1-b
NAME                                         STATUS   ROLES    AGE     VERSION
gke-dwk-cluster-default-pool-417013e7-4s01   Ready    <none>   5h37m   v1.29.10-gke.1054000
gke-dwk-cluster-default-pool-417013e7-mv57   Ready    <none>   5h37m   v1.29.10-gke.1054000
gke-dwk-cluster-default-pool-417013e7-tj3g   Ready    <none>   5h37m   v1.29.10-gke.1054000

```