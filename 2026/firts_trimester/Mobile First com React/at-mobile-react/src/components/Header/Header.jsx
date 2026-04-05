import { useState, useEffect, useRef } from "react";
import styles from "./Header.module.css";
import { FaBars, FaTimes } from "react-icons/fa";

export default function Header() {
  const [menuOpen, setMenuOpen] = useState(false);
  const [visible, setVisible] = useState(true);
  const prevScrollY = useRef(0);

  function toggleMenu() {
    setMenuOpen(!menuOpen);
  }

  function handleNavClick(e, targetId) {
    e.preventDefault();
    const section = document.querySelector(targetId);

    if (section) {
      section.scrollIntoView({ behavior: "smooth" });
    }

    setMenuOpen(false);
  }

  useEffect(() => {
    const handleScroll = () => {
      const currentScrollY = window.scrollY;

      if (currentScrollY > prevScrollY.current && currentScrollY > 80) {
        setVisible(false);
      } else {
        setVisible(true);
      }

      prevScrollY.current = currentScrollY;
    };

    window.addEventListener("scroll", handleScroll);

    return () => {
      window.removeEventListener("scroll", handleScroll);
    };
  }, []);

  return (
    <header className={`${styles.header} ${visible ? "" : styles.hidden}`}>
      <div className={styles.container}>
        <h1 className={styles.logo}>Enéas Carneiro</h1>

        <button className={styles.hamburger} onClick={toggleMenu} aria-label="Abrir menu">
          {menuOpen ? <FaTimes /> : <FaBars />}
        </button>

        <nav className={`${styles.nav} ${menuOpen ? styles.active : ""}`}>
          <a href="#biografia" onClick={(e) => handleNavClick(e, "#biografia")}>
            Biografia
          </a>
          <a href="#propostas" onClick={(e) => handleNavClick(e, "#propostas")}>
            Propostas
          </a>
          <a href="#agenda" onClick={(e) => handleNavClick(e, "#agenda")}>
            Agendas
          </a>
          <a href="#videos" onClick={(e) => handleNavClick(e, "#videos")}>
            Vídeos
          </a>
          <a href="#contato" onClick={(e) => handleNavClick(e, "#contato")}>
            Contato
          </a>
        </nav>
      </div>
    </header>
  );
}
