import React, {useState}from 'react';
import axios from 'axios';
import Modal from 'react-modal';
import{useNavigate} from'react-router-dom';

function Footer() {

  
  
 

  const navigate = useNavigate();

    const navigateCart = () => {
        navigate('/cart');
    };
    const navigateMenu= () => {
      navigate('/Menu');
  };

const[OpenModal, setOpenModal] = useState(false);

  const setOpenModalAsTrue =()=>{
      setOpenModal(true)
  }

  const setOpenModalAsFalse =()=>{
      setOpenModal(false)
  };
  

  class API extends React.Component {
    constructor() {
      super()
      this.state = {user: null, usercount:0, totalcount:0}
    }
    
    

    onLoginChange(event) {
      this.setState({...this.state, user: event.target.value})
    }
    

    login() {
      const {user} = this.state
      var url = 'http://127.0.0.1:5000/login/' + user
      axios.get(url).then((resp) => {
          this.setState({...this.state, 
              usercount: resp.data['user count'], 
              totalcount: resp.data['total count']
          })
      }).catch(error => {
          console.log(error)
      })
  }
  

  

    render() {
      const {user, usercount, totalcount} = this.state
      return <div class="API">
        <Modal isOpen={OpenModal} className="modal">
          <div class= 'modal-card'>
          <div class='modal-image'></div>
          <br></br>
          <input placeholder="Username"class='input-email'type='email' value={user} onChange={this.onLoginChange.bind(this)}/>
          <input placeholder="Password" class='input-email'type='password'></input>
        <br></br>
        {(usercount > 0)} 
        <p><span>{user} Logins: {usercount} </span></p>
        <br></br>
        <p><span>Total User Logins: {totalcount}</span></p>
          <button onClick={this.login.bind(this)}class='button6' >LOGIN</button>
          <button onClick={setOpenModalAsFalse}class='button6'>CANCEL</button>
          </div>
      </Modal>
      </div>
    }
  }


    return (
      
    <footer class="footer">
   
    <button onClick={setOpenModalAsTrue}class='button7'>Login</button>
    
    <button onClick={navigateCart} class='button8'>Order Now</button>
    <button onClick={navigateMenu} class='button7'>Menu</button>
        <br></br>
        <API/>
      
    </footer>
    );
  }
  
  export default Footer;