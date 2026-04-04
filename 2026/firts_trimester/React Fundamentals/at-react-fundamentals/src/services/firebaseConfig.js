import { initializeApp } from "firebase/app";
import { getAuth } from "firebase/auth";

const firebaseConfig = {
  apiKey: "AIzaSyATdDfrdN4ICSOKma2aaBu_7oDiYztbuCc",
  authDomain: "at-fundamentos-de-react-27c27.firebaseapp.com",
  projectId: "at-fundamentos-de-react-27c27",
  storageBucket: "at-fundamentos-de-react-27c27.firebasestorage.app",
  messagingSenderId: "223679316462",
  appId: "1:223679316462:web:b85fc5b871218489bc4eff",
  measurementId: "G-5LJ7B71PJK",
};

const app = initializeApp(firebaseConfig);
export const auth = getAuth(app);
