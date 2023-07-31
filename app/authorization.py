from clearskies import BindingConfig
from clearskies.authentication import Authorization

def is_admin():
    return BindingConfig(IsAdmin)

class IsAdmin(Authorization):
    def configure(self):
        pass

    def gate(self, authorization_data, input_output):
        return authorization_data.get("role") == "Admin"
