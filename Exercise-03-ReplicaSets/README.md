# Exercise 3: Scaling Flask App Using ReplicaSets

## Objective

Understand Kubernetes ReplicaSets, Pod replication, scaling, health probes, and automatic Pod replacement using a simulated e-commerce flash-sale application.

## Real-Life Use Case

During an e-commerce flash sale, application traffic can increase suddenly. A ReplicaSet maintains the desired number of application Pods and creates replacements when Pods are deleted or fail.

## Files

- `app.py` — Flask application with homepage, purchase, and health endpoints.
- `Dockerfile` — Builds the application image using Python 3.11, Flask, and Gunicorn.
- `replicaset.yaml` — Defines the `flashsale-rs` ReplicaSet, three initial replicas, health probes, and resource requests and limits.
- `service.yaml` — Defines the `flashsale-svc` ClusterIP Service.

## Application Endpoints

- `/` — Returns a welcome message and the serving Pod hostname.
- `/buy?user=123` — Simulates a purchase and returns a random product, user ID, and serving Pod hostname.
- `/health` — Returns the application health status and Pod hostname.

## Implementation

1. Built the image using `minikube image build -t flashsale:1.0 .`.
2. Applied the ReplicaSet using `kubectl apply -f replicaset.yaml`.
3. Applied the Service using `kubectl apply -f service.yaml`.
4. Verified that all three initial Pods reached the Running and Ready state.
5. Accessed the application through a port-forward using `kubectl port-forward service/flashsale-svc 8080:80`.
6. Tested the homepage, purchase, and health endpoints successfully.
7. Scaled the ReplicaSet from three to five replicas using `kubectl scale rs flashsale-rs --replicas=5`.
8. Deleted one Pod and verified that Kubernetes created a replacement.
9. Inspected Pod placement using `kubectl get pods -l app=flashsale -o wide`.
10. Inspected application logs using `kubectl logs`.

## Verification

The three application endpoints responded successfully. The ReplicaSet was scaled to five replicas, and deleting a Pod triggered automatic replacement.

All Pods run on the single Minikube node in this exercise.

## Lab Questions and Answers

**Q1. What is the initial number of replicas in the ReplicaSet?**

Answer: 3.

**Q2. How many Pods run after applying the ReplicaSet configuration?**

Answer: 3.

**Q3. What happens when the ReplicaSet is scaled to five replicas?**

Answer: Kubernetes creates two additional Pods to reach the desired count of five.

**Q4. What happens when one Pod is deleted?**

Answer: The ReplicaSet creates a replacement Pod to maintain five replicas.

**Q5. How does Kubernetes maintain the desired number of replicas?**

Answer: It continually compares the actual number of matching Pods with the desired count and creates or removes Pods as needed.

**Q6. How many nodes are running?**

Answer: 1.

**Q7. Where are the Pods running with respect to nodes?**

Answer: All five Pods run on the single Minikube node.

## Useful Commands

```powershell
kubectl get pods -l app=flashsale -o wide
kubectl logs -l app=flashsale --tail=10
kubectl describe rs flashsale-rs
kubectl scale rs flashsale-rs --replicas=5
kubectl delete pod <pod-name>
```

## Cleanup

Run these commands when finished:

```powershell
kubectl delete -f service.yaml
kubectl delete -f replicaset.yaml
```
