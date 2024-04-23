from datetime import timedelta
import time
from prefect import flow, task
from prefect.tasks import task_input_hash
from subflow_one import my_subflow
from subflow_two import my_subflow_two

@flow(name="Hello Flow")
def hello_world(name="world"):
    message = print_hello.submit(name="Task 1 concurrent")
    message_2 = print_hello.submit(name="Task 2 concurrent")
    message_3 = print_hello.submit(name="Task 3 concurrent")
    
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


@flow(log_prints=True)
def flow_of_tasks():
    upstream_result = upstream.submit()
    downstream_1_result = downstream_1.submit(upstream_result)
    downstream_2_result = downstream_2.submit(upstream_result)
    mapped_task_results = mapped_task.map([downstream_1_result, downstream_2_result])
    final_task(mapped_task_results)

@task
def upstream():
    return "Hello from upstream!"

@task
def downstream_1(input):
    return input

@task
def downstream_2(input):
    return input

@task
def mapped_task(input):
    return input

@task
def final_task(input):
    print(input)

if __name__ == "__main__":
    hello_world("Marvin")