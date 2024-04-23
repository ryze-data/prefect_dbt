from prefect import flow, task
from prefect_dbt.cli.commands import DbtCoreOperation

@task
def dbt_debug():
    result = DbtCoreOperation(
        commands=["dbt debug"],
        project_dir="/workspaces/prefect_dbt/dbt_projects/jaffle_shop",
        profiles_dir="/workspaces/prefect_dbt/dbt_projects/jaffle_shop"
    ).run()
    return result

@task
def dbt_deps():
    result = DbtCoreOperation(
        commands=["dbt deps"],
        project_dir="/workspaces/prefect_dbt/dbt_projects/jaffle_shop",
        profiles_dir="/workspaces/prefect_dbt/dbt_projects/jaffle_shop"
    ).run()
    return result

@task
def dbt_ls():
    result = DbtCoreOperation(
        commands=["dbt clean"],
        project_dir="/workspaces/prefect_dbt/dbt_projects/jaffle_shop",
        profiles_dir="/workspaces/prefect_dbt/dbt_projects/jaffle_shop"
    ).run()
    return result

@task
def dbt_seed():
    result = DbtCoreOperation(
        commands=["dbt seed"],
        project_dir="/workspaces/prefect_dbt/dbt_projects/jaffle_shop",
        profiles_dir="/workspaces/prefect_dbt/dbt_projects/jaffle_shop"
    ).run()
    return result

@task
def dbt_run():
    result = DbtCoreOperation(
        commands=["dbt run"],
        project_dir="/workspaces/prefect_dbt/dbt_projects/jaffle_shop",
        profiles_dir="/workspaces/prefect_dbt/dbt_projects/jaffle_shop"
    ).run()
    return result


@flow
def trigger_dbt_flow() -> str:
    upstream = dbt_ls.submit()
    debug = dbt_debug.submit(wait_for=[upstream])
    deps = dbt_deps.submit(wait_for=[upstream])
    ls = dbt_seed.submit(wait_for=[deps,debug])
    run = dbt_run.submit(wait_for=[ls])



if __name__ == "__main__":
    trigger_dbt_flow()