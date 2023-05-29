Some of the specifics about this Infrastructure:

*1. Server*

A server is a piece of computer hardware or software(Computer program) that provides functionality for other programs or devices, called 'clients'.
This architecture is called the client-server model

Servers manage network resources. For example, a user may set up a server to control access to a network, send/receive e-mail, manage print jobs, or host a website.
They are also proficient at performing intense calculations.
Some servers are committed to a specific task or one website, often called **dedicated servers**. However, many servers today are shared servers that take on the responsibility of e-mail, DNS, FTP and multiple websites in the case of a web server.


*2. Role of Domain Name*

Domain name helps replace the complex IP address numbers into an easily human readable and understandable names to help humans rember and communicate with them better.

*3. Type of DNS record www is in www.foobar.com*

www belongs to the subdomain of the www.foobar.com


*4. Role of a Web Server*


Web Server makes web hosting possible as it enables one to rent a space on a server to store the web files. The web server can also be a large computer that stores and transmits data via a network system like the internet. The Browser is responsible for communication by sending and receiving data that determines what is displayed on the screen.


*5. Role of the Appliction Server*

The Application server facilitates application hosting, installation, operation and delivery to end users, organizations and IT services using diferent protocols and application programming interfaces. It does so by hosting user's business logic which manages data behaviour in Software applications.


*5. Role of Database*


The Database helps store the information gathered in an organized way that can be easily accessed, managed and updated.


*6. What the server uses to communicate with computer of user requesting the website*


The Server uses the HTTP protocol which enables transfer of data like HTML documents between server and client (Browser).
The communication is initialized by the client which's the browser, this is calle request. When the server replies with the necessary files, it's called response.


*ISSUES WITH THE SIMPLE WEB INFRASTRUCTURE*


*- SPOF*

This is referred to as Single Point Failure.
In this infrastructure, if a component of the system fails, there is no backup that can support the continuity of the system. This brings the entire system to a collapse.

*- Downtime when maintenance is neeed*

Whenever some structure of the system needs to be repaired, the whole system has to be shut down during the process.And this means the clients' requests cannot be processed during this period.


*- Cannot scale if too much traffic*

Since scalability is an issue, overload of the traffic can be a risk as it will lead into crash of the system.
