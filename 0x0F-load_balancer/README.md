# 0x0F. Load balancer

## Concepts
For this project, we expect you to look at these concepts:
* [Load balancer]()
* [Web stack debugging]()

## Background Context
You have been given 2 additional servers:
* gc-[STUDENT_ID]-web-02-XXXXXXXXXX
* gc-[STUDENT_ID]-lb-02-XXXXXXXXXX

Let's improve our web stack so that there is [redundancy]() for our web servers.
This will allow us to be able to accept more traffic by doubling the number of web servers, and to make our infrastructure more reliable. If one web server fails, we will still have a second one to handle requests.

For this project, you will need to write Bash scripts to automate your work. All scripts must be designed to configure a brand new Ubuntu server to match the task requirements.

## Resources
### **Read or watch**
* [Introduction to load-balancing and HAproxy]()
* [HTTP header]()
* [Debian/Ubuntu HAproxy packages]()

## Tasks
### 0. Double the number of web servers
In the first task you need to configure *web-02* to be identical to *web-01*. Fortunately, you built a Bash script during your [web server project](), and they'll now come in handy to easily configure *web-02*. Remember, always try to automate your work!

Since we're placing our web servers behing a load balancer for theis project, we want to add a custom Nginx response header. The goal here is to be able to track which server is answering our HTTP requests, to understand and track the way a load balancer works.

More in the coming tasks

Requirements
* Configure Nginx so that its HTTP response contains a custom header (on *web-01* and *web-02*)
	* The name of the custom HTTP header must be *X-Served-By*
	* The value of the custom HTTP header must be the hostname of the server Nginx is running on
* Write 0-custom_http_response_header so that it configures a brand new Ubuntu machine to the requirements asked in this task
	* [Ignore]() [SC2154]() for *shellcheck*

If your server's hostnames are not properly configures (*[STUDENT_ID]-web-01* and *[STUDENT_ID]-web-02*), follow this [tutorial]()

File: [0-custom_http_response_header]()

### 1. Install your load balancer
Install and configure HAproxy on your *lb-01* server

Requirements:
* Configure HAproxy so that it sends traffic to *web-01* and *web-02*
* Distribute request using a round robin algorithm
* Make sure that HAproxy can be managed via an init script
* Make sure that your servers are configured with the right hostnames: *[STUDENT_ID]-web-01* and *[STUDENT]-web-02*. If not, follow this [tutorial]()
* For your answer file, write a Bash script that configures a new Ubuntu machine to respect above requirements

File: [1-install_load_balancer]()

### 2. Add a custom HTTP header with puppet
