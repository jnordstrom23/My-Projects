import React from 'react';
import{HashRouter, Route, Routes} from'react-router-dom'
import './App.css';
import Navigation from './Components/Navigation';
import Footer from './Components/Footer';
import Home from './Components/Home';
import Cart from './Components/Cart';
import Order from './Components/Order';
import Header from './Components/Header'
import Complete from './Components/Complete'



function App() {

  return (
    <HashRouter>
      <Header/>
      <Navigation/>
      <Routes>
          <Route path ="/" element={<Home/>} />
      </Routes>
      <Routes>
          <Route path ="/Menu" element={<Order/>} />
          <Route path ="/Cart" element={<Cart/>} />
          <Route path ="/Complete" element={<Complete/>} />
        </Routes>
      <Footer/>
    </HashRouter>
  );
}

export default App;
