module "website" {
  source = "../modules/website"
  project = var.project

  website_domain = "geekbrains.banzai-predict.com"

  website = {
    index = "index.html"
    error = "index.html"
  }
}