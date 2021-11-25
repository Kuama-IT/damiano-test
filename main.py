from singTodo import SingTodo

todoList = []

def listTodo():
    for singleTodo in todoList:
        if singleTodo.completed:
            print("id:"+singleTodo.id+" - desc:"+singleTodo.text+" - dueDate:"+singleTodo.dueDate+"\n")


def createTodo():
    desc = input("Digita la descrizione: ")
    todoList.append(SingTodo(desc))


def completeTodo():
    listTodo()
    id = input("Quale todo vuoi completare? ")
    singleTd = next(x for x in todoList if x.id == id)
    if singleTd:
        singleTd.complete()
        print("todo completato \n")
    else:
        print("elemento non trovato: \n")


def main():
    while(True):
        print("digita 1-lista todo, 2-creazione todo, 3-completa todo, 99 - termina esecuzione\n")
        x = input("Scegli l'operazione da eseguire: ")
        match x:
            case 1:
                listTodo()
            case 2:
                createTodo()
            case 3:
                completeTodo()
            case 99:
                break
            case _:
                print("comando non riconosciutos")


if __name__ == "__main__":
    main()
