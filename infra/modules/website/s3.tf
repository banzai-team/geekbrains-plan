resource "yandex_storage_bucket" "this" {
  bucket     = var.website_domain
  acl        = "public-read"
  access_key = var.access_key
  secret_key = var.secret_key

   https {
     certificate_id = var.https.existing_certificate_id
   }

#  dynamic "cors_rule" {
#    for_each = var.cors_rule
#    content {
#      allowed_headers = cors_rule.value.allowed_headers
#      allowed_methods = cors_rule.value.allowed_methods
#      allowed_origins = cors_rule.value.allowed_origins
#      expose_headers  = cors_rule.value.expose_headers
#      max_age_seconds = cors_rule.value.max_age_seconds
#    }
#  }

  dynamic "website" {
    for_each = range(var.website != null ? 1 : 0)
    content {
      index_document           = var.website.redirect_all_requests_to == null ? var.website.index_document : null
      error_document           = var.website.redirect_all_requests_to == null ? var.website.error_document : null
      routing_rules            = var.website.redirect_all_requests_to == null ? local.routing_rules : null
      redirect_all_requests_to = var.website.redirect_all_requests_to
    }
  }

#  force_destroy = true
}

moved {
  from = yandex_storage_bucket.website
  to   = yandex_storage_bucket.this
}