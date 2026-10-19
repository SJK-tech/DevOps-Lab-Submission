\# Exercise 1: Kubernetes Getting Started



\## Objective

Deploy an Nginx Pod on a local Kubernetes cluster using Minikube and expose it through a NodePort Service.



\## Prerequisites

\- Docker Desktop with its Linux engine running

\- Minikube

\- kubectl



\## Implementation

The Nginx Pod was created using `kubectl run` and exposed using `kubectl expose`.



\## Commands executed

```powershell

minikube start --driver=docker

kubectl run hello-k8s --image=nginx --port=80

kubectl wait --for=condition=Ready pod/hello-k8s --timeout=180s

kubectl expose pod hello-k8s --type=NodePort --port=80

kubectl get nodes

kubectl get pods

kubectl get services

minikube service hello-k8s

```



\## Verification results

\- Kubernetes node status: Ready

\- Pod: hello-k8s

\- Pod status: Running

\- Ready containers: 1/1

\- Restarts: 0

\- Service type: NodePort

\- Service port: 80

\- Assigned NodePort: 30163



\## Access

Minikube opened the service through a local tunnel. The terminal must remain open while the tunnel is running.



\## Cleanup

```powershell

kubectl delete service hello-k8s

kubectl delete pod hello-k8s

minikube stop

```



\## Status

Pod and Service creation were verified using kubectl. Confirm the Nginx welcome page in the browser to complete the browser verification.

