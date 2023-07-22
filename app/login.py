import clearskies
import clearskies_auth_server
from . import models

login = clearskies.Application(
    clearskies.handlers.SimpleRouting,
    {
        "authentication": clearskies.authentication.public(),
        "routes": [
            {
                "path": "login",
                "handler_class": clearskies_auth_server.handlers.PasswordLogin,
                "handler_config": {
                    "user_model_class": models.user.User,
                    "issuer": "clearskies.auth.example.com",
                    "audience": "clearskies.auth.example.com",
                    "path_to_private_keys": "/auth/test/private_keys",
                    "path_to_public_keys": "/auth/test/public_keys",
                    "username_column_name": "email",
                    "password_column_name": "password",
                    "jwt_lifetime_seconds": 3600,
                    "claims_column_names": ["email"],
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
