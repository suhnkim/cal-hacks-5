import React, { Component } from 'react';
import { Link } from 'react-router';
import logo from './logo.svg';
import './App.css';
import ApiCalendar from 'react-google-calendar-api';

//this is the homepage for Meet My Professor

class Home extends Component {
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <p>
            <br></br> Welcome to Meet My Professor
          </p>
          <button className = "button" id="login"> <code> Log In </code> </button>

        </header>
      </div>
    );
  }
}

export default Home;

// export default class Home extends Component {
//    state = {
//    }
//    render () {
//       return (
//         <div id='container'>
//            <a href="home">Filters</a>
//         </div>
//       )
//    }
// }


{/*<a className="App-link" href="https://meetyourprofessor.berkeley.edu" target="_blank" rel="noopener noreferrer">
      Learn React </a> */}
