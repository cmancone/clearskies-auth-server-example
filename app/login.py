import clearskies
import clearskies_auth_server
from . import models

login = clearskies.Application(
    clearskies.handlers.SimpleRouting,
    {
        "authentication": clearskies.authentication.public(),
        "routes": [
            {
                "path": "/organizations/{organization_id}/login",
                "handler_class": clearskies_auth_server.handlers.PasswordLogin,
                "handler_config": {
                    "user_model_class": models.user.User,
                    "issuer": "clearskies.auth.example.com",
                    "audience": "clearskies.auth.example.com",
                    "path_to_private_keys": "/auth/test/private_keys",
                    "path_to_public_keys": "/auth/test/public_keys",
                    "username_column_name": "email",
                    "password_column_name": "password",
                    "tenant_id_column_name": "organization_id",
                    "tenant_id_source": "routing_data",
                    "tenant_id_source_key_name": "organization_id",
                    "jwt_lifetime_seconds": 3600,
                    "claims_column_names": ["email", "role_id", "organization_id"],
                },
            },
            {
                "path": ".well-known/jwks.json",
                "handler_class": clearskies_auth_server.handlers.Jwks,
                "handler_config": {
                    "path_to_public_keys": "/auth/test/public_keys",
                    "path_to_private_keys": "/auth/test/private_keys",
                },
            }
        ]
    }
)
