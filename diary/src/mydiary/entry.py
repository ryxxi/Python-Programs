import random
import time
from datetime import datetime

generated_ids = []

class Entry:

    id = None
    title = None
    body = None
    creation_date = None

    def __init__(self, title, body):
        self.title = title
        self.body = body
        self.id = self.generate_id()
        self.creation_date = datetime.now()

    def generate_id(self):
        while True:
            generated_id = random.randint(100000, 999999)
            if generated_id not in generated_ids:
                generated_ids.append(generated_id)
                return generated_id

    def get_id(self):
        return self.id

    def get_title(self):
        return self.title

    def get_body(self):
        return self.body

    def type_entry(self):
        self.body = input("Type entry:\n")