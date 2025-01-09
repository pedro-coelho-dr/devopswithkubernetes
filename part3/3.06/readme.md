# Exercise 3.06: DBaaS vs DIY



## 1 - DBaaS (Google Cloud SQL)

| **Pros**                                             | **Cons**                                               |
|------------------------------------------------------|-------------------------------------------------------|
| Easy setup with minimal configuration.              | Higher cost compared to DIY solutions.                |
| Managed maintenance, updates, and monitoring.       | Limited control over database internals and configuration. |
| Built-in backup solutions and high reliability.     |                                                       |
| Simplifies scaling and integration with Google Cloud services. |                                                       |
| Security features like IAM and encryption are pre-configured. |                                                       |



## 2- DIY with PVCs (Postgres in Kubernetes)

| **Pros**                                             | **Cons**                                               |
|------------------------------------------------------|-------------------------------------------------------|
| Full control over database configuration and tuning. | Requires significant effort for setup and maintenance. |
| Lower direct costs, paying only for compute and storage. | Complex backup and restore processes.                 |
| Flexibility to use custom Postgres versions or extensions. | Scaling and ensuring high availability demand additional work. |
|                                                      | Higher risk of misconfigurations affecting reliability or security. |



## 3 - Comparison

| **Aspect**         | **DBaaS (Google Cloud SQL)**                                                                 | **DIY (Postgres with PVCs)**                                                              |
|---------------------|---------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|
| **Setup Complexity** | Minimal: Simple setup through a managed service with UI or CLI.                            | Medium to High: Requires manual setup of Postgres, PVCs, and Kubernetes configurations.  |
| **Maintenance**     | Low: Google handles updates, scaling, and monitoring.                                       | High: You manage updates, scaling, and database health manually.                         |
| **Cost**            | High: Higher cost for convenience and reliability.                                          | Lower: Pay for compute and storage, but operational work adds indirect costs.           |
| **Reliability**     | High: Built-in redundancy and SLAs ensure high reliability.                                 | Medium: Requires manual configuration for high availability and recovery.               |
| **Backups**         | Easy: Automated and on-demand backups available with minimal effort.                        | Complex: You must configure and manage your own backup system securely.                  |
| **Scaling**         | Simple: Automatic vertical and horizontal scaling.                                          | Manual: Scaling requires additional setup and effort.                                    |
| **Integration**     | Seamless: Integrates easily with Google Cloud services like BigQuery and App Engine.        | Custom: Integration with external services requires manual work.                         |
| **Customizability** | Limited: Configuration options are restricted to what the service allows.                   | High: Full control over Postgres settings and extensions.                                |
| **Security**        | Strong: Built-in encryption, IAM, and firewall rules ensure strong security.                | Flexible: You are responsible for implementing and maintaining security measures.        |




