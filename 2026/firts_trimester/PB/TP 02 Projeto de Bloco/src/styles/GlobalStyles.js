import { createGlobalStyle } from "styled-components";

export const GlobalStyles = createGlobalStyle`
  * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
  }

  body {
    background-color: #f8fafc; /* Cor de fundo leve e amigável para apps de saúde */
    color: #334155;
    -webkit-font-smoothing: antialiased;
  }

  /* Mobile First */
  #root {
    width: 100%;
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    
    /* Tablet/Desktop */
    @media (min-width: 768px) {
      max-width: 480px; 
      margin: 0 auto;
      box-shadow: 0 0 20px rgba(0,0,0,0.05);
      background-color: #ffffff;
    }
  }

  button {
    cursor: pointer;
    border: none;
  }
  
  a {
    text-decoration: none;
  }
`;
