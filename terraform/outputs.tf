output "project_id" {
  description = "ID of the LedgerFlow Railway project"
  value       = railway_project.ledgerflow.id
}

output "service_id" {
  description = "ID of the LedgerFlow API service"
  value       = railway_service.api.id
}