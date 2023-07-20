import clearskies_aws
import clearskies_auth_server
import models

auth_service = clearskies_aws.contexts.wsgi(
    {
        "handler_class": clearskies.handlers.SimpleRouting,
        "handler_config": {
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
                        "claims_column_names": ["email"],
                    },
                },
                {
                    "path": ".well-known/jwks.js",
                    "handler_class": clearskies_auth_server.handlers.Jwks,
                    "handler_config": {
                        "path_to_public_keys": "/auth/test/public_keys",
                    },
                }
            ]
        }
    },
    bindings={
        "secrets": clearskies_aws.secrets.SecretsManager,
    },
    binding_modules=[models],
)
def application(env, start_response):
    return auth_service(env, start_response)
