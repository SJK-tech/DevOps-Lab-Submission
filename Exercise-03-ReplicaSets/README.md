\# Exercise 3: Scaling Flask with ReplicaSets



\## Objective

Deploy a Flask container using a Kubernetes ReplicaSet and demonstrate replica scaling.



\## Implementation

\- Created a ReplicaSet configured for three replicas.

\- Exposed the pods using a Kubernetes NodePort Service.

\- Scaled the ReplicaSet to five replicas and then back to three.



\## Verification

Use `kubectl get replicasets` and `kubectl get pods -l app=flask-replicaset` to inspect the replica count and pod status.



\## Cleanup

Run `kubectl delete -f .\\Exercise-03-ReplicaSets\\service.yaml` and `kubectl delete -f .\\Exercise-03-ReplicaSets\\replicaset.yaml`.



