import { useEffect, useState } from "react"
import SingleTodo from "./SingleTodo"

export default function TodoList() {

    const [todoList, setTodoList] = useState([]) // state to hold todolist
    const [newTodo, setNewTodo] = useState("") // state for new todo



    // function to add new todo to existing todo list state and update localstorage for keeping data persistent
    const addNewTodo = () => {
        if(newTodo !== ""){
            setTodoList((prev) => [...prev, {todo:newTodo, completed: false}])
            setNewTodo("")
        }
        
    }

    // function to change todo status
    const changeTodoStatus = (index) => {
        
        let newTodolist = [...todoList]
        newTodolist[index] = { ...newTodolist[index], completed: !newTodolist[index].completed}

        setTodoList(newTodolist)
    }


    // UseEffect to get saved todos from browser's localstorage otherwise an empty array
    useEffect(() => {
        const todos = localStorage.getItem("todos")
        setTodoList(JSON.parse(todos) || []);
        return () => {
        }
    }, [])


    // save updated todo list to browser's localstorage
    useEffect(() => {
        saveTodosToLocalStorage(todoList)
        return () => {
            // cleanup
        }
    }, [todoList])


    // function to save updated todos
    const saveTodosToLocalStorage = (todoList) => {
        localStorage.setItem("todos", JSON.stringify(todoList))
    }

    return (
        <div>
            <h1 className="text-center mt-5" >Todo List</h1>
            <input type="text" className="form-control" id="newTodo" placeholder="New Todo" onChange={(event) => setNewTodo(event.target.value)} value={newTodo} />
            <button type="submit" className="btn btn-primary mb-5 mt-2" onClick={addNewTodo}>Add Todo</button>           
            {
                (todoList.length > 0) ?
                <table className="table table-striped">
                    <thead className="table-dark">
                        <tr>
                            <th scope="col" className="col-md-1">#</th>
                            <th scope="col" className="col-md-8">Todo</th>
                            <th scope="col" className="col-md-3">Action</th>
                        </tr>
                    </thead>
                    <tbody>
                        {
                            // Iterate todoList state array to render singletodo component
                            todoList.map((singleTodo, index) => (
                                <SingleTodo key={index} todo={singleTodo.todo} index={index} completed={singleTodo.completed} changeTodoStatus={changeTodoStatus} />
                            ))
                        }
                    </tbody>
                </table>
                : <h3>There are todos currently</h3>
            }
        </div>
    )
}
