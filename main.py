from singTodo import SingTodo

todoList = []

def listTodo():
    for singleTodo in todoList:
        if singleTodo.completed:
            print("id:"+singleTodo.id+" - desc:"+singleTodo.text+" - dueDate:"+singleTodo.dueDate+"\n")


def createTodo():
    desc = input("Digita la descrizione: ")
    todoList.append(SingTodo(desc))


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
                return "I'm a teapot"
            case 99:
                break
            case _:
                print("comando non riconosciutos")


if __name__ == "__main__":
    main()
