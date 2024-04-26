resource "random_string" "unique_id" {
  length  = 8
  upper   = false
  lower   = true
  numeric = true
  special = false
}

variable "folder_id" {
  type    = string
  default = null
}

variable "project" {
  type = string
}

variable "access_key" {
  type      = string
  default   = null
  sensitive = true
}

variable "secret_key" {
  type      = string
  default   = null
  sensitive = true
}

variable "website_domain" {
  type = string
}

variable "existing_certificate_id" {
  type    = string
  default = null
}

variable "with_cdn" {
  type    = bool
  default = false
}
#
#variable "cors_rule" {
#  description = <<EOF
#    (Optional) List of objets containing rules for Cross-Origin Resource Sharing.
#    For more information see https://cloud.yandex.com/en/docs/storage/concepts/cors.
#
#    Configuration attributes:
#      allowed_headers - (Optional) Specifies which headers are allowed.
#      allowed_methods - (Required) Specifies which methods are allowed. Can be `GET`, `PUT`, `POST`, `DELETE` or `HEAD` (case sensitive).
#      allowed_origins - (Required) Specifies which origins are allowed.
#      expose_headers  - (Optional) Specifies expose header in the response.
#      max_age_seconds - (Optional) Specifies time in seconds that browser can cache the response for a preflight request.
#  EOF
#  nullable    = false
#  type = list(object({
#    allowed_headers = optional(set(string))
#    allowed_methods = set(string)
#    allowed_origins = set(string)
#    expose_headers  = optional(set(string))
#    max_age_seconds = optional(number)
#  }))
#  validation {
#    condition = alltrue([
#      for k in var.cors_rule : (
#      length(setsubtract(k.allowed_methods, ["GET", "PUT", "POST", "DELETE", "HEAD"])) == 0
#      )
#    ])
#    error_message = "CORS \"allowed_methods\" can be GET, PUT, POST, DELETE or HEAD (case sensitive)."
#  }
#  default = []
#}

variable "website" {
  description = <<EOF
    (Optional) Object for static web-site hosting or redirect configuration.
    For more information see https://cloud.yandex.com/en/docs/storage/concepts/hosting.

    Configuration attributes:
      index_document           - (Required, unless using redirect_all_requests_to) Storage returns this index document when requests are made to the root domain or any of the subfolders.
      error_document           - (Optional) An absolute path to the document to return in case of a 4XX error.
      routing_rules            - (Optional) List of json arrays containing routing rules describing redirect behavior and when redirects are applied. For more information see https://cloud.yandex.com/en/docs/storage/s3/api-ref/hosting/upload#request-scheme.
      redirect_all_requests_to - (Optional) A hostname to redirect all website requests for this bucket to. Hostname can optionally be prefixed with a protocol (http:// or https://) to use when redirecting requests. The default is the protocol that is used in the original request. When set, other website configuration attributes will be skiped.

    The `routing_rules` object supports the following attributes:
      condition - (Optional) Object used for conditions that trigger the redirect. If a routing rule doesn't contain any conditions, all the requests are redirected.
      redirect  - (Required) Object for configure redirect a request to a different page, different host, or change the protocol.

    The `condition` object supports the following attributes:
      key_prefix_equals               - (Optional) Sets the name prefix for the request-originating object.
      http_error_code_returned_equals - (Optional) Specifies the error code that triggers a redirect.

    The `redirect` object supports the following attributes:
      protocol                - (Optional) In the Location response header, a redirect indicates the protocol scheme (http or https) to be used.
      host_name               - (Optional) In the Location response header, a redirect indicates the host name to be used.
      replace_key_prefix_with - (Optional) Specifies the name prefix of the object key replacing `key_prefix_equals` in the redirect request. Incompatible with `replace_key_with`.
      replace_key_with        - (Optional) Specifies the object key to be used in the Location header. Incompatible with `replace_key_prefix_with`.
      http_redirect_code      - (Optional) In the Location response header, a redirect specifies the HTTP redirect code. Possible values: any 3xx code.

    The default value for index_document is used in case, when a website object is specified in the module input variables,
    but the index_document or redirect_all_requests_to are not set.
  EOF
  type        = object({
    index_document = optional(string, "index.html")
    error_document = optional(string, "index.html")
    routing_rules  = optional(list(object({
      condition = optional(object({
        key_prefix_equals               = optional(string)
        http_error_code_returned_equals = optional(string)
      }))
      redirect = object({
        protocol                = optional(string)
        host_name               = optional(string)
        replace_key_prefix_with = optional(string)
        replace_key_with        = optional(string)
        http_redirect_code      = optional(string)
      })
    })))
    redirect_all_requests_to = optional(string)
  })

  validation {
    condition     = try((length(var.website.routing_rules) != 0), true)
    error_message = "Website \"routing_rules\" cannot be empty list."
  }

  # Explanation of the conditions below.

  # First, determine whether the `website` is set and whether can get a list of objects in `routing_rules`:
  #   try(coalesce(var.website.routing_rules, []), [])
  # Here:
  #   - if `var.website.routing_rules` does not exist because no policy is set (var.website = null),
  # then the `coalesce` function will return an error, which will be handled by the `try` function and return an empty list as a fallback.
  #   - if `var.website.routing_rules` is null, assume that the variable does not have a valid value.
  # The `coalesce` function will skip the value and return an empty list as a fallback.
  #   - in other cases, a list of objects in `routing_rules` will be returned.

  # Then, for each object in the list of `routing_rules`, check the values of `replace_key_with` and `replace_key_prefix_with`.
  # If both are set at the same time then return true. Collect all the results in a list for checking by the `anytrue` function.
  # If at least one object returns true, then consider the condition not fulfilled.
  validation {
    condition = !(anytrue([
      for k in try(coalesce(var.website.routing_rules, []), []) :
      k.redirect.replace_key_prefix_with != null && k.redirect.replace_key_with != null
      ]))
    error_message = "Attributes \"replace_key_prefix_with\" and \"replace_key_with\" conflicts. Only one of them should be used in each \"redirect\" rule."
  }

  # For each object in the list of `routing_rules`, validate the value of `redirect.protocol`, if it is set.
  # Collect all the results in a list for checking by the `alltrue` function.
  # If at least one object returns false, then consider the condition not fulfilled.
  validation {
    condition = alltrue([
      for k in try(coalesce(var.website.routing_rules, []), []) :
      contains(["http", "https"], k.redirect.protocol) if k.redirect.protocol != null
    ])
    error_message = "Website redirect \"protocol\" valid value is \"http\" or \"https\"."
  }

  # For each object in the list of `routing_rules`, validate the value of `redirect.http_redirect_code`, if it is set.
  # Collect all the results in a list for checking by the `alltrue` function.
  # If at least one object returns false, then consider the condition not fulfilled.
  validation {
    condition = alltrue([
      for k in try(coalesce(var.website.routing_rules, []), []) :
      can(regex("^30[0-8]$", k.redirect.http_redirect_code)) if k.redirect.http_redirect_code != null
    ])
    error_message = <<EOF
      Only valid 3xx Redirection code are allowed in "http_redirect_code".
For more information see https://en.wikipedia.org/wiki/List_of_HTTP_status_codes.
EOF
  }
  default = {}
}

variable "https" {
  description = <<EOF
    (Optional) Object manages https certificate for bucket.
    For more information see https://cloud.yandex.com/en/docs/storage/operations/hosting/certificate.

    At least one of `certificate`, `existing_certificate_id` must be specified.

    Configuration attributes:
      existing_certificate_id - (Optional) Id of an existing certificate in Yandex Cloud Certificate Manager, that will be used for the bucket.
      certificate             - (Optional) Object allows to manage the parameters for generating a managed HTTPS certificate in Yandex Cloud Certificate Manager.

    The `certificate` object supports the following attributes:
      domains             - (Required) Domains for this certificate.
      public_dns_zone_id  - (Required) The id of the DNS zone in which record set will reside.
      dns_records_ttl     - (Optional) The time-to-live of DNS record set (seconds). Default value is `300`.
      name                - (Optional) Certificate name. Conflicts with `name_prefix`.
      name_prefix         - (Optional) Prefix of the certificate name. A unique certificate name will be generated using the prefix. Default value is `s3-https-certificate`. Conflicts with `name`.
      description         - (Optional) Certificate description.
      labels              - (Optional) Labels to assign to certificate.
      deletion_protection - (Optional) Prevents certificate deletion. Default value is `false`.

    It will try to create bucket using IAM-token in provider config, not using access_key.
  EOF
  type        = object({
    existing_certificate_id = optional(string)
    certificate             = optional(object({
      domains             = set(string)
      public_dns_zone_id  = string
      dns_records_ttl     = optional(number, 300)
      name                = optional(string)
      name_prefix         = optional(string)
      description         = optional(string, "Certificate for S3 static website.")
      labels              = optional(map(string))
      deletion_protection = optional(bool, false)
    }))
  })
  validation {
    condition     = !(try(var.https.certificate == null, false) && try(var.https.existing_certificate_id == null, false))
    error_message = "One of \"certificate\" or \"existing_certificate_id\" is required."
  }
  validation {
    condition     = !(try(var.https.certificate != null, false) && try(var.https.existing_certificate_id != null, false))
    error_message = "Attributes \"certificate\" and \"existing_certificate_id\" conflicts. Only one of them should be used."
  }
  validation {
    condition     = !(try(var.https.certificate.name != null, false) && try(var.https.certificate.name_prefix != null, false))
    error_message = "Certificate attributes \"name\" and \"name_prefix\" conflicts. Only one of them should be used."
  }
  default = null
}


