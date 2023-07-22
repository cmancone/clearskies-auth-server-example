import clearskies
from . import models

roles = clearskies.Application(
    clearskies.handlers.SimpleRouting,
    {
        "authentication": clearskies.authentication.public(),
        "routes": [
            {
                "path": "/roles",
                "handler_class": clearskies.handlers.RestfulAPI,
                "handler_config": {
                    "model_class": models.Role,
                    "writeable_columns": ["name", "description"],
                    "readable_columns": ["id", "name", "description", "created_at", "updated_at"],
                    "searchable_columns": ["id", "name"],
                    "default_sort_column": "name",
                },
            },
        ]
    }
)
