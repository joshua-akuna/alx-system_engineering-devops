# 3. Scale up
![A scaled-up web infrastructure](https://github.com/joshua-akuna/alx-system_engineering-devops/blob/master/0x09-web_infrastructure_design/3-scale_up.png)

## Infrastructure Description
This infrastructure is a scaled up version of the one in [https://github.com/joshua-akuna/alx-system_engineering-devops/blob/master/0x09-web_infrastructure_design/2-secured_and_monitored_web_infrasture.png](2-secured_and_monitored_web_infrastructure). In this infrastructure, all SPOF's have been eliminated and each of the major component (server, web server, application server and database server) have been moved to a separate Linux server. The SSL protection isn't terminated at the load-balancer and each server's network is protected with a firewall and monitored.

## Specifics about the Infrastructure
#### Placing a firewall between servers.
This protects each server from unwanted and unautorized users instead of protecting a single server.

## Issues with the Infrastructure
#### High cost of maintenance.
Placing each of the major components in its own server requires that more servers would need to be bought, resulting in an increase in electricity bills. Consequently, company funds would be use to buy servers and pay for electricity needed to keep all servers running.
