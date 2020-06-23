import React from 'react'
import './Header.css'

function Header(props) {
    const { logo, companyName } = props

    return (
        <div className="header">
            <div className="badge">
                <div className="logo">{logo}</div>
                <div>{companyName}</div>
            </div>

            <div className="authbuttons">
                <button>Login</button>
                <button>Log Out</button>
            </div>
        </div>
    )
}

export default Header