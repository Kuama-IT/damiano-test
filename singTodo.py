import datetime

class SingTodo:
    id = 0
    text = ""
    createDate = datetime.datetime.now()
    dueDate = datetime.datetime.now()

    def __init__(self, id, text, dueDate):
        self.id = id
        self.text = text
        self.dueDate = dueDate