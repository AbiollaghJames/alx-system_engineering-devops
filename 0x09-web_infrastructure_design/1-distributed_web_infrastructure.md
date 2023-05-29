*For every additional element, why you are adding it*

The infrastructue is composed of two servers, primary and secondary and load balancer as added infrastructure compared to the previous one.
The two servers hve to be idential.
The load is managed by the load balancer which distributes the queries using the Round-robin algorithm. The Seconadry server is  needed to serve a replica of primary server helping to unload the master server reading the queries.


*What distribution algorithm your load balancer is configured with and how it works*


The Load balancer uses the Round Robin algorithm for distribution of queries.
That means the requests receievd are distributed to every server sequentially one after the other, If the last request was sent to the seconary server, the proceeding one will be sent to the primary server.
This dsiributes work load on the servers equally enabling 50% work between the servers.


*Is your load-balancer enabling an Active-Active or Active-Passive setup, explain the difference between both*


The Load Balancer is enabling an Active-Active set up.

The Active-Active is made up of at least two servers/nodes, both running actively same type of services at the ame time.

This set up achieves load balancing by distributing tasks to different nodes equally.

On the other hand, Active-Passive set up is also made up of at least two nodes.
However, not all nodes are active simultaneously.

While one node is active, the other nodes(failover servers) are passively waiting to be active as back up in case the primary node is disconnected or unble to serve


*How a database Primary-Replica (Master-Slave) cluster works*

This is a mechanism that enables data of one database(the master) to be replicated/copied to one or more databses/computers servers(the slaves) for all users to be able to share same level of information.

The database replication process can either be synchronous or asynchronous. In the first one, the replication process is done from the client server to the model server and then replicated to all the replica servers before the client is notified about the data replication. This method of replication may take longer to verify, however all data was copied before proceeding.

As in the asynchronous replication process, replication is done by sending data from the client to the model server, followed by a confirmation order to the client, who finally gives permission of copying to the replicas at an unspecified or monitored pace

*What is the difference between the Primary node and the Replica node in regard to the application*

One of the main differences between the primary node and the replica node, regarding the application, is that the primary database is regarded as the authoritative source, while the replica database is synchronized to it. The primary node serves as the keeper of information, here the “real” data is kept, then writing only happens here. On the other hand, reading only occurs in the replica or slave node. This architecture purpose is due to safeguard site reliability. In case a site receives a lot of traffic, a replica node prevents overloading of the master node with reading and writing requests. This eases the load of the entire system preventing it to collapse
