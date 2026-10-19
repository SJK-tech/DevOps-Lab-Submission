

\# Exercise 5: Docker Security with AppArmor and Python



\## Objective



Explore Docker container security using a Flask application, the Docker SDK for Python, and AppArmor-related security options.



\## Files



\- `app.py` — Flask application serving a message on port 5000.

\- `Dockerfile` — Builds the Flask application image.

\- `apply\_apparmor.py` — Builds the image, starts a container with the requested AppArmor security option, inspects the container configuration, and cleans up.

\- `test\_restricted\_actions.py` — Tests reading `/etc/passwd` and executing `/bin/bash`.



\## Implementation



1\. Built the image using `docker build -t flask-apparmor .`.

2\. Started the Flask container and verified the response at `http://localhost:5000/`.

3\. Installed the Docker SDK for Python.

4\. Ran `apply\_apparmor.py` to start and inspect a container using `security\_opt=\["apparmor=my-apparmor-profile"]`.

5\. Ran `test\_restricted\_actions.py` to test the two restricted actions.



\## Results



The Flask application returned the expected response.



The Docker SDK script reported the configured security option `apparmor=my-apparmor-profile`. However, Docker Desktop reported only `seccomp` and `cgroupns` in its security options.



The restricted-action tests returned exit code 0 for both reading `/etc/passwd` and executing `/bin/bash`. Both actions succeeded, so the expected restrictions were \*\*not demonstrated\*\*.



\*\*Limitation:\*\* Custom AppArmor profile loading and enforcement were not verified in this Windows Docker Desktop environment. Actual enforcement requires a Linux environment that supports AppArmor and has the profile loaded.



\## Questions and Answers



\*\*1. What is the purpose of using AppArmor with Docker containers?\*\*



AppArmor enforces security policies that confine applications and limit access to system resources, files, and networks.



\*\*2. How do AppArmor profiles help secure a Docker container?\*\*



Profiles define permitted and restricted actions, such as file access, network operations, and binary execution.



\*\*3. Why restrict access to `/etc/` and `/var/`?\*\*



These directories contain system configuration, application data, and other important files. Restricting access can reduce the risk of unauthorized reading or modification.



\*\*4. What other capabilities can AppArmor restrict?\*\*



It can restrict file access, execution of binaries, network operations, and certain privileged actions.



\*\*5. How can you verify whether an AppArmor profile is applied?\*\*



Inspect the container's security configuration using the Docker CLI or SDK, and verify enforcement from a Linux environment that supports AppArmor. A recorded security option alone does not prove that the profile is enforced.



