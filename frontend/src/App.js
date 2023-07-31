import {
    BrowserRouter as Router,
    Routes,
    Route
  } from "react-router-dom";

import './App.css';


import Home from './components/Home';
import Results from './components/Results';



function App() {

  return (
    <div className="App">
        <>
        <Router>
            <Routes>
            
                <Route path='/' element={<Home/>} />
                    
                <Route path='/results' element={<Results/>} />
                    
            </Routes>
        </Router>
        </>
    </div>
  );
}


export default App;