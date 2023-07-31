import clearskies
from . import models
from .self_authenticate import self_authenticate
from .authorization import is_admin

users = clearskies.Application(
    clearskies.handlers.SimpleRouting,
    {
        "routes": [
            {
                "path": "/users",
                "handler_class": clearskies.handlers.RestfulAPI,
                "handler_config": {
                    "authentication": self_authenticate,
                    # the organization_id column attached to the user will automatically filter user records to
                    # the ones for our org, so all we have to do is limit access to people with the admin role.
                    "authorization": is_admin(),
                    "model_class": models.User,
                    # for security reasons we don't want admins to be able to change email or password
                    "writeable_columns": ["name", "role"],
                    "readable_columns": ["id", "name", "email", "created_at", "updated_at"],
                    "searchable_columns": ["name", "role", "email"],
                    "default_sort_column": "name",
                },
            },
        ]
    }
)
