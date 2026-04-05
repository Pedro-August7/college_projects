import styles from "./Agenda.module.css";
import EventoItem from "./EventoItem";

export default function Agenda() {
  const eventos = [
    {
      data: "10/05/2026",
      local: "São Paulo - SP",
      tipo: "Comício",
    },
    {
      data: "15/05/2026",
      local: "Belo Horizonte - MG",
      tipo: "Debate",
    },
    {
      data: "20/05/2026",
      local: "Rio de Janeiro - RJ",
      tipo: "Reunião",
    },
    {
      data: "25/05/2026",
      local: "Brasília - DF",
      tipo: "Entrevista",
    },
  ];

  return (
    <section id="agenda" className={styles.container}>
      <h2 className={styles.titulo}>Agenda de Campanha</h2>

      <div className={styles.grid}>
        {eventos.map((evento, index) => (
          <EventoItem key={index} data={evento.data} local={evento.local} tipo={evento.tipo} destaque={index === 0} />
        ))}
      </div>
    </section>
  );
}
