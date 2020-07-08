import React, { useState, useEffect } from 'react'
import './Header.css'
import ModalButton from '../Modal/ModalButton.js'

function Header(props) {
    const { logo, companyName } = props

    const [ test, setTest ] = useState('')
    useEffect(() => {
        fetch('/test')
        .then((res) => {
            return res.json()
        })
        .then( (text) => {
            setTest(text.hello)
        })
    })

    return (
        <div className="header">
            <div className="badge">
                <div className="logo">{logo}</div>
                <h1>{companyName}</h1>
                <span>Test: {test}</span>
            </div>

            <div className="authButtons">
                <input type="button" value="Login" />
                <input type="button" value="Sign Up" />
            </div>
        </div>
    )
}

export default Header