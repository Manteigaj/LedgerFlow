output "project_id" {
  description = "ID of the LedgerFlow Railway project"
  value       = railway_project.ledgerflow.id
}

output "api_service_id" {
  description = "ID of the LedgerFlow API service"
  value       = railway_service.api.id
}

output "celery_service_id" {
  description = "ID of the LedgerFlow Celery service"
  value       = railway_service.celery.id
}

output "postgres_service_id" {
  description = "ID of the LedgerFlow PostgreSQL service"
  value       = railway_service.postgres.id
}

output "redis_service_id" {
  description = "ID of the LedgerFlow Redis service"
  value       = railway_service.redis.id
}

output "postgres_tcp_proxy_domain" {
  value = railway_tcp_proxy.postgres.domain
}

output "postgres_tcp_proxy_port" {
  value = railway_tcp_proxy.postgres.proxy_port
}