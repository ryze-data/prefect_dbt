import asyncio
from prefect import task, flow
from prefect_dbt.cli.commands import DbtCoreOperation

@task(task_run_name='task-{name}-1')
async def task_1(name :str):
    await asyncio.sleep(1)

@task(task_run_name='task-{name}-2')
async def task_2(name :str):
    await asyncio.sleep(2)

@task(task_run_name='task-{name}-3')
async def task_3(name :str):
    await asyncio.sleep(3)

@task
def dbt_run():
    result = DbtCoreOperation(
        commands=["dbt run"],
        project_dir="/workspaces/prefect_dbt/dbt_projects/jaffle_shop",
        profiles_dir="/workspaces/prefect_dbt/dbt_projects/jaffle_shop"
    ).run()
    return result

@flow(flow_run_name= 'subflow-{name}-1')
async def async_subflow(name :str):
    await task_1(name)
    await task_2(name)

@flow
def trigger_dbt_flow() -> str:
    dbt_run()

@flow
async def test_async_flow():
    futures = []

    for name in ['A','B','C','D','E']:
        futures.append(async_subflow(name))

    await asyncio.gather(*futures)

    trigger_dbt_flow()

if __name__ == '__main__':
    asyncio.run(test_async_flow())