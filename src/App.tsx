import React from 'react';
import { Homepage } from './components/Homepage';
import './App.scss';
import { BrowserRouter as Router, Route, Switch, Link} from "react-router-dom";
import { CarList } from './components/CarList';
import brandlogo from "./brand.svg"
import { CarDetails } from './components/CarDetails';
// import {CarCustomisation} from './components/CarCustomisation'

function App() {
  return (
    <Router>
    <div className="App">
      <section>
        <Link to="/">
          <img src={brandlogo} alt="brand logo" className="brand-logo" />
        </Link>
        <Switch>
          <Route exact path="/">
            <Homepage />
          </Route>
          <Route exact path="/cars">
            <CarList />
          </Route>
          <Route exact path="/cars/:id">
            <CarDetails />
          </Route>
          {/* <Route exact path="/car/:id/customise">
            <CarCustomisation/>
          </Route> */}
        </Switch>
      </section>
    </div>
    </Router>
  );
}

export default App;
