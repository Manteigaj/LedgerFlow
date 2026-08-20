resource "railway_project" "ledgerflow" {
  name        = var.project_name
  description = "LedgerFlow - Financial Transaction Management API"
  private     = true
}

resource "railway_service" "api" {
  name       = "api"
  project_id = railway_project.ledgerflow.id

  source_repo        = var.repository
  source_repo_branch = var.branch
}