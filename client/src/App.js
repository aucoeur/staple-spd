import React from 'react'
import './App.css'
import DisplayMarkdown from './components/DisplayMarkDown'
import Header from './components/Header/Header'

function App() {

  return (
    <div className="App">
      <Header logo="" companyName="test"/>
      <DisplayMarkdown />
    </div>
  );
}

export default App;
