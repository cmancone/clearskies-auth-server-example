import clearskies
from . import models

roles = clearskies.Application(
    clearskies.handlers.SimpleRouting,
    {
        "routes": [
            {
                "path": "/roles",
                "handler_class": clearskies.handlers.RestfulAPI,
                "handler_config": {
                    "authentication": clearskies.authentication.public(),
                    "model_class": models.Role,
                    "writeable_columns": ["name", "description"],
                    "readable_columns": ["name", "description", "created_at", "updated_at"],
                    "searchable_columns": ["name"],
                    "default_sort_column": "name",
                },
            },
        ]
    }
)
