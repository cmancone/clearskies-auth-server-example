from collections import OrderedDict

import clearskies
from clearskies import Model
from clearskies.column_types import created, json, string, uuid


class AuditRecord(Model):
    def __init__(self, memory_backend, columns):
        super().__init__(memory_backend, columns)

    def columns_configuration(self):
        return OrderedDict(
            [
                uuid("id"),
                string("class"),
                string("resource_id"),
                string("action"),
                json("data"),
                created("created_at"),
            ]
        )
