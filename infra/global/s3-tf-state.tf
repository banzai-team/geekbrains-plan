resource "yandex_iam_service_account" "s3-sa" {
  folder_id = var.folder_id
  name      = "${var.project}-s3-sa"
}

// Grant permissions
resource "yandex_resourcemanager_folder_iam_member" "sa-editor" {
  folder_id = var.folder_id
  role      = "storage.admin"
  member    = "serviceAccount:${yandex_iam_service_account.s3-sa.id}"
}

// Create Static Access Keys
resource "yandex_iam_service_account_static_access_key" "sa-static-key" {
  service_account_id = yandex_iam_service_account.s3-sa.id
  description        = "static access key for object storage"
}

resource "yandex_storage_bucket" "geekbrains-tf-state" {
  bucket     = "${var.project}-tf-state"
  access_key = yandex_iam_service_account_static_access_key.sa-static-key.access_key
  secret_key = yandex_iam_service_account_static_access_key.sa-static-key.secret_key
}
