import React, {useState, useEffect} from "react";
import { Link, Switch, Route, BrowserRouter } from "react-router-dom";
import About from "./About";
import NavBar from "./NavBar";

//remember to set proxy for the backend server!!


function Generate() {
  const [eboards, setEboards] = useState([])
  const [query, setQuery] = useState("")




  return (
    <BrowserRouter>
      <main>
        <NavBar/>
        <Switch>
            <Route exact path="/">
                <About />
            </Route>
            <Route path="/ ___ ">

            </Route>
            <Route path="/ ___ ">

            </Route>
        </Switch>
      </main>
    </BrowserRouter>
  )
}

export default Generate
