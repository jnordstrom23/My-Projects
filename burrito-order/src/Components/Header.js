import {Link} from "react-router-dom"

function Header() {
    return (
      
        <header class="header">
            
   
       
       
       <li><Link to="/Home">
       <img src= "https://image.shutterstock.com/image-vector/authentic-burritos-vintage-restaurant-stamp-600w-557719639.jpg"
       class="header-image"
          alt="Home"/>
            </Link></li>   
            
       
          
        </header>
        );
      }


export default Header;
