import clearskies
from clearskies.column_types import audit, belongs_to, created, datetime, email, string, updated, uuid
from clearskies.input_requirements import unique, required
import clearskies_auth_server
from clearskies_auth_server.column_types import password, tenant_id
from collections import OrderedDict
from . import audit_record, organization, role

class User(clearskies.Model):
    def __init__(self, memory_backend, columns, organizations, roles):
        super().__init__(memory_backend, columns)
        self._organizations = organizations
        self._roles = roles

    def _build_model(self):
        # the model is its own factory, so since we need some extra classes, we need to
        # pass those along when we build more user models.
        model_class = self.model_class()
        return model_class(self._backend, self._columns, self._organizations, self._roles)

    def columns_configuration(self):
        return OrderedDict([
            uuid("id"),
            tenant_id(
                "organization_id",
                parent_models_class=organization.Organization,
                source="authorization_data",
                source_key_name="organization_id",
            ),
            email('email', input_requirements=[required()]),
            password('password', input_requirements=[required()]),
            string('name', input_requirements=[required()]),
            string('reset_key'),
            datetime('reset_key_expiration'),
            belongs_to(
                "role",
                parent_models_class=role.Role,
                model_column_name="role_model",
            ),
            created('created_at'),
            updated('updated_at'),
            audit(
                "audit",
                audit_models_class=audit_record.AuditRecord,
                exclude_columns=["password"],
            ),
        ])

    def pre_save(self, data):
        # if the user doesn't exist and we have no organization id in the data, then we must
        # be registering as a new tenant admin.
        if not self.exists and not data.get('organization_id'):
            data = {
                **data,
                **self.setup_new_organization(data.get("name") + "'s organization"),
            }
        return data

    def setup_new_organization(self, name):
        """ Create a new organization when a user is registering as the admin of a new org. """
        new_organization = self._organizations.create({
            "name": name,
        })

        # find the default admin role
        admin_role = self._roles.find("name=Admin")
        if not admin_role:
            raise ValueError("Huh, the default admin role doesn't exist :(")

        return {
            "organization_id": new_organization.id,
            "role": admin_role.name,
        }
