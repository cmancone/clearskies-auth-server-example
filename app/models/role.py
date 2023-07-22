import clearskies
from clearskies.column_types import uuid, string, created, updated
from clearskies.input_requirements import required
from collections import OrderedDict

class Role(clearskies.Model):
    def __init__(self, memory_backend, columns):
        super().__init__(memory_backend, columns)

    def columns_configuration(self):
        return OrderedDict([
            uuid('id'),
            string('name', input_requirements=[required()]),
            string('description'),
            created('created_at'),
            updated('updated_at'),
        ])
