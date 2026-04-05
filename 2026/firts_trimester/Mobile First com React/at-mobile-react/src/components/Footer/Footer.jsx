import styles from "./Footer.module.css";

import { FaFacebookF, FaInstagram, FaYoutube, FaXTwitter } from "react-icons/fa6";

export default function Footer() {
  return (
    <footer className={styles.footer}>
      <div className={styles.container}>
        <div className={styles.social}>
          <a href="https://www.facebook.com/EneasCarneiro.Br/" target="blank" aria-label="Facebook">
            <FaFacebookF />
          </a>

          <a href="https://www.instagram.com/eneasoficial/" target="blank" aria-label="Instagram">
            <FaInstagram />
          </a>

          <a href="https://www.youtube.com/user/EneasTV" target="blank" aria-label="YouTube">
            <FaYoutube />
          </a>

          <a href="https://x.com/EneasProna01" target="blank" aria-label="X Twitter">
            <FaXTwitter />
          </a>
        </div>

        <div className={styles.contato}>
          <p>Email: contato@eneas2026.com.br</p>
          <p>Telefone: (11) 99999-0000</p>
        </div>

        <div className={styles.copy}>
          <p>© 2026 Enéas Carneiro. Todos os direitos reservados.</p>
        </div>
      </div>
    </footer>
  );
}
