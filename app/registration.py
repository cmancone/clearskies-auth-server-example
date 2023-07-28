import clearskies
import clearskies_auth_server
from . import models

registration = clearskies.Application(
    clearskies.handlers.SimpleRouting,
    {
        "authentication": clearskies.authentication.public(),
        "routes": [
            # This route is used when a user registers to a tenant
            {
                "path": "/register/{organization_id}",
                "request_method": "POST",
                "handler_class": clearskies.handlers.Create,
                "handler_config": {
                    "model_class": models.User,
                    "writeable_columns": ["email", "password", "name"],
                    "readable_columns": ["id", "email", "name"],
                    "column_overrides": {
                        "organization_id": {
                            "source": "routing_data",
                            "source_key_name": "organization_id",
                        },
                        "email": {
                            # the email is not marked as unique in the base model because it mucks with the login process
                            "input_requirements": [clearskies.input_requirements.unique()],
                        }
                    }
                },
            },
            # this route is used when a user registers a brand new tenant
            {
                "path": "/register_tenant",
                "request_method": "POST",
                "handler_class": clearskies.handlers.Create,
                "handler_config": {
                    "model_class": models.User,
                    "writeable_columns": ["email", "password", "name"],
                    "readable_columns": ["id", "organization_id", "email", "name"],
                    "column_overrides": {
                        # organization is normally of type "tenant_id" which has lots of behavior associated
                        # with it to identify the user's organization based on their JWT.  In the case of the
                        # initial tenant creation, we can't do any of that of course.  Therefore, we change the
                        # column class to "String" to disable all of that.  The model will take care of the
                        # initial tenant creation.
                        "organization_id": {
                            "class": clearskies.column_types.String,
                        },
                    },
                },
            },
        ]
    }
)
