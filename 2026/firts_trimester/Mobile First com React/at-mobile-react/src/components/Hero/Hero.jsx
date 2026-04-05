import styles from "./Hero.module.css";
import Button from "@mui/material/Button";
import eneas_logo from "../../assets/Eneas-Carneiro.jpg";

export default function Hero() {
  function handleScroll() {
    const section = document.querySelector("#propostas");

    if (section) {
      section.scrollIntoView({
        behavior: "smooth",
      });
    }
  }

  return (
    <section className={styles.hero}>
      <div className={styles.container}>
        <div className={styles.content}>
          <h1 className={styles.title}>Um futuro melhor começa agora</h1>

          <p className={styles.subtitle}>Eu acredito piamente que no meu país vai se levantar uma legião de jovens, guerreiros, dispostos a recuperar aquela soberania que nos foi retirada.</p>

          <Button variant="contained" size="large" onClick={handleScroll}>
            Conheça as propostas
          </Button>
        </div>

        <div className={styles.imageWrapper}>
          <img src={eneas_logo} alt="Enéas Carneiro" className={styles.image} />
        </div>
      </div>
    </section>
  );
}
