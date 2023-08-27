#2. Secured and monitored web infrastructure
##Description
The design is a three server web infrastructure that hosts the website www.foobar.com, it must be secured, serve encrypted traffic and be monitored. In additon to the equipment from the previous task, this infrastructure adds
* 3 firewalls
* 1 SSL certificate to serve www.foobar.com over HTTPS
* 3 monitoring clients (data collector for the Sumologic or other monitoring services)

##Specifics about the infrastructure
####What are firewalls for?
Firewalls are implemented either as software or hardware and functions to allow, limit, and block network traffic based on preconfigured rules in the hardware or software, analyzing data packets that request entry to the network.

####Why is the traffic served over HTTPS?
Traffic is served over HTTPS, which is a secure version of HTTP, to secure all communications between the client device and the website via encryption.

####What monitoring is used for?
Software monitoring is used to watch computer metrics, record them, and emit an alert if something is unusual or that could make the computer not work properly happens.

####How the monitoring tools is collecting data?
Monitoring tools tracks the availability, performance, and resource utilization of hosts, containers, and other backend components. Engineers typically install software, called an agent on their hosts,i.e. physical servers, or virtual machines which use the resources of a physical server. The agent collects infrastructure metrics from hosts and sends the data to a monitoring platform for analysis and visualization. Infrastructure monitoring provides visibility into the health of the backend components that run the applications, ensuring that critical services are available for users and that they work as expected.

####Explain what to do if you want to monitor your web server QPS?

