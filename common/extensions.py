from drf_spectacular.extensions import OpenApiAuthenticationExtension


from .auth import BearerTokenAuthentication

class BearerTokenAuthenticationScheme(OpenApiAuthenticationExtension):
    target_class = BearerTokenAuthentication
    name = "BearerTokenAuthentication"

    def get_security_definition(self, auto_schema):
        return {
            "type": "http",
            "scheme": "bearer",
        }