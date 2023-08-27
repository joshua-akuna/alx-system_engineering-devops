# 0. Simple web stack

![A simple web stack](https://github.com/joshua-akuna/alx-system_engineering-devops/blob/master/0x09-web_infrastructure_design/0-simple_web_stack.png)

## Infrastructure Description
This is a one server web infrastruture that hosts the website that is reachable via www.foobar.com. It consists of
* 1 server
* 1 web server (Nginx)
* 1 application server
* 1 application files (your code base)
* 1 database (MySQL)
* 1 domain name foobar.com configured with a www record that points to your server IP 8.8.8.8

## Specifics about the infrastructure.
#### What is a server?
A server is a piece of computer hardware or software that provides functionality for other programs or devices called clients.
#### What is the role of a domain name?
A domain name serve to identify internet resources, such as computers, networks and services, with a text based label that is easier to memorize than the numerical addresses used in internet protocol.
#### What type of DNS record www is in www.foobar.com
www is a CNAME (Canonical Name) DNS record-type in www.foobar.com since it also points to the same IP addresses as foobar.com and if the IP address changes, we can only record changes in the DNS A record of foobar.com
#### What is the role of a web server.
A web server is a software that handles the HTTP protocol by recieivng HTTP requests and sending HTTP responses.
#### What is the role of an application server?
An application server is a software that exposes business logic to client applications through various protocols, possibly including HTTP.
#### What is the role of a database?
The role of a database is to organize a collection of structured information, data, typically stored electronically in a computer system.
#### What is the server using to communicate with the computer of the user requestion the website.
The server communicates with client computers using the TCP/IP protocol suite.

## Issues associated with this infrastructure.
#### SPOF - Single Point of Failure.
There are a few Single Point of Failure in this infrastructure, i.e. failure in the MySQL database server would result in loss of the entire website.
#### Downtime when maintenance needed (like deploying new code web server needs to be restarted)
When maintenance is performed on the any component on the server, the server has to be shut down resulting in downtimes.
#### Cannot scale if too much incoming traffic.
The stated infrastructure cannot scale if there's too much incoming traffic due to the absence of a second server in the system to share loads, resulting to an overloading of the server.
