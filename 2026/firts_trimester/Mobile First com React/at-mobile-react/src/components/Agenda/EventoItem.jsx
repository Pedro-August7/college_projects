import styles from "./EventoItem.module.css";

export default function EventoItem({ data, local, tipo, destaque }) {
  return (
    <div className={`${styles.card} ${destaque ? styles.destaque : ""}`}>
      {destaque && <span className={styles.selo}>Próximo</span>}

      <p>
        <strong>Data:</strong> {data}
      </p>
      <p>
        <strong>Local:</strong> {local}
      </p>
      <p>
        <strong>Evento:</strong> {tipo}
      </p>
    </div>
  );
}
