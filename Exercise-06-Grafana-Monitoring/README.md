

\# Exercise 6: Real-Time Operations Monitoring and Alerting



\## Objective

Build a delivery-monitoring system for ZAPPTTO using Python, Prometheus, Grafana, Docker, and Jenkins.



\## Files

\- `delivery\_metrics.py` — simulates delivery metrics and exposes them on port 8000.

\- `prometheus.yml` — configures Prometheus scraping.

\- `alert\_rules.yml` — defines delivery alert rules.

\- `Dockerfile` — packages the Python metrics exporter.

\- `Jenkinsfile` — validates the files and builds the Docker image.



\## Metrics

\- `total\_deliveries`

\- `pending\_deliveries`

\- `on\_the\_way\_deliveries`

\- `average\_delivery\_time\_sum`

\- `average\_delivery\_time\_count`



\## Setup

Install the Python dependency:



```bash

pip install prometheus-client

