from singTodo import SingTodo

todoList = []


def listTodo():
    for singleTodo in todoList:
        if not singleTodo.completed:
            print("id:" + str(singleTodo.id) + " - desc:" + singleTodo.text + " - dueDate:" + singleTodo.createDate.strftime("%x") + "\n")


def createTodo():
    desc = input("Digita la descrizione: ")
    todoList.append(SingTodo(desc))


def completeTodo():
    listTodo()
    id = input("Quale todo vuoi completare? ")
    singleTd = next(x for x in todoList if str(x.id) == id)
    if singleTd:
        singleTd.complete()
        print("todo completato \n")
    else:
        print("elemento non trovato: \n")


def main():
    while (True):
        print("digita 1-lista todo, 2-creazione todo, 3-completa todo, 99 - termina esecuzione\n")
        x = input("Scegli l'operazione da eseguire: ")
        if x == "1":
            listTodo()
        elif x == "2":
            createTodo()
        elif x == "3":
            completeTodo()
        elif x == "99":
            break
        else:
            print("comando non riconosciuto \n")


if __name__ == "__main__":
    main()
