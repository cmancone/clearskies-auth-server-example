import clearskies
import clearskies_auth_server
from . import models
from .self_authenticate import self_authenticate

login_configuration = {
    "authentication": clearskies.authentication.public(),
    "user_model_class": models.user.User,
    "issuer": "clearskies.auth.example.com",
    "audience": "clearskies.auth.example.com",
    "path_to_private_keys": "/auth/test/private_keys",
    "path_to_public_keys": "/auth/test/public_keys",
    "username_column_name": "email",
    "tenant_id_column_name": "organization_id",
    "tenant_id_source": "routing_data",
    "tenant_id_source_key_name": "organization_id",
    "claims_column_names": ["id", "email", "role", "organization_id"],
}

login = clearskies.Application(
    clearskies.handlers.SimpleRouting,
    {
        "routes": [
            {
                "path": "/reset_request/{organization_id}",
                "handler_class": clearskies_auth_server.handlers.PasswordResetRequest,
                "handler_config": {
                    # there are more config options here but we've named our columns to match
                    # the defaults for the handler, so no need to
                    "user_model_class": models.user.User,
                    "where": lambda users, routing_data: users.where(f"organization_id=" + routing_data.get("organization_id")),
                }
            },
            {
                "path": "/reset/{reset_key}",
                "handler_class": clearskies_auth_server.handlers.PasswordReset,
                "handler_config": {
                    # there are more config options here but we've named our columns to match
                    # the defaults for the handler, so no need to
                    "user_model_class": models.user.User,
                    "readable_columns": ["id", "email"],
                    "column_overrides": {
                        "organization_id": {"class": clearskies.column_types.String},
                    }
                }
            },
            {
                "path": "/login/switch/{organization_id}",
                "handler_class": clearskies_auth_server.handlers.SwitchTenant,
                "handler_config": {
                    **login_configuration,
                    **{
                        "authentication": self_authenticate,
                        "username_key_name_in_authorization_data": "email",
                    },
                },
            },
            {
                # this endpoint allows a user to login directly to an org and returns a JWT which
                # already has the organization id baked into it.
                "path": "/login/{organization_id}",
                "handler_class": clearskies_auth_server.handlers.PasswordLogin,
                "handler_config": {
                    **login_configuration,
                    **{
                        "jwt_lifetime_seconds": 3600,
                        "password_column_name": "password",
                    }
                },
            },
            {
                # this endpoint allows a user to login "generically" without an organization id.
                # they will get a JWT without an organization id in it, which means that they will
                # need to use the "switch" endpoint to swap it out for a JWT with an organization id
                # before they can do much.  This supports usage flows where someone logs into an app
                # and then is allowed to select which organization to work with (in cases where a single
                # user may have accounts with multiple organizations).
                "path": "/login",
                "handler_class": clearskies_auth_server.handlers.PasswordLogin,
                "handler_config": {
                    **login_configuration,
                    **{
                        "jwt_lifetime_seconds": 3600,
                        "password_column_name": "password",
                        "tenant_id_column_name": "",
                        "claims_column_names": ["id", "email", "role"],
                    },
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
