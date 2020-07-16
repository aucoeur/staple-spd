import React, { Component } from 'react'
import Modal from './Modal.js'
// Used this tutorial. https://blog.bitsrc.io/build-a-simple-modal-component-with-react-16decdc111a6
// TODO: Convert to function component and use hooks
class ModalButton extends Component {
    constructor(props){
        super(props)

        this.state = {
            display: false
        }
    }

    displayModal() {
        this.setState(
            {display: true}
        )
    }

    closeModal() {
        this.setState(
            {display: false}
        )
    }

    render() {
        return (
            <div>
                <button onClick={ () => this.displayModal()}> Login </button>

                {this.state.display ? <Modal content="test" onChange={this.closeModal}/> : undefined}
            </div>
        )

    }
}

export default ModalButton