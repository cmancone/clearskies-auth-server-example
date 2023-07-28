import clearskies
import clearskies_auth_server
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
        ]
    }
)
