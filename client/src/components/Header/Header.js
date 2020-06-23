import React from 'react'
import './Header.css'
import ModalButton from '../Modal/ModalButton.js'

function Header(props) {
    const { logo, companyName } = props

    return (
        <div className="header">
            <div className="badge">
                <div className="logo">{logo}</div>
                <div>{companyName}</div>
            </div>

            <div className="authbuttons">
                <ModalButton />
                <button>Login</button>
                <button>Sign Up</button>
            </div>
        </div>
    )
}

export default Header