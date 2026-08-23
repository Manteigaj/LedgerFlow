resource "railway_project" "ledgerflow" {
  name        = var.project_name
  description = "LedgerFlow - Financial Transaction Management API"
  private     = true
}

# ---------------------------------------------------------
# PostgreSQL
# ---------------------------------------------------------

resource "railway_service" "postgres" {
  name       = "postgres"
  project_id = railway_project.ledgerflow.id

  source_image = "postgres:17"

  volume = {
    name       = "ledgerflow-postgres-volume"
    mount_path = "/var/lib/postgresql/data"
  }
}

resource "railway_variable" "postgres_user" {
  name           = "POSTGRES_USER"
  value          = var.database_user
  environment_id = railway_project.ledgerflow.default_environment.id
  service_id     = railway_service.postgres.id
}

resource "railway_variable" "postgres_password" {
  name           = "POSTGRES_PASSWORD"
  value          = var.database_password
  environment_id = railway_project.ledgerflow.default_environment.id
  service_id     = railway_service.postgres.id
}

resource "railway_variable" "postgres_db" {
  name           = "POSTGRES_DB"
  value          = var.database_name
  environment_id = railway_project.ledgerflow.default_environment.id
  service_id     = railway_service.postgres.id
}

resource "railway_variable" "postgres_pgdata" {
  name           = "PGDATA"
  value          = "/var/lib/postgresql/data/pgdata"
  environment_id = railway_project.ledgerflow.default_environment.id
  service_id     = railway_service.postgres.id
}

# ---------------------------------------------------------
# Redis
# ---------------------------------------------------------

resource "railway_service" "redis" {
  name       = "redis"
  project_id = railway_project.ledgerflow.id

  source_image = "redis:7-alpine"
}

# ---------------------------------------------------------
# API
# ---------------------------------------------------------

resource "railway_service" "api" {
  name       = "api"
  project_id = railway_project.ledgerflow.id

  source_repo        = var.repository
  source_repo_branch = var.branch

  config_path = "/railway.api.toml"
}

resource "railway_variable" "api_openai_key" {
  name           = "OPENAI_API_KEY"
  value          = var.openai_api_key
  environment_id = railway_project.ledgerflow.default_environment.id
  service_id     = railway_service.api.id
}

resource "railway_variable" "api_jwt_secret" {
  name           = "JWT_SECRET_KEY"
  value          = var.jwt_secret_key
  environment_id = railway_project.ledgerflow.default_environment.id
  service_id     = railway_service.api.id
}

resource "railway_variable" "api_jwt_algorithm" {
  name           = "ALGORITHM"
  value          = var.jwt_algorithm
  environment_id = railway_project.ledgerflow.default_environment.id
  service_id     = railway_service.api.id
}

resource "railway_variable" "api_jwt_expiration" {
  name  = "ACCESS_TOKEN_EXPIRE_MINUTES"
  value = tostring(var.access_token_expire_minutes)

  environment_id = railway_project.ledgerflow.default_environment.id
  service_id     = railway_service.api.id
}

resource "railway_variable" "api_database_url" {
  name = "DATABASE_URL"

  value = "postgresql://$${{postgres.POSTGRES_USER}}:$${{postgres.POSTGRES_PASSWORD}}@$${{postgres.RAILWAY_PRIVATE_DOMAIN}}:5432/$${{postgres.POSTGRES_DB}}"

  environment_id = railway_project.ledgerflow.default_environment.id
  service_id     = railway_service.api.id
}

resource "railway_variable" "api_redis_url" {
  name           = "REDIS_URL"
  value          = "redis://$${{redis.RAILWAY_PRIVATE_DOMAIN}}:6379"
  environment_id = railway_project.ledgerflow.default_environment.id
  service_id     = railway_service.api.id
}

# ---------------------------------------------------------
# Celery Worker
# ---------------------------------------------------------

resource "railway_service" "celery" {
  name       = "celery"
  project_id = railway_project.ledgerflow.id

  source_repo        = var.repository
  source_repo_branch = var.branch

  config_path = "/railway.celery.toml"
}

resource "railway_variable" "celery_openai_key" {
  name           = "OPENAI_API_KEY"
  value          = var.openai_api_key
  environment_id = railway_project.ledgerflow.default_environment.id
  service_id     = railway_service.celery.id
}

resource "railway_variable" "celery_jwt_secret" {
  name           = "JWT_SECRET_KEY"
  value          = var.jwt_secret_key
  environment_id = railway_project.ledgerflow.default_environment.id
  service_id     = railway_service.celery.id
}

resource "railway_variable" "celery_jwt_algorithm" {
  name           = "ALGORITHM"
  value          = var.jwt_algorithm
  environment_id = railway_project.ledgerflow.default_environment.id
  service_id     = railway_service.celery.id
}

resource "railway_variable" "celery_jwt_expiration" {
  name  = "ACCESS_TOKEN_EXPIRE_MINUTES"
  value = tostring(var.access_token_expire_minutes)

  environment_id = railway_project.ledgerflow.default_environment.id
  service_id     = railway_service.celery.id
}

resource "railway_variable" "celery_database_url" {
  name = "DATABASE_URL"

  value = "postgresql://$${{postgres.POSTGRES_USER}}:$${{postgres.POSTGRES_PASSWORD}}@$${{postgres.RAILWAY_PRIVATE_DOMAIN}}:5432/$${{postgres.POSTGRES_DB}}"

  environment_id = railway_project.ledgerflow.default_environment.id
  service_id     = railway_service.celery.id
}

resource "railway_variable" "celery_redis_url" {
  name           = "REDIS_URL"
  value          = "redis://$${{redis.RAILWAY_PRIVATE_DOMAIN}}:6379"
  environment_id = railway_project.ledgerflow.default_environment.id
  service_id     = railway_service.celery.id
}