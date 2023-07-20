import clearskies
from clearskies.column_types import audit, email, created, updated
from clearskies_auth_server.column_types import password
from collections import OrderedDict
from . import audit_record, user_organization, organization

class User(clearskies.Model):
    id_column_name = 'email'

    def __init__(self, memory_backend, columns):
        super().__init__(memory_backend, columns)

    def columns_configuration(self):
        return OrderedDict([
            email('email'),
            password('password'),
            created('created_at'),
            updated('updated_at'),
            many_to_many(
                "organizations",
                pivot_models_class=user_organization.UserOrganization,
                related_models_class=organization.Organization,
            ),
            audit(
                "audit",
                audit_models_class=audit_record.AuditRecord,
                exclude_columns=["password"],
            ),
        ])
