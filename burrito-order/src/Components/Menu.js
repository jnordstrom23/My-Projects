
import React from 'react';
import{useNavigate} from'react-router-dom'

function Menu() {

    const navigate = useNavigate();

    const navigateCart = () => {
        navigate('/cart');
    };



    return (
       
        <div class="card-container">

            <div class='card'>
                <div class='card-image'></div>
                <div class='card-title'>Beef</div>
                <div class='card-text'>$10.50</div>
                <button onClick={navigateCart}>Order Now</button>
            </div>
            <div class='card'>
                <div class='card-image'></div>
                <div class='card-title'>Chicken</div>
                <div class='card-text'>$10.00</div>
                <button onClick={navigateCart}>Order Now</button>
            </div>
            <div class='card'>
                <div class='card-image'></div>
                <div class='card-title'>Bean</div>
                <div class='card-text'>9.50</div>
                <button onClick={navigateCart}>Order Now</button>
            </div>
            <div class='card'>
                <div class='card-image'></div>
                <div class='card-title'>Pork</div>
                <div class='card-text'>11.00</div>
                <button onClick={navigateCart}>Order Now</button>
            </div>

        </div>
        
    );
  }
  
  export default Menu;