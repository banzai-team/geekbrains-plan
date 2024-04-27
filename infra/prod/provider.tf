terraform {
  required_providers {
    yandex = {
      source  = "yandex-cloud/yandex"
      version = "~> 0.113.0"
    }
  }
  required_version = ">= 1.7.4"

  backend "s3" {
  }
}

provider "yandex" {
  service_account_key_file = var.service_account_key_file
  cloud_id                 = var.cloud_id
  folder_id                = var.folder_id
  storage_access_key       = var.access_key
  storage_secret_key       = var.secret_key
  zone = "ru-central1-a"
}
