import React, { Component } from 'react';

class Results extends Component {
    render() {
    return (
      <div className="App">
        <header className="App-header">
        <img src={logo} className="App-logo-subpages" alt="logo" />
        <button className = "button-subpages" id="login"> <code> Home </code> </button>
          <p className="pStyle">
            Your results
          </p>
        </header>
      </div>
    );
  }
}

/*constructor(props) {
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
}*/


