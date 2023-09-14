// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyBlp55LEBvfwD0YCrU6oNolRh-zuxGzq7k",
  authDomain: "induskritistorage.firebaseapp.com",
  databaseURL: "https://induskritistorage-default-rtdb.asia-southeast1.firebasedatabase.app",
  projectId: "induskritistorage",
  storageBucket: "induskritistorage.appspot.com",
  messagingSenderId: "517916698146",
  appId: "1:517916698146:web:7a846ff5fb832c22bc0c7b",
  measurementId: "G-08WC3YTRJX"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);