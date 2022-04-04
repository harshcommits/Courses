import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';

let city = {
  name: "Madrid",
  country: "Spain"
}

function Hello(props) {
  console.log(Object.keys(props));
  return (
  <div>
    <h1 id="heading">Welcome to {props.library}!</h1>
    <p>{props.message}</p>
    <p>{props.number}</p>
  </div>
  );
}

ReactDOM.render(
  /*
  React.createElement(
    "h2", {style: { color: "blue" } }, "Hello!"
    */
   /*
   <h1 id="heading">Hello from {city.name}!</h1> //heading id allows using color change css used in index.html
   */
  <Hello 
    library="React" 
    message="Have fun!"
    number={3}
    />,
  document.getElementById('root')
);
