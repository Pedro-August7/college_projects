import Header from "./components/Header/Header";
import Hero from "./components/Hero/Hero";
import Biografia from "./components/Biografia/Biografia";
import Propostas from "./components/Propostas/Propostas";
import Agenda from "./components/Agenda/Agenda";
import Videos from "./components/Videos/Videos";
import Contato from "./components/Contato/Contato";
import Footer from "./components/Footer/Footer";

export default function App() {
  return (
    <>
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
    </>
  );
}
