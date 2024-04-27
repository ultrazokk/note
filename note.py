import json
import datetime

class Note:
    def __init__(self, title, body, id=None):
        self.id = id or datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        self.title = title
        self.body = body
        self.created_at = datetime.datetime.now()
        self.updated_at = self.created_at

    def update(self, title=None, body=None):
        if title:
            self.title = title
        if body:
            self.body = body
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'body': self.body,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }    