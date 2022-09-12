import React from 'react';
import './App.css';
import { Link }from 'react-router-dom';

function Nav() {
    const navstyle = {
        color: 'black'
    }
    return(
      <nav>
        <h3>
            <Link style={navstyle}to='/'>
                <li>
                    <img src = "http://burritobuilders.letseat.at/system/business_logos/17737/original/5aac016782ab663fdb9e.jpg?1384665485"
                    width='175'
                    height='125'
                    />
                </li>
            </Link>
        </h3>
        <ul className='nav-links'>
            <Link style={navstyle}to='/about'>
                <li>About</li>
            </Link>
            <Link style={navstyle}to ='/shop'>
                <li>Shop</li>
            </Link>
        </ul>
      </nav>
    );
  }
  
  export default Nav;