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


@flow()
def flow_2(name="world"):
    
    message = print_hello.submit(name="Task 1 concurrent")
    message_2 = print_hello.submit(name="Task 2 concurrent")
    message_3 = print_hello(name="Task 3 concurrent", wait_for=[message, message_2])

if __name__ == "__main__":
    flow_2(name="world")