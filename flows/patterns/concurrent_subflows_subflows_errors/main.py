from datetime import timedelta
import time
from prefect import flow, task
from prefect.tasks import task_input_hash
from subflow_one import my_subflow
from subflow_two import my_subflow_two

@task(name="Print Hello")
def print_hello(name):
    msg = f"Hello {name}!"
    time.sleep(5)
    print(msg)
    my_task.fn()
    return msg

@task
def my_task():
    time.sleep(3)
    print("Hello, I'm a task called my_task()")

@task(cache_key_fn=task_input_hash, cache_expiration=timedelta(days=1))
def hello_task(name_input):
    # Doing some work
    print("Saying hello")
    return "hello " + name_input

@flow(name="Hello Flow")
def hello_world(name="world"):
    message = print_hello.submit(name="Task 1 concurrent")
    message_2 = print_hello.submit(name="Task 2 concurrent")
    message_3 = print_hello.submit(name="Task 3 concurrent")
    my_subflow(message)
    my_subflow_two(message)

hello_world("Marvin")