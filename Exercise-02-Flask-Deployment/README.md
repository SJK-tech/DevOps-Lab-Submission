# Exercise 2: Minikube and Flask

## Objective

Build a Flask web application inside a Docker image and deploy it to Kubernetes using Minikube.

## Files

- `app.py` — Flask application serving a response on port 15000.
- `Dockerfile` — Builds the application image.
- `flask-deployment.yaml` — Defines the Kubernetes Deployment and NodePort Service.

## Implementation

1. Started Minikube using `minikube start`.
2. Built the Docker image using `minikube image build -t flask-app:latest .`.
3. Deployed the application using `kubectl apply -f flask-deployment.yaml`.
4. Verified the Deployment rollout using `kubectl rollout status deployment/flask-app`.
5. Configured a NodePort Service to expose the application on port 15000.

## Verification

The Deployment rollout completed successfully.

Run `minikube service flask-app-service --url` to obtain the service URL. Test the URL in a separate PowerShell terminal using `curl.exe`.

Expected response:

`Hello from Flask on Kubernetes!`

**Note:** Confirm the response before claiming that service connectivity has been verified.

## Lab Questions and Answers

### 1. What is the purpose of `minikube service flask-app-service --url`?

It provides a URL for accessing the Flask application through its Kubernetes Service.

### 2. What happens when this command is executed?

Minikube identifies the specified Service and provides a URL through which the application can be accessed.

### 3. What is the purpose of `targetPort` in a Kubernetes Service?

`targetPort` specifies the port on the destination Pod to which traffic is forwarded.

### 4. What is the difference between `port` and `targetPort`?

`port` is the port exposed by the Service, whereas `targetPort` is the port on the application container receiving the traffic.

### 5. How can the Flask application be accessed in Minikube?

Use `minikube service flask-app-service --url` and open or test the resulting URL.

### 6. Why must the terminal remain open when using a Minikube service tunnel?

With certain Minikube drivers and configurations, the command maintains the tunnel required to access the Service. Keep it running while using the URL if the command requires it.

### 7. What is the benefit of using the `--url` option?

It prints the URL that can be used to access the Kubernetes Service.

### 8. How can a Kubernetes Service be exposed?

Use `kubectl expose` to create a Service from an existing resource, or define the Service in a YAML file and apply it using `kubectl apply -f`.

### 9. What is the benefit of Minikube?

Minikube provides a local Kubernetes environment for developing, testing, and learning Kubernetes deployments.

### 10. What is the role of `kubectl`?

`kubectl` is the command-line tool used to interact with Kubernetes and create, inspect, update, and delete cluster resources.

## Cleanup

Run the following command to remove the Deployment and Service:

`kubectl delete -f flask-deployment.yaml`
