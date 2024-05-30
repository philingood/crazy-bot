import docker
import os


async def get_current_container_name():
    client = docker.from_env()
    container_id = os.environ.get("HOSTNAME")
    container = client.containers.get(container_id)
    return container.name


async def stop_docker_container():
    client = docker.from_env()
    container_name = await get_current_container_name()
    container = client.containers.get(container_name)

    container.update(restart_policy={"Name": "no"})
    container.stop()
    container.remove()
