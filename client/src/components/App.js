import React, { useEffect } from 'react';
import './App.css';
import Generate from './Generate';
import Header from './Header';


function App() {
  const [user, setUser] = useState  ({});
  const [currentUser, setCurrentUser] = useState({});


  useEffect(() => {
    fetch("/check_session")
    .then((data) => {
      if (data.ok) {
        data.json().then((user) => setCurrentUser(user));
      }
    })
  }, [])


  return (
    <div className="app">
    <BrowserRouter>
      <Header />
      <main>
        <NavBar/>
        <Switch>
            <Route exact path="/">
                <Login 
                setUser={setUser}
                user = {user}
                />
            </Route>
            <Route path="/home">

            </Route>
            <Route path="/ ___ ">

            </Route>
        </Switch>
      </main>
    </BrowserRouter>
    </div>
  );
}

export default App;
