
import React from 'react'
import axios from 'axios';
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

  const Checkout = () => {
    setBeefCount(BeefCount*0)
    setBeefPrice(BeefPrice*0)
    setChixCount(ChixCount*0)
    setChixPrice(ChixPrice*0)
    setBeanCount(BeanCount*0)
    setBeanPrice(BeanPrice*0)
    setPorkCount(PorkCount*0)
    setPorkPrice(PorkPrice*0)
    setOpenModal(false)
    setValue("")
  }
  
  const[OpenModal, setOpenModal] = useState(false);

    const setOpenModalAsTrue =()=>{
        setOpenModal(true)
    }

    const setOpenModalAsFalse =()=>{
        setOpenModal(false)
    };
    
    const [value, setValue] = useState('');
  
    

    function fixedPlace(x) {
      return Number.parseFloat(x).toFixed(2);
    }


    class API2 extends React.Component {
      constructor() {
        super()
        this.state = {email: null, emailcount:0}
        this.state = {BeefCount:null}
      }
      
     
      
  
      onEmailChange(event) {
        this.setState({...this.state, email: event.target.value})
        this.setState({...this.state, BeefCount: event.target.value})
      }

      onBeefSubmit(event) {
        
      }
      
      
  
      data() {
        const {email} = this.state
        const {BeefCount} = this.state
        var url = 'http://127.0.0.1:5000/data/' + email +BeefCount
        axios.get(url).then((resp) => {
            this.setState({...this.state, 
                emailcount: resp.data['email count'], 
                totalemailcount: resp.data['total email count'],

            })
        }).catch(error => {
            console.log(error)
        })
    }
    
  
      render() {
        const {email, emailcount} = this.state
        const {BeefCount} = this.state
        return <div class="API">
          <Modal isOpen={OpenModal} className="modal">
            <div class= 'modal-card'>
            <div class='modal-image'></div>
            <br></br>
            <input placeholder="Email"class='input-email'type='email' value={email} onChange={this.onEmailChange.bind(this)}/>
            
          <br></br>
          {(emailcount > 0)} 
          <p><span>Your Email: {email} </span></p>
          <button onClick={this.data.bind(this) }class='button6' >SUBMIT EMAIL</button>
          {(BeefCount)}
           <button onClick={setOpenModalAsFalse}class='button6'>CANCEL</button>
          <button onClick={Checkout}class='button9' >FINAL CHECKOUT</button>
           
            </div>
        </Modal>
        </div>
      }
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
          <API2/>
      
       
         
      </div>
     
  </div>
    );
  }

  
  export default Cart;