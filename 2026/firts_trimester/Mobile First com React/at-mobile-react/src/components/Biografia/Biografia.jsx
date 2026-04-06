import { useEffect, useState } from "react";
import styles from "./Biografia.module.css";

export default function Biografia() {
  const [bio, setBio] = useState(null);

  useEffect(() => {
    async function fetchBiografia() {
      try {
        const response = await fetch("https://dadosabertos.camara.leg.br/api/v2/deputados/74269");

        const data = await response.json();
        setBio(data.dados);
      } catch (error) {
        console.error("Erro ao buscar biografia:", error);
      }
    }

    fetchBiografia();
  }, []);

  if (!bio) {
    return <p className={styles.loading}>Carregando biografia...</p>;
  }

  return (
    <section id="biografia" className={styles.biografia}>
      <div className={styles.container}>
        <div className={styles.imageWrapper}>
          <img src={bio.ultimoStatus?.urlFoto} alt={bio.nomeCivil} className={styles.image} />
        </div>

        <div className={styles.content}>
          <h2>{bio.nomeCivil}</h2>

          <p>
            {bio.nomeCivil} foi um político e médico brasileiro conhecido por sua forte presença nos debates públicos e defesa de ideias nacionalistas. Atuou como deputado federal e marcou a política
            brasileira por seus discursos diretos e posicionamentos firmes.
          </p>
        </div>
      </div>
    </section>
  );
}
