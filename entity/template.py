from dataclasses import dataclass
from datetime import datetime
import uuid
from enum import Enum

@dataclass(frozen=True)
class template_info:

    template_name : str
    subject : str
    body : str
    template_id : str = None
    creation_datetime:datetime = None

    def __post_init__(self):
        if not self.template_id:
            object.__setattr__(self, "template_id", str((uuid.uuid4()).hex))
        if not self.creation_datetime:
            object.__setattr__(self, "creation_datetime", datetime.now())



    @staticmethod
    def from_json(json):
        return template_info(**json)


    def to_json(self):
        payload={
            "template_id":self.template_id,
            "template_name":self.template_name,
            "subject":self.subject,
            "body":self.body,
            "creation_datetime":str(self.creation_datetime)
        }
        return payload

