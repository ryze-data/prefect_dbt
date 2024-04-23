from datetime import timedelta
import time
from prefect import flow, task
from prefect.tasks import task_input_hash

@task
def my_task():
    time.sleep(5)
    print("Hello, I'm a task called my_task()")

@flow(name="Subflow")
def my_subflow_two(msg):
    print(f"Subflow says: {msg}")
    my_task.submit()
    my_task.submit()
    my_task.submit()