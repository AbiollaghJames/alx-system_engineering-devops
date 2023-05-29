*For every additional element, why you are adding it*

*3 Firewalla:*

The 1st firewall checks the rules after eceiving request and it can deny access following request.

The 2nd firewall works in the server to ensure security, i.e. prevents one from hacking.

The 3rd firewall acts as a circuit level firewall, it inspects transcarion of information.


*SSL Certificate:*

This secures https protocols and encrypt communication.
It prevents the plain text from being accessed easily by thrid party making communication and transfer of data from browser to the server more secure.

*What are firewalls for*

Firewall is a security device that monitors the traffic of network by analyzing data packets that requests entry into the network.
Firewalls also allow remote access to a private network through secure authentication.

*Why is the traffic served over HTTPS*
HTTPS provides security. It is used to bring protection by uing secure port 443 which encrypts outgoing information.
This makes it difficult to spy or access the site's information.


*What monitoring is used for*

Monitoring is used for quality control.

3 monitoring clients: 2 monitoring deployed in each master-server, and one monitoring client for the load balancer. This will help understand the metrics of the performance of the resources according to the users requests. The information gathered will help us improve users’ experience and make decisions on the future whether to scale up the web infrastructure system.

*How the monitoring tool is collecting data*

The monitoring tool is composed of 3 parts

1. Foundation: This is the infrastructure at the lowest layer. It is composed of physical and virtual devices such as servers, CPUs and VMs

2. Software: This is the section that analyzeswhats happening in the devices in terms of CPU usage, load, memory and running count.

3. Interparetation: The collected data is transformed into metrics and are presented through Graphs or data charts.
This is integrated with tools for data visualization to help better understand and do data analytics.

*Explain what to do if you want to monitor your web server QPS*

Queries per second is a measure of the rate of traffic going in a particular server serving a Web domain. It is an important metric to monitor, because it can help you decide whether to scale the server in order to cope with the demand of usage, and resource requirement so the web page won’t collapse in the future with overload server request.

*Why terminating SSL at the load balancer level is an issue*

This would leave the traffic between Load balancer and web server unencrypted.

*Why having only one MySQL server capable of accepting writes is an issue*

This will cause Single Point of Failure issues as it would not be scallable.

*Why having servers with all the same components (database, web server and application server) might be a problem*

This set up cannot be easily scallable.
It also makes components be contend for resources on server like CPU, Memory I/O which leads to poor performance and also makes it dificult to locate source problems.
