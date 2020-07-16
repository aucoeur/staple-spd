import React, { useState, useEffect } from 'react'
import { NavLink } from 'react-router-dom';
import './Header.css'
// import ModalButton from '../Modal/ModalButton.js'

function Header(props) {
    const { logo, companyName } = props

    // const [ json, setJSON ] = useState('')

    // useEffect(() => {
    //     fetch('/create')
    //     .then((res) => {
    //         return res.json()
    //     })
    //     .then((text) => {
    //         setJSON(text.hello)
    //     })
    // })

    return (
        <div className="header">
            <div className="badge">
                <div className="logo">{logo}</div>
                <h1>{companyName}</h1>
            </div>

            <div className="authButtons">
                <NavLink to='/create'>
                    <input type="button" value="New File" />
                </NavLink>
                <NavLink to='/login'>
                    <input type="button" value="Login" />
                </NavLink>
                <input type="button" value="Sign Up" />
            </div>
        </div>
    )
}

export default Header;