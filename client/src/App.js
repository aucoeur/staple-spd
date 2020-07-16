import React from 'react';
import { HashRouter as Router, Route } from 'react-router-dom';

import Landing from './components/Landing/Landing'
import EditMarkdown from './components/EditMarkdown/EditMarkDown';
import Login from './components/Login/Login';

import Header from './components/Header/Header';
import Footer from './components/Footer/Footer';

import './App.css';

function App() {

  return (
    <Router>
      <div className="App">
        <Header logo="" companyName="staple"/>
        <Route exact 
          path='/'
          component={Landing}/>
        <Route path="/create" component= {EditMarkdown} />
        <Route path="/login" component= {Login} />
        <Footer />
      </div>
    </Router>
  )
}

export default App;
