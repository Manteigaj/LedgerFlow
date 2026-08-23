variable "project_name" {
  description = "Name of the Railway project"
  type        = string
  default     = "ledgerflow"
}

variable "repository" {
  description = "GitHub repository URL"
  type        = string
  default     = "https://github.com/Manteigaj/fastapi"
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

variable "database_name" {
  description = "PostgreSQL database name"
  type        = string
  default     = "ledgerflow"
}

variable "database_user" {
  description = "PostgreSQL database user"
  type        = string
  default     = "ledgerflow"
}

variable "database_password" {
  description = "PostgreSQL database password"
  type        = string
  sensitive   = true
}

variable "openai_api_key" {
  description = "OpenAI API key"
  type        = string
  sensitive   = true
}

variable "jwt_secret_key" {
  description = "Secret key used to sign JWT tokens"
  type        = string
  sensitive   = true
}

variable "jwt_algorithm" {
  description = "JWT signing algorithm"
  type        = string
  default     = "HS256"
}

variable "access_token_expire_minutes" {
  description = "JWT expiration time in minutes"
  type        = number
  default     = 30
}