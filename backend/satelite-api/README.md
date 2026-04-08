# Description

# Installation

## Prerequisites

- Python >= 3.12
- PostgreSQL running and accessible

## Environment variables

```shell
DATABASE_DIALECT=postgresql
DATABASE_HOSTNAME=localhost
DATABASE_PORT=5432
DATABASE_NAME=satellite
DATABASE_PASSWORD=satellite_api_password
DATABASE_USERNAME=satellite_api_user
DEBUG_MODE=true
```

## Option A — with uv (recommended)

1. Install uv: https://docs.astral.sh/uv/getting-started/installation/
2. Clone the repository
3. Install dependencies
```shell
uv sync
```
4. Run the application
```shell
DATABASE_DIALECT=postgresql DATABASE_HOSTNAME=localhost DATABASE_PORT=5432 \
DATABASE_NAME=satellite DATABASE_PASSWORD=satellite_api_password \
DATABASE_USERNAME=satellite_api_user DEBUG_MODE=true \
uv run fastapi dev
```
5. Test the application
```shell
curl http://127.0.0.1:8000/v1/healthcheck/
```

## With IntelliJ IDEA

1. Add UV as Python interpreter
2. Configure run configuration with environment variables
   1. Set uv as interpreter
   2. Module name: fastapi
   3. Parameters: dev main.py
   4. Environment variables: DATABASE_DIALECT=postgresql;DATABASE_HOSTNAME=localhost;DATABASE_PORT=5432;DATABASE_NAME=satellite;DATABASE_PASSWORD=satellite_api_password;DATABASE_USERNAME=satellite_api_user;DEBUG_MODE=true;

# Development

- Update dependencies (uv)
```shell
uv add <package>
```

- Create alembic migration
```shell
alembic revision -m "create table satellites"
```
- Execute alembic migration
   - Set uv as interpreter
   - Module name: alembic 
   - Parameters: upgrade head