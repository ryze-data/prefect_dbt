import httpx
from prefect import flow


from datetime import timedelta
import time
from prefect import flow, task
from prefect.tasks import task_input_hash

@task(name="Print Hello")
def print_hello(name):
    msg = f"Hello {name}!"
    time.sleep(5)
    print(msg)

    return msg


@flow(name="Hello Flow")
def hello_world(name="world"):
    
    message = print_hello.submit(name="Task 1 concurrent")
    message_2 = print_hello.submit(name="Task 2 concurrent")
    message_3 = print_hello(name="Task 3 concurrent", wait_for=[message, message_2])


if __name__ == "__main__":
    hello_world.from_source(
        "https://github.com/ryze-data/prefect_2_public.git",
        entrypoint="flows/patterns/serving_flows/single_deployment/main.py:hello_world",
    ).serve(
        name="my-first-deployment",
        # cron="0/5 * * * *",
        tags=["testing", "tutorial"],
        description="Given a GitHub repository, logs repository statistics for that repo.",
        version="tutorial/deployments",
        parameters={"name": "world"}
    ).deploy(
        name="no-image-deployment",
        work_pool_name="wp-local-subprocess",
        build=False
    )