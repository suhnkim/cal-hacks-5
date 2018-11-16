import React, { Component } from 'react';
import './App.css';
import logo from './logo.svg';
import { Button, ButtonGroup, ButtonDropdown, DropdownItem } from 'reactstrap'
import ApiCalendar from 'react-google-calendar-api';

class Filters extends Component{
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <p>
            Select your filters
          </p>
          <ButtonGroup className="button">
            <ButtonDropdown title="Dropdown">
              <DropdownItem eventKey="1">Research</DropdownItem>
              <DropdownItem eventKey="2">Classes</DropdownItem>
              <DropdownItem eventKey="3">Departments</DropdownItem>
              <DropdownItem eventKey="4">Interests</DropdownItem>
              <DropdownItem eventKey="5">Times</DropdownItem>
            </ButtonDropdown>
          </ButtonGroup>
        </header>
      </div>
    );
  }
}

export default Filters;

// export default class Home extends Component {
//    state = {
//    }
//    render () {
//       return (
//         <div id='container'>
//            <a href="filters">Filters</a>
//         </div>
//       )
//    }
// }
