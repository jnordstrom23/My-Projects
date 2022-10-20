
import React from 'react'
import {useState} from 'react';
import Modal from 'react-modal'

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

  //const Checkout = () => {
   // setBeefCount(BeefCount*0)
   // setBeefPrice(BeefPrice*0)
    //setChixCount(ChixCount*0)
   // setChixPrice(ChixPrice*0)
   // setBeanCount(BeanCount*0)
    //setBeanPrice(BeanPrice*0)
    //setPorkCount(PorkCount*0)
    //setPorkPrice(PorkPrice*0)
    //setOpenModal(false)
    //setValue("")
  //}
  
  const[OpenModal, setOpenModal] = useState(false);

    const setOpenModalAsTrue =()=>{
        setOpenModal(true)
    }

    const setOpenModalAsFalse =()=>{
        setOpenModal(false)
    };
    
   
  
    

    function fixedPlace(x) {
      return Number.parseFloat(x).toFixed(2);
    }

    return (
      <div class="cart-container">
  
  <div class='cart'>
          <div class='cart-image'></div>
          <div class='cart-title'>Beef</div>
          <button onClick={plusBeef}class='button3'>+</button>
          <div class="counter">{BeefCount}</div>
          <button disabled ={BeefCount <1}onClick={minusBeef} class='button4'>-</button>
          
          <div class='cart-text'>${BeefPrice.toFixed(2)}</div>
      </div>

      <div class='cart'>
          <div class='cart-image'></div>
          <div class='cart-title'>Chix</div>
          <button onClick={plusChix}class='button3'>+</button>
          <div class="counter">{ChixCount}</div>
          <button disabled ={ChixCount <1}onClick={minusChix} class='button4'>-</button>
          <div class='cart-text'>${ChixPrice.toFixed(2)}</div>
      </div>

      <div class='cart'>
          <div class='cart-image'></div>
          <div class='cart-title'>Bean</div>
          <button onClick={plusBean}class='button3'>+</button>
          <div class="counter">{BeanCount}</div>
          <button disabled ={BeanCount <1}onClick={minusBean} class='button4'>-</button>
          <div class='cart-text'>${BeanPrice.toFixed(2)}</div>
      </div>

      <div class='cart'>
          <div class='cart-image'></div>
          <div class='cart-title'>Pork</div>
          <button onClick={plusPork}class='button3'>+</button>
          <div class="counter">{PorkCount}</div>
          <button disabled ={PorkCount <1}onClick={minusPork} class='button4'>-</button>
          <div class='cart-text'>${PorkPrice.toFixed(2)}</div>
      </div>
      

      <div class='cart'>
          <div class='cart-image'></div>
          <div class='cart-title'>Cart</div>
          <div class='cart-text'></div>
          <div class="counter2">{BeefCount+PorkCount+BeanCount+ChixCount}</div>
          <div class='cart-text'>BURRITOS</div>
      </div>


      <div class='cart'>
          <div class='cart-image'></div>
          <div class='cart-title'>Cost</div>
          <div class='cart-text'>${fixedPlace(BeefPrice+ChixPrice+BeanPrice+PorkPrice)}</div>
         
          
          <button onClick={setOpenModalAsTrue}class='button5'>CHECKOUT</button>
          <Modal isOpen={OpenModal} className="modal2">
          <div class= 'modal-card'>
         
        
          <div class="cart-title">BURRITOS | COUNT </div>
          <div class="cart-text">BEEF :  {BeefCount}</div>
          <div class="cart-text">CHIX :  {ChixCount}</div>
          <div class="cart-text">BEAN :  {BeanCount}</div>
          <div class="cart-text">PORK :  {PorkCount}</div>
          <div class="cart-title">PAYMENT</div>
          <div class='cart-text'>SUBTOTAL : ${fixedPlace(BeefPrice+ChixPrice+BeanPrice+PorkPrice)}</div>
          <div class="cart-text">TAX (9.5%): ${fixedPlace((BeefPrice+ChixPrice+BeanPrice+PorkPrice)*0.095)}</div>
          <div class='cart-text2'>TOTAL : ${fixedPlace(fixedPlace((BeefPrice+ChixPrice+BeanPrice+PorkPrice)*0.095+ BeefPrice+ChixPrice+BeanPrice+PorkPrice))}</div>
          
          <img src= "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQulepVqs0LPJ-_3oB_dfMj1u-isynYtAl-2A&usqp=CAU" alt="visa"class="cclogo"></img>
          <div class='form'>
          <form action= "https://flask-order-app-service.kjt7dv43kepem.us-west-2.cs.amazonlightsail.com/orders" method='post'>
         
          <input type="text" name="first_name" id="first_name" class='input-name' placeholder="First Name" required />
          <input type="text" name="last_name" id="last_name" class='input-name' placeholder="Last Name" required />
          <input type="text" name="credit_card" id="credit_card" class='input-cc' placeholder="Credit Card #" required />
          <input type="text" name="CVV" id="CVV" class='input-cvv' placeholder="CVV" required />
          <label class='label'> Card Expiry Date :   </label><input type="month" name="ExpDate" id="ExpDate" class='input-cc' placeholder="Exp Date" required />
          <input type="text" name="Address" id="Address" class='input-email' placeholder="Address" required />
          <input type="text" name="City" id="City" class='input-city' placeholder="City" required />
          
          <select STYLE="font-size : 12pt"id="state" name="state" class='input-state'>
                <option value="AL">Alabama</option>
                <option value="AK">Alaska</option>
                <option value="AS">American Samoa</option>
                <option value="AZ">Arizona</option>
                <option value="AR">Arkansas</option>
                <option value="UM-81">Baker Island</option>
                <option value="CA">California</option>
                <option value="CO">Colorado</option>
                <option value="CT">Connecticut</option>
                <option value="DE">Delaware</option>
                <option value="DC">District of Columbia</option>
                <option value="FL">Florida</option>
                <option value="GA">Georgia</option>
                <option value="GU">Guam</option>
                <option value="HI">Hawaii</option>
                <option value="UM-84">Howland Island</option>
                <option value="ID">Idaho</option>
                <option value="IL">Illinois</option>
                <option value="IN">Indiana</option>
                <option value="IA">Iowa</option>
                <option value="UM-86">Jarvis Island</option>
                <option value="UM-67">Johnston Atoll</option>
                <option value="KS">Kansas</option>
                <option value="KY">Kentucky</option>
                <option value="UM-89">Kingman Reef</option>
                <option value="LA">Louisiana</option>
                <option value="ME">Maine</option>
                <option value="MD">Maryland</option>
                <option value="MA">Massachusetts</option>
                <option value="MI">Michigan</option>
                <option value="UM-71">Midway Atoll</option>
                <option value="MN">Minnesota</option>
                <option value="MS">Mississippi</option>
                <option value="MO">Missouri</option>
                <option value="MT">Montana</option>
                <option value="UM-76">Navassa Island</option>
                <option value="NE">Nebraska</option>
                <option value="NV">Nevada</option>
                <option value="NH">New Hampshire</option>
                <option value="NJ">New Jersey</option>
                <option value="NM">New Mexico</option>
                <option value="NY">New York</option>
                <option value="NC">North Carolina</option>
                <option value="ND">North Dakota</option>
                <option value="MP">Northern Mariana Islands</option>
                <option value="OH">Ohio</option>
                <option value="OK">Oklahoma</option>
                <option value="OR">Oregon</option>
                <option value="UM-95">Palmyra Atoll</option>
                <option value="PA">Pennsylvania</option>
                <option value="PR">Puerto Rico</option>
                <option value="RI">Rhode Island</option>
                <option value="SC">South Carolina</option>
                <option value="SD">South Dakota</option>
                <option value="TN">Tennessee</option>
                <option value="TX">Texas</option>
                <option value="UM">United States Minor Outlying Islands</option>
                <option value="VI">United States Virgin Islands</option>
                <option value="UT">Utah</option>
                <option value="VT">Vermont</option>
                <option value="VA">Virginia</option>
                <option value="UM-79">Wake Island</option>
                <option value="WA">Washington</option>
                <option value="WV">West Virginia</option>
                <option value="WI">Wisconsin</option>
                <option value="WY">Wyoming</option>
            </select>
            <input type="text" name="zipcode" id="zipcode" class='input-zipcode' placeholder="Zipcode" required />
            <label class='label'>Delivery : Same as Above  </label><input type="checkbox"></input>
          <input type="text" name="Email" id="Email" class='input-email2' placeholder="Email" required />

          <input type="hidden" name="beef" id="beef" value={BeefCount} />
          <input type="hidden" name="chix" id="chix" value={ChixCount} />
          <input type="hidden" name="bean" id="bean" value={BeanCount} />
          <input type="hidden" name="pork" id="pork" value={PorkCount} />
          <input type="hidden" name="tax" id="tax" value={fixedPlace((BeefPrice+ChixPrice+BeanPrice+PorkPrice)*0.095)} />
          <input type="hidden" name="total_sale" id="total_sale" value={fixedPlace((BeefPrice+ChixPrice+BeanPrice+PorkPrice)*0.095+ BeefPrice+ChixPrice+BeanPrice+PorkPrice)} />

          <button disabled = {PorkCount+BeefCount+ChixCount+BeanCount===0} type="submit" value="Submit" class= 'button10'>SUBMIT</button>
          </form>
          </div>
           
          <button onClick={setOpenModalAsFalse}class='button11'>CANCEL</button>
          </div>
      </Modal>
        </div>
      
       
         
      </div>
     
    );
  }

  
  export default Cart;