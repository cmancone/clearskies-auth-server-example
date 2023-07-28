import clearskies
from clearskies.column_types import uuid, string, created, updated
from clearskies.input_requirements import required, unique
from collections import OrderedDict

class Role(clearskies.Model):
    def __init__(self, memory_backend, columns):
        super().__init__(memory_backend, columns)

    id_column_name = 'name'

    def columns_configuration(self):
        return OrderedDict([
            string('name', input_requirements=[required(), unique()]),
            string('description'),
            created('created_at'),
            updated('updated_at'),
        ])
