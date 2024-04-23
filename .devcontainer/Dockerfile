FROM mcr.microsoft.com/devcontainers/base:ubuntu-22.04
# FROM mcr.microsoft.com/devcontainers/python:3.11-bullseye
# FROM mcr.microsoft.com/devcontainers/python:3.12-bullseye

# Version: prefect:2.16.9-python3.10-ubuntu22.04
RUN sudo apt-get update && \
    # install pip3-pip
    sudo apt-get install --no-install-recommends -y python3-pip && \
    pip3 install --upgrade pip && \
    # install prefect and prefect integrations (prefect working on suppporting pydantic v2)
    pip3 install prefect==2.16.9 prefect-shell prefect-dbt pydantic==1.10.6 && \
    # install dbt
    pip3 install dbt-core==1.7.13 dbt-snowflake==1.7.3 && \
    # install postgres
    pip3 install psycopg2-binary==2.9.3 && \
    # install cloud sdks
    # TODO: aws, azure
    # install certain specific versions for compatibility
    pip3 install s3fs==2022.8.2 cryptography==42.0.4 && \
    # TODO: install odbc driver
    # TODO: mongoexport driver
    # install github cli
    # sudo mkdir -p -m 755 /etc/apt/keyrings && wget -qO- https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo tee /etc/apt/keyrings/githubcli-archive-keyring.gpg > /dev/null && sudo chmod go+r /etc/apt/keyrings/githubcli-archive-keyring.gpg && echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null && sudo apt install gh -y
    sudo apt-get clean && sudo rm -rf /var/lib/apt/lists/*
    