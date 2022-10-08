import React, {useState}from 'react';
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
    
    render() {
      
      return <div class="API">
        <Modal isOpen={OpenModal} className="modal">
          <div class= 'modal-card'>
          <img src=" https://www.nicepng.com/png/detail/302-3026464_png-file-svg-login-member-icon-png.png" class="login-img"></img>
          <br></br>
          <form action= "https://burrito-app-service.kjt7dv43kepem.us-west-2.cs.amazonlightsail.com/login" methods='post'>
          <input type="text" name="username" id="username" class='input-email' placeholder="Username" required />
          <br></br>
          <input type="password" name="password" id="password" class='input-email' placeholder="Password" required />
          <br></br>
          <button type="submit" value="Submit" class= 'button10'>SUBMIT</button>
          </form>
          
           
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