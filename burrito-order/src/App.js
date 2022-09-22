import React from 'react';
import{BrowserRouter as Router, Route, Routes} from'react-router-dom'
import './App.css';
import Navigation from './Components/Navigation';
import Footer from './Components/Footer';
import Home from './Components/Home';
import Cart from './Components/Cart';
import Order from './Components/Order';



function App() {

 

  return (
    <Router>
      <Navigation/>
        <Routes>
          <Route path ="/" element={<Home/>} />
          <Route path ="/Order" element={<Order/>} />
          <Route path ="/Cart" element={<Cart/>} />
        </Routes>
      <Footer/>
    </Router>
  );
}

export default App;
