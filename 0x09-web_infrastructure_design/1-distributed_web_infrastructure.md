#1. Distributed web infrastructure

##Description
This is a design of a three server web infrastructure that hosts the website www.foobar.com consisting of
* 2 servers
* 1 web server (Nginx)
* 1 application server
* 1 load-balancer (HAproxy)
* 1 set of application files (your code base)
* 1 database (MySQL)

##Specifics about the infrastructure

####1 load-balancer (HAproxy)
A load balancer acts to distribute the work-load of your system, i.e. server, to multiple individual systems, or group of systems in order to reduce the amount of load on asingle system, resulting in an increase in reliability, efficiency and availability of your enterprise application or website.

####What distributed algorithm your load balancer is configured with and how does it works?
My load balancer is configured with the Round Robin algorithm distribution. The algorithm works by passing a new connection to the next server in line, eventually distributing connections evenly across the array of machines (servers) being load balanced. This is assuming that my web infrastructure being load balanced consists of equipment with roughly equal processing speed, connection speed, and/or memory.

####Is your load-balancer enabling an Active-Active or Active-Passive setup, explain the difference between both.
My load-balancer enables the Active-Active setup.

The Active-Active setup is typically made up of at least two nodes, both actively running the same type of services simultaenously. Their purpose is to achieve load balancing by distributing tasks to different servers in order to prevent overload. Because there are more nodes available to serve, there is always going to be marked improvement in throughput and response times.

Likewise, the Active-Passive cluster consists of at least two nodes. However, unlike the Active-Active cluster, not all nodes are going to be active. In case of two nodes, if the first node is already active, the second node must be passive or on standby as backup for the active server in case it gets disconnected.

####How a database Primary-Replica (Master-Slave) cluster works?
A database Primary-Replica (Master-Slave) is a mechanism which enables data of one database server (the master) to be replicated or to be copied to one or more computers or database servers (the slaves), in order for all users to share the same level of information. This process leads to a distributed database in which users can quickly access data without interferring with each other.

####What is the difference between the Primary node and the Replica node in regard to the application?
The main difference between the Primary node and the Replica node is the the Primary node is responsible for write operations on the site while the Replica node is capable of processing read-only opeartions, thereby decreasing the read traffic to the Primary node.

##Issues with the infrastructure
####Where are SPOF?
The are multiple Single Point of Failure. i.e. if the Primary MySQL database server fails, it would be impossible to CRUD operations on the site.

In addition, the server containing the load balancer and the application server connecting to the primary database server are possible SPOF's.

####Security Issues (no firewall, no HTTPS)
The data transmitted over the network is not encryted via an SSL certificate and is therefore susceptible to spywares or hacking on the network. This is also no way of blocking unsuthorized IP's since there's no firewall installed on any server.

####No monitoring.
There's no method of determining the status of each server because they are not monitored.
