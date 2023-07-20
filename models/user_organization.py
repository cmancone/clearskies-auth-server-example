import clearskies
from clearskies.column_types import uuid, belongs_to, many_to_many
from collections import OrderedDict
from . import user, organization, user_organization_role, role

class UserOrganization(clearskies.Model):
    def __init__(self, memory_backend, columns):
        super().__init__(memory_backend, columns)

    def columns_configuration(self):
        return OrderedDict([
            uuid('id'),
            belongs_to("user_id", parent_models_class=user.User),
            belongs_to("organization_id", parent_models_class=organization.Organization),
            many_to_many(
                "roles",
                pivot_models_class=user_organization_role.UserOrganizationRole,
                related_models_class=role.Role,
            )
        ])
