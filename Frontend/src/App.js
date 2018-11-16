import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import { Button, ButtonGroup, ButtonDropdown, DropdownItem } from 'reactstrap'
import Home from './home.js';
import Filters from './filters.js';
import {BrowserRouter, Route} from 'react-router-dom';
import ApiCalendar from 'react-google-calendar-api';


class App extends Component {
  render() {
    return (
      <BrowserRouter>
        <div className="App">
          <Route exact path="/" component={Home} />
          <Route path="/filters" component={Filters} />
        </div>
      </BrowserRouter>
    );
  }
}
export default App;

/*<ButtonGroup  className="App-link">
  <Button>Classes</Button>
  <Button>Departments</Button>
  <ButtonDropdown title="Dropdown">
    <DropdownItem eventKey="1">Dropdown link</DropdownItem>
    <DropdownItem eventKey="2">Dropdown link</DropdownItem>
  </ButtonDropdown>
</ButtonGroup>*/
