# 2. Secured and monitored web infrastructure

![A secured and monitored web infrastructure](https://github.com/joshua-akuna/alx-system_engineering-devops/blob/master/0x09-web_infrastructure_design/2-secured_and_monitored_web_infrastructure.png)

## Description
The design is a three server web infrastructure that hosts the website www.foobar.com, it must be secured, serve encrypted traffic and be monitored. In additon to the equipment from [https://github.com/joshua-akuna/alx-system_engineering-devops/blob/master/0x09-web_infrastructure_design/1-distrubuted_web_infrastructure.png](1-distributed_web_infrastructure), it adds the following,
* 3 firewalls
* 1 SSL certificate to serve www.foobar.com over HTTPS
* 3 monitoring clients (data collector for the Sumologic or other monitoring services)

## Specifics about the infrastructure
#### What are firewalls for?
Firewalls are implemented either as software or hardware and functions to allow, limit, and block network traffic based on preconfigured rules in the hardware or software, analyzing data packets that request entry to the network.

#### Why is the traffic served over HTTPS?
Traffic is served over HTTPS, which is a secure version of HTTP, to secure all communications between the client device and the website via encryption.

#### What monitoring is used for?
Software monitoring is used to watch computer metrics, record them, and emit an alert if something is unusual or that could make the computer not work properly happens.

#### How the monitoring tools is collecting data?
Monitoring tools tracks the availability, performance, and resource utilization of hosts, containers, and other backend components. Engineers typically install software, called an agent on their hosts,i.e. physical servers, or virtual machines which use the resources of a physical server. The agent collects infrastructure metrics from hosts and sends the data to a monitoring platform for analysis and visualization. Infrastructure monitoring provides visibility into the health of the backend components that run the applications, ensuring that critical services are available for users and that they work as expected.

#### Explain what to do if you want to monitor your web server QPS?
For server applications, such as web servers, databases, caches, queues and load balancers, tools like New Relic and App Dynamic can be used to monitor QPS.

## Issues with the Infrastructure
#### Why terminating SSL at the load balancer level is an issue?
Terminating SSL at the load balancer level would leave the traffic between the load balancer and the web servers unencrpyted.

#### Why having only one MySQL server capable of accepting writes is an issue?
Having only one MySQL server capable of accepting writes is an issue because it is not scalable and can be a Single Point of Failure for the infrastructure.

#### Why having servers with all the same components (database, web server and application server) might be a problem?
Having an infrastructure setup where servers all have the same components would make the components contend for resources on the servers like CPU, memory, I/O. Consequently, this leads to poor performance and makes it difficult to locate the source of the problem. Secondly, such an infrastructure is not easily scalable.
