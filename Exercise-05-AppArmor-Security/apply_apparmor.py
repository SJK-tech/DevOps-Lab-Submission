import docker

client = docker.from_env()

print("Building image from Dockerfile...")
client.images.build(path=".", tag="flask-apparmor")

print("Running container with AppArmor profile...")

try:
    container = client.containers.run(
        "flask-apparmor",
        name="flask-apparmor-sdk-test",
        ports={"5000/tcp": 5002},
        security_opt=["apparmor=my-apparmor-profile"],
        detach=True
    )

    print(f"Container started: {container.short_id}")

    container_info = client.api.inspect_container(container.id)
    apparmor_profile = container_info["HostConfig"]["SecurityOpt"]

    print(f"Configured security options: {apparmor_profile}")
    print("Note: configured options do not prove AppArmor enforcement.")

finally:
    try:
        container.stop()
        container.remove()
        print("Container stopped and removed.")
    except (NameError, docker.errors.NotFound):
        pass