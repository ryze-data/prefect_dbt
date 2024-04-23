FROM prefecthq/prefect:2.14.10-python3.10

RUN apt update && \
    pip install psycopg2-binary==2.9.3 s3fs==2022.8.2 cryptography==42.0.4

# The /app directory should act as the main application directory
WORKDIR /app

COPY ./jaffle_shop /app/jaffle_shop

EXPOSE 4200
EXPOSE 8080