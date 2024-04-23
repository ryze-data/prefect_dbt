from prefect import flow, task
from prefect_dbt.cli.commands import DbtCoreOperation

@task
def dbt_debug():
    result = DbtCoreOperation(
        commands=["pwd", "dbt debug"],
        project_dir="/workspaces/prefect_dbt/dbt_projects/jaffle_shop"
    ).run()
    return result

@task
def dbt_deps():
    result = DbtCoreOperation(
        commands=["pwd", "dbt deps"],
        project_dir="/workspaces/prefect_dbt/dbt_projects/jaffle_shop"
    ).run()
    return result

@task
def dbt_ls():
    result = DbtCoreOperation(
        commands=["pwd", "dbt ls"],
        project_dir="/workspaces/prefect_dbt/dbt_projects/jaffle_shop"
    ).run()
    return result

@flow
def trigger_dbt_flow() -> str:
    upstream = dbt_ls.submit()
    debug = dbt_debug.submit(wait_for=[upstream])
    deps = dbt_deps.submit(wait_for=[upstream])
    ls = dbt_ls.submit(wait_for=[deps,debug])



trigger_dbt_flow()