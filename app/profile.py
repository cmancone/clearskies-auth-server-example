import clearskies
import clearskies_auth_server
from clearskies_auth_server.input_requirements import password_validation
from . import models
from .self_authenticate import self_authenticate

profile = clearskies.Application(
    clearskies.handlers.SimpleRouting,
    {
        "authentication": self_authenticate,
        "routes": [
            {
                "path": "/profile/my-organizations",
                "handler_class": clearskies.handlers.List,
                "handler_config": {
                    "model_class": models.organization.Organization,
                    "readable_columns": ["id", "name"],
                    "searchable_columns": ["id", "name"],
                    "default_sort_column": "name",
                },
            },
            {
                "path": "/profile",
                "request_method": "POST",
                "handler_class": clearskies_auth_server.handlers.Profile,
                "handler_config": {
                    "model_class": models.user.User,
                    "user_id_key_in_authorization_data": "id",
                    "writeable_columns": ["name", "email", "password"],
                    "readable_columns": ["id", "name", "email"],
                    "column_overrides": {
                        "email": {"input_requirements": [password_validation("password")]},
                        "password": {"input_requirements": [password_validation("password")]},
                    }
                },
            },
        ]
    }
)
