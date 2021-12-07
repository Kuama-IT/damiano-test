import React from 'react'

export default function SingleTodo({todo, index, completed, changeTodoStatus}) {
    
    return (
        <tr>
            <th scope="row">{index+1}</th>
            <td className={(!completed)? "incomplete": "complete"}>{todo}</td>
            <td>
            <button 
                type="button" 
                className="btn btn-primary mb-2" 
                onClick={() => changeTodoStatus(index)} >
                    Mark as {(completed)? "incomplete": "complete"}
                </button>
            </td>
        </tr>
    )
}
