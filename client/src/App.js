import React from 'react';
import './App.css';
import Header from './components/Header/Header';
import DisplayMarkdown from './components/DisplayMarkdown/DisplayMarkDown';

function App() {

  return (
    <div className="App">
      <Header logo="" companyName="test"/>
      <DisplayMarkdown />
    </div>
  );
}

export default App;
