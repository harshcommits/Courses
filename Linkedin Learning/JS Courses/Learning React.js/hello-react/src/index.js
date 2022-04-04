import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';

/*
let city = {
  name: "Madrid",
  country: "Spain"
}
*/

function Lake({name}) {
  return (
    <div>
      <h1>Visit {name}</h1>
    </div>
  );
}

/*
const lakeList = [
  "Echo Lake",
  "Maud Lake",
  "Cascade Lake"
]
*/

function SkiResort({name}) {
  return (
    <div>
      <h1>
        Visit {name}!
      </h1>
    </div>
  )
}

/*
const lakeList = [
  { id: "1", name: "Echo", trailhead: "Echo" },
  { id: "2", name: "Maud", trailhead: "Wrights" },
  { id: "3", name: "Velma", trailhead: "Bayview" }
]
*/

/*
function Lake({ name }) {
  return<h1>{name}</h1>
}
*/
 /*
function App({ lakes }) {
  return (
    <div>
      {lakes.map(lake => (
      <div key={lake.id}>
      <h2>{lake.name}</h2>
      <p>Accessed by: {lake.trailhead}</p>
      </div>
      ))}
    </div>);
}
*/

//can be written using ternary operators; need more reading
function App(props) {
  if (props.season === "summer") {
    return <Lake name="Jenny Lake"/>;
  } else if (props.season === "winter") {
    return <SkiResort name="JHMR"/>;
  }
}



/*
function Hello(props) {
  console.log(Object.keys(props));
  return (
  <div>
    <h1 id="heading">Welcome to {props.library}!</h1>
    <p>{props.message}</p>
    <p>{props.number} Props in total</p>
  </div>
  );
}
*/

ReactDOM.render(
  
  <App season="winter" />,
  document.getElementById('root')
);
