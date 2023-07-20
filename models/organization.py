import clearskies
from clearskies.column_types import uuid, string, created, updated, many_to_many
from clearskies.input_requirements import required
from collections import OrderedDict
from . import user, user_organization

class Organization(clearskies.Model):
    def __init__(self, memory_backend, columns):
        super().__init__(memory_backend, columns)

    def columns_configuration(self):
        return OrderedDict([
            uuid('id'),
            string('name', input_requirements=[required()]),
            string('description'),
            created('created_at'),
            updated('updated_at'),
            many_to_many(
                "users",
                pivot_models_class=user_organization.UserOrganization,
                related_models_class=organization.Organization,
            ),
        ])
