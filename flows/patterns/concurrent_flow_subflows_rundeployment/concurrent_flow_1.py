import time
from prefect import flow, serve, deploy, task

@task(name="Print Hello")
def print_hello(name):
    msg = f"Hello {name}!"
    time.sleep(5)
    print(msg)

    return msg

@flow
def flow_1(sleep: int = 60, name: str ="world"):
    "Sleepy flow - sleeps the provided amount of time (in seconds)."
    time.sleep(sleep)
    message = print_hello.submit(name="Task 1 concurrent")
    message_2 = print_hello.submit(name="Task 2 concurrent")
    fast_flow()
    message_3 = print_hello(name="Task 3 concurrent", wait_for=[message, message_2])


@flow
def fast_flow(name:str ="world"):
    "Fastest flow this side of the Mississippi."
    message_2 = print_hello.submit(name="Task 3 concurrent")
    return

if __name__ == "__main__":
    flow_1(sleep = 5, name="world")