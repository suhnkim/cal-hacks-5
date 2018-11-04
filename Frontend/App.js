import React, { Component } from 'react';
import { Link } from 'react-router';
import logo from './logomeet.svg';
import './App.css';

class App extends Component {
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <p>
            <br></br> Welcome to Meet My Professor
          </p>
          <button className = "button" id="login"> <code> Login </code> </button>
        </header>
      </div>
    );
  }
}

export default App;
