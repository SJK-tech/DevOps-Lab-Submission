# Exercise 2: Minikube and Flask



## Objective

Build a Flask web application inside a Docker image and deploy it to Kubernetes using Minikube.



## Files

- `app.py` — Flask application serving a response on port 15000.

- `Dockerfile` — Builds the application image.

- `flask-deployment.yaml` — Defines the Kubernetes Deployment and NodePort Service.



## Implementation

1\. Built the Docker image using `minikube image build -t flask-app:latest .`.

2\. Deployed the application using `kubectl apply -f flask-deployment.yaml`.

3\. Verified the Deployment rollout using `kubectl rollout status deployment/flask-app`.



## Verification

The Deployment rollout completed successfully. The application endpoint can be tested using `minikube service flask-app-service --url`.



Expected response: `Hello from Flask on Kubernetes!`



## Cleanup

Run `kubectl delete -f flask-deployment.yaml` to remove the Deployment and Service.



