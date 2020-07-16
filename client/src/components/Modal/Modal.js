import React from 'react'

function Modal(props){
    const { content, onChange } = props

    return(
        <div>
            <h2>Modal Window</h2>
            <div>{content}</div>
            <button onClick={onChange}> close </button>
        </div>
    )

}

export default Modal