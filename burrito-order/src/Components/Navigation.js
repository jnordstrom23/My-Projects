import React from 'react';
import {Link} from "react-router-dom"

function Navigation() {
    return (
      <div >
        <h1>
          <ul class="topnav">
    <li><Link to="/Home">
      <img src="https://static.vecteezy.com/system/resources/thumbnails/000/568/450/small/vector60-1781-01.jpg" 
        class="Home"
          alt="Home"/>
            </Link></li>
    <li><Link to="/Menu">Menu </Link></li>
    <li><Link to="/cart">
      <img src="https://www.citypng.com/public/uploads/preview/hd-shopping-cart-white-logo-icon-transparent-png-11640441682ecem2ohejv.png" 
        class="Cart"
          alt="/Cart"/>
            </Link></li>
        </ul>
      </h1>
    </div>
    );
  }
  
  export default Navigation;
  