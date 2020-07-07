import React from 'react'
import './Header.css'
import ModalButton from '../Modal/ModalButton.js'

function Header(props) {
    const { logo, companyName } = props

    return (
        <div className="header">
            <div className="badge">
                <div className="logo">{logo}</div>
                <h1>{companyName}</h1>
            </div>

            <div className="authButtons">
                <input type="button" value="Login" />
                <input type="button" value="Sign Up" />
            </div>
        </div>
    )
}

export default Header