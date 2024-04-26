resource "yandex_iam_service_account" "tf-sa" {
  folder_id = var.folder_id
  name      = "${var.project}-tf-sa"
}

// Grant permissions
resource "yandex_resourcemanager_folder_iam_member" "tf-admin" {
  folder_id = var.folder_id
  role      = "editor"
  member    = "serviceAccount:${yandex_iam_service_account.tf-sa.id}"
}
