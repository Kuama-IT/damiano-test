import datetime
import uuid

class SingTodo:
    id = ""
    text = ""
    dueDate = datetime.datetime.now()
    completed = False

    def __init__(self, text):
        self.id = uuid.uuid4()
        self.text = text

    def complete(self):
        self.completed = True