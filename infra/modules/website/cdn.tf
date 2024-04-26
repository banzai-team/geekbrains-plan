resource "yandex_cdn_origin_group" "website" {
  count = var.with_cdn ? 1 : 0

  name = "${var.project}-landing"

  origin {
    source = "${var.website_domain}.${yandex_storage_bucket.this.website_domain}"
    backup = false
  }
}


resource "yandex_cdn_resource" "this" {
  count = var.with_cdn ? 1 : 0

  cname = var.website_domain

  active = true

  origin_protocol = "http"
  origin_group_id = yandex_cdn_origin_group.website[0].id

  dynamic "ssl_certificate" {
    for_each = range(var.with_cdn ? 1 : 0)
    content {
      type                   = "certificate_manager"
      certificate_manager_id = try(coalesce(var.existing_certificate_id, yandex_cm_certificate.this[0].id))
    }
  }

  options {
    gzip_on                = true
    redirect_http_to_https = true

    browser_cache_settings = "1800"
    ignore_cookie          = true
    ignore_query_params    = false
    edge_cache_settings    = 345600
    static_request_headers = {
      is-from-cdn = "yes"
    }
    static_response_headers = {
      is-cdn = "yes"
    }
  }
}