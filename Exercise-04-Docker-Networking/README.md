\# Exercise 4: Docker Networking



\## Objective

Create a custom Docker bridge network and verify communication between containers using container names.



\## Implementation

1\. Create a user-defined bridge network named `devops-net`.

2\. Run two Nginx containers on that network.

3\. Verify that Docker provides network connectivity and DNS resolution between the containers.



\## Commands

```powershell

docker network create devops-net

docker run -d --name web1 --network devops-net nginx

docker run -d --name web2 --network devops-net nginx

docker network inspect devops-net

docker exec web1 nginx -v

```



\## Cleanup

```powershell

docker rm -f web1 web2

docker network rm devops-net

```



