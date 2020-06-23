import React from 'react';
import './App.css';
import DisplayMarkdown from './components/DisplayMarkdown/DisplayMarkDown';
import Header from './components/Header/Header';
import Footer from './components/Footer/Footer';

function App() {

  return (
    <div className="App">
      <Header logo="" companyName="test"/>
      <DisplayMarkdown />
      <Footer />
    </div>
  )
}

export default App;
