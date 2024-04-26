variable "service_account_key_file" {
  type    = string
  default = null
}

variable "cloud_id" {
  type    = string
}

variable "folder_id" {
  type    = string
}

variable "project" {
  type    = string
}

variable "access_key" {
  type    = string
  sensitive = true
}

variable "secret_key" {
  type    = string
  sensitive = true
}
