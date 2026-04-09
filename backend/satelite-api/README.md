# Description

# Installation

## Prerequisites

- Python >= 3.12
- PostgreSQL running and accessible

## Environment variables

The database is hosted on [Neon](https://neon.tech) and provisioned via the Vercel Marketplace.
Pull the values from Vercel for local development:

```shell
vercel env pull .env
```

Or set manually:

```shell
DATABASE_URL=postgresql://user:password@host/dbname?sslmode=require
DEBUG_MODE=true
```

## Option A — with uv (recommended)

1. Install uv: https://docs.astral.sh/uv/getting-started/installation/
2. Clone the repository
3. Install dependencies

```shell
uv sync
```

4. Start docker

```shell
docker-compose up -d
```

4. Run the application

```shell
uv run --env-file=.local.env fastapi dev
```

5. Test the application

```shell
curl http://127.0.0.1:8000/api/v1/healthcheck
```

## With IntelliJ IDEA

1. Add UV as Python interpreter
2. Run `vercel env pull .env` to get the env vars locally
3. Configure run configuration with environment variables
    1. Set uv as interpreter
    2. Module name: fastapi
    3. Parameters: dev main.py
    4. Environment variables: load from `.env` (or paste `DATABASE_URL=...;DEBUG_MODE=true`)

# Development

- Update dependencies (uv)

```shell
uv add <package>
```

- Create alembic migration

```shell
alembic revision -m "create table satellites"
```

- Execute alembic migration (local-docker)
```shell
uv run --env-file=.local.env alembic upgrade head
```

- Execute alembic migration (local-vercel)
```shell
uv run --env-file=.env.development.local alembic upgrade head
```

# Vercel deployment

1. Links: 
   2. https://satellite-map-git-main-jose-borettos-projects.vercel.app/api/v1/healthcheck
   3. https://satellite-map-git-main-jose-borettos-projects.vercel.app/api/v1/satellites/
2. 