import { useMemo } from "react";
import { ThemeProvider, createTheme } from "@mui/material/styles";
import useMediaQuery from "@mui/material/useMediaQuery";
import CssBaseline from "@mui/material/CssBaseline";

import Header from "./components/Header/Header";
import Hero from "./components/Hero/Hero";
import Biografia from "./components/Biografia/Biografia";
import Propostas from "./components/Propostas/Propostas";
import Agenda from "./components/Agenda/Agenda";
import Videos from "./components/Videos/Videos";
import Contato from "./components/Contato/Contato";
import Footer from "./components/Footer/Footer";

export default function App() {
  const prefersDarkMode = useMediaQuery("(prefers-color-scheme: dark)");

  const theme = useMemo(
    () =>
      createTheme({
        palette: {
          mode: prefersDarkMode ? "dark" : "light",
          primary: { main: "#2ea8df" },
          background: {
            default: prefersDarkMode ? "#0b0f14" : "#ffffff",
            paper: prefersDarkMode ? "#161d24" : "#ffffff",
          },
        },
      }),
    [prefersDarkMode],
  );

  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />

      <Header />
      <main>
        <Hero />
        <Biografia />
        <Propostas />
        <Agenda />
        <Videos />
        <Contato />
      </main>
      <Footer />
    </ThemeProvider>
  );
}
