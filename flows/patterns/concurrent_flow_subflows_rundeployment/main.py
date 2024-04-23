'''
This Prefect Flow pattern requires deployments to concurrent-deployment-1 and concurrent-deployment-2 to have already been created
'''
from prefect import flow, task
from prefect.deployments import run_deployment


@flow
def flow_of_deployments():
    deployment_run_1 = run_deployment_task.submit(
        flow_name="flow-1",
        deployment_name="concurrent_flow_1_deployment",
        parameters={"sleep": 2,"name": "world"},
    )
    deployment_run_2 = run_deployment_task.submit(
        flow_name="flow-2",
        deployment_name="concurrent_flow_2_deployment",
        parameters={"name": "world"},
    )
    downstream_task(wait_for=[deployment_run_1, deployment_run_2])



@task(task_run_name="Run deployment {flow_name}/{deployment_name}")
def run_deployment_task(
    flow_name: str,
    deployment_name: str,
    parameters: dict
):
    run_deployment(
        name=f"{flow_name}/{deployment_name}",
        parameters=parameters
    )


@task
def downstream_task():
    print("I'm downstream!")

if __name__ == "__main__":
    flow_of_deployments()