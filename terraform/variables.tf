variable "project_name" {
  description = "Name of the Railway project"
  type        = string
  default     = "ledgerflow"
}

variable "repository" {
  description = "GitHub repository URL"
  type        = string
}

variable "branch" {
  description = "Git branch used for deployment"
  type        = string
  default     = "main"
}
variable "railway_token" {
  description = "Railway API token"
  type        = string
  sensitive   = true
}