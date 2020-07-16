import React from 'react';
import './App.css';
import Landing from './components/Landing/Landing'
import EditMarkdown from './components/EditMarkdown/EditMarkDown';
import Header from './components/Header/Header';
import Footer from './components/Footer/Footer';

function App() {

  return (
    <div className="App">
      <Header logo="" companyName="test"/>
      <Landing />
      <EditMarkdown />
      <Footer />
    </div>
  )
}

export default App;
