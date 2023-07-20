import clearskies
from clearskies.column_types import uuid, belongs_to
from collections import OrderedDict
from . import user, organization, role

class UserOrganizationRole(clearskies.Model):
    def __init__(self, memory_backend, columns):
        super().__init__(memory_backend, columns)

    def columns_configuration(self):
        return OrderedDict([
            uuid('id'),
            belongs_to("user_id", parent_models_class=user.User),
            belongs_to("organization_id", parent_models_class=organization.Organization),
            belongs_to("role_id", parent_models_class=role.Role),
        ])
