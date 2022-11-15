// For Firebase JS SDK v7.20.0 and later, measurementId is optional
// I used Firebase JS SDK 9 with compat version 8

import firebase from "firebase/compat/app";
import 'firebase/compat/auth';
import 'firebase/compat/firestore';

const firebaseConfig = {
    apiKey: "AIzaSyD8nxaA03zr3b0Slb79Upr9taMa0fXl4Qg",
    authDomain: "burrito-ordering-app.firebaseapp.com",
    databaseURL: "https://burrito-ordering-app.firebaseio.com",
    projectId: "burrito-ordering-app",
    storageBucket: "burrito-ordering-app.appspot.com",
    messagingSenderId: "776613424611",
    appId: "1:776613424611:web:1a9624efc9942cb01e04d6",
    measurementId: "G-N7Z665FBSG"
  };

const firebaseApp = firebase.initializeApp(firebaseConfig);
const db = firebaseApp.firestore();
const auth = firebase.auth();
const provider = new firebase.auth.GoogleAuthProvider();

export {auth, provider};
export default db;