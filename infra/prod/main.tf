data "yandex_compute_image" "container-optimized-image" {
  family = "container-optimized-image"
}

module "website" {
  source  = "../modules/website"
  project = var.project

  website_domain = "geekbrains.banzai-predict.site"

  website = {
    index = "index.html"
    error = "index.html"
  }

  https = {
    existing_certificate_id = "fpqn58g6b03v8bmn1ejl"
  }
}

resource "yandex_vpc_security_group" "level-instance-sg" {
  name        = "${var.project}-instance-sg"
  description = "description for my security group"
  network_id  = module.net.vpc_id

  labels = {
  }

  ingress {
    protocol       = "TCP"
    description    = "http"
    v4_cidr_blocks = ["0.0.0.0/0"]
    port           = 80
  }

  ingress {
    description       = "Communication inside this SG"
    from_port         = -1
    port              = -1
    predefined_target = "self_security_group"
    protocol          = "ANY"
    to_port           = -1
    v4_cidr_blocks    = []
    v6_cidr_blocks    = []
  }

  ingress {
    protocol       = "TCP"
    description    = "ssh"
    v4_cidr_blocks = ["0.0.0.0/0"]
    port           = 22
  }

  egress {
    protocol       = "ANY"
    description    = "any"
    v4_cidr_blocks = ["0.0.0.0/0"]
    from_port      = 0
    to_port        = 65535
  }
}

resource "yandex_iam_service_account" "sa-instance" {
  name        = "${var.project}-instance"
  description = "service account to work with instance"
}

resource "yandex_resourcemanager_folder_iam_member" "sa-instance-invoker" {
  folder_id = var.folder_id
  role      = "container-registry.images.puller"
  member    = "serviceAccount:${yandex_iam_service_account.sa-instance.id}"
}

locals {
  default_zone = "ru-central1-a"
}

module "net" {
  source              = "github.com/terraform-yc-modules/terraform-yc-vpc"
  labels = { tag = "prod", company : "level" }
  network_description = "Network for hr-level project"
  network_name        = "${var.project}-network"
  create_vpc          = true
  public_subnets      = [
    {
      "v4_cidr_blocks" : ["10.121.0.0/16"],
      "zone" : local.default_zone
    },
  ]
}

resource "yandex_compute_instance" "backend" {
  boot_disk {
    initialize_params {
      name     = "geekbrains"
      image_id = data.yandex_compute_image.container-optimized-image.id
      size     = 50
    }
  }

  service_account_id = yandex_iam_service_account.sa-instance.id
  network_interface {
    subnet_id = module.net.public_subnets["10.121.0.0/16"].subnet_id
    nat       = true

    security_group_ids = [yandex_vpc_security_group.level-instance-sg.id]
  }
  resources {
    cores  = 4
    memory = 8
    #     core_fraction = 20
  }
  metadata = {
    "ssh-keys"     = <<-EOT
                    yc-user:ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIEi/t2y3WUENzZ2y8rvDzQu6+/GqQOvDqdaf8xLwCn0K jamakase@Artems-MacBook-Pro.local
            EOT
    docker-compose = templatefile("${path.module}/../../docker-compose.yaml", {
      DB_USER : "postgres"
      DB_PASSWORD : "2Od5uhnPl5po"
      DB_NAME : "postgres"
      ROOT_DIR : "/home/yc-user/"
    })
    user-data = file("${path.module}/cloud-config/cloud_config.yaml")
  }

  lifecycle {
    ignore_changes = [boot_disk[0].initialize_params[0].image_id]
  }
}