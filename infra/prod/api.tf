resource "yandex_api_gateway" "gateway" {
  name        = "${var.project}-api"
  description = "api gateway"
  #  labels = {
  #    label       = "label"
  #    empty-label = ""
  #  }
  #  custom_domains {
  #    fqdn = "test.example.com"
  #    certificate_id = "<certificate_id_from_cert_manager>"
  #  }
  #  connectivity {
  #    network_id = "<dynamic network id>"
  #  }
  spec = <<-EOT
openapi: 3.0.0
info:
  title: Movies API
  version: 1.0.0

x-yc-apigateway:
  cors:
    origin: '*'
    methods: '*'
    allowedHeaders: '*'

paths:
  /{path+}:
    x-yc-apigateway-any-method:
      x-yc-apigateway-integration:
        type: http
        url: http://178.154.226.11:4000/{path}
        query:
          '*': '*'
        headers:
          Host: api.geekbrains.banzai-predict.site
          '*': '*'
        omitEmptyHeaders: true
        omitEmptyQueryParameters: true
      parameters:
      - name: path
        in: path
        required: false
        schema:
          type: string
EOT
}