FROM mcr.microsoft.com/devcontainers/base:ubuntu-22.04
# FROM mcr.microsoft.com/devcontainers/python:3.11-bullseye
# FROM mcr.microsoft.com/devcontainers/python:3.12-bullseye

# Version: prefect:2.16.9-python3.10-ubuntu22.04
RUN sudo apt-get update && \
    # install pip3-pip
    sudo apt-get install --no-install-recommends -y python3-pip && \
    pip3 install --upgrade pip && \
    # install prefect and prefect integrations (prefect working on suppporting pydantic v2)
    pip3 install prefect prefect-shell prefect-dbt && \
    # install dbt
    pip3 install dbt-core dbt-snowflake && \
    # install postgres
    pip3 install psycopg2-binary && \
    # install cloud sdks
    # TODO: aws, azure
    # install certain specific versions for compatibility
    pip3 install s3fs cryptography && \
    # TODO: install odbc driver
    # TODO: mongoexport driver
    # install github cli
    # sudo mkdir -p -m 755 /etc/apt/keyrings && wget -qO- https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo tee /etc/apt/keyrings/githubcli-archive-keyring.gpg > /dev/null && sudo chmod go+r /etc/apt/keyrings/githubcli-archive-keyring.gpg && echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null && sudo apt install gh -y
    # sudo apt-get update && sudo apt-get install postgresql && \
    sudo apt-get clean && sudo rm -rf /var/lib/apt/lists/*
    