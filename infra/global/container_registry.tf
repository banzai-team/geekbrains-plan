resource "yandex_container_registry" "registry" {
  name = "${var.project}-registry"
  folder_id = var.folder_id
}

resource "yandex_container_registry_iam_binding" "pusher" {
  registry_id = yandex_container_registry.registry.id
  role          = "container-registry.images.pusher"

  members = [
    "serviceAccount:${yandex_iam_service_account.s3-sa.id}",
  ]
}

resource "yandex_container_repository" "admin-api" {
  name = "${yandex_container_registry.registry.id}/gk-frontend"
}

resource "yandex_container_repository" "api" {
  name = "${yandex_container_registry.registry.id}/gk-backend"
}