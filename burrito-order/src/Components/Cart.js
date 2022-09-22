
import {useState} from 'react';

function Cart() {

  

  const[BeefCount,setBeefCount]=useState(0);
  const[ChixCount,setChixCount]=useState(0);
  const[BeanCount,setBeanCount]=useState(0);
  const[PorkCount,setPorkCount]=useState(0);
  
  const[BeefPrice,setBeefPrice]=useState(0);
  const[ChixPrice,setChixPrice]=useState(0);
  const[BeanPrice,setBeanPrice]=useState(0);
  const[PorkPrice,setPorkPrice]=useState(0);
  

  const plusBeef = () => {
    setBeefCount(BeefCount+1)
    setBeefPrice(BeefPrice+10.00)
  }
  const minusBeef = () => {
    setBeefCount(BeefCount-1)
    setBeefPrice(BeefPrice-10.00)
  }

  const plusChix = () => {
    setChixCount(ChixCount+1)
    setChixPrice(ChixPrice+10.50)
  }
  const minusChix = () => {
    setChixCount(ChixCount-1)
    setChixPrice(ChixPrice-10.50)
  }

  const plusBean = () => {
    setBeanCount(BeanCount+1)
    setBeanPrice(BeanPrice+9.50)
  }
  const minusBean = () => {
    setBeanCount(BeanCount-1)
    setBeanPrice(BeanPrice-9.50)
  }

  const plusPork = () => {
    setPorkCount(PorkCount+1)
    setPorkPrice(PorkPrice+11.00)
  }
  const minusPork = () => {
    setPorkCount(PorkCount-1)
    setPorkPrice(PorkPrice-11.00)
  }

  

    return (
      <div class="cart-container">
  
  <div class='cart'>
          <div class='cart-image'></div>
          <div class='cart-title'>Beef</div>
          
          <button onClick={plusBeef}class='button3'>+</button>
          <div class="counter">{BeefCount}</div>
          <button onClick={minusBeef} class='button4'>-</button>
          
          <div class='cart-text'>${BeefPrice}</div>
      </div>

      <div class='cart'>
          <div class='cart-image'></div>
          <div class='cart-title'>Chix</div>
          
          <button onClick={plusChix}class='button3'>+</button>
          <div class="counter">{ChixCount}</div>
          <button onClick={minusChix} class='button4'>-</button>
          
          <div class='cart-text'>${ChixPrice}</div>
      </div>

      <div class='cart'>
          <div class='cart-image'></div>
          <div class='cart-title'>Bean</div>
          
          <button onClick={plusBean}class='button3'>+</button>
          <div class="counter">{BeanCount}</div>
          <button onClick={minusBean} class='button4'>-</button>
          
          <div class='cart-text'>${BeanPrice}</div>
      </div>

      <div class='cart'>
          <div class='cart-image'></div>
          <div class='cart-title'>Pork</div>
          
          <button onClick={plusPork}class='button3'>+</button>
          <div class="counter">{PorkCount}</div>
          <button onClick={minusPork} class='button4'>-</button>
          
          <div class='cart-text'>${PorkPrice}</div>
      </div>
      

      <div class='cart'>
          <div class='cart-image'></div>
          <div class='cart-title'>Cart</div>
          <div class='cart-text'></div>
          <button class='button2'>Add to Cart</button>
      </div>
     
  </div>
    );
  }
  
  export default Cart;