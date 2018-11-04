import React, { Component } from 'react';

class Results extends Component {
  render() {
  	//test case
  	constructor(props) {
    super(props);
    this.state = {
      items: {"a":3, "b":4, "c":5}
    };
  }
  render() {
    return (
      <div className="App">
        <header className="App-header">{
         Object.keys(this.state.items).map((k, i) => {
          return <p key={k}> this is my key {k} and this is my value {this.state.items[k]}</p> 
        })
      }
        </header>
      </div>
    );
  }
}


