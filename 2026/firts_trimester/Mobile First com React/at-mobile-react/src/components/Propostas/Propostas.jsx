import styles from "./Propostas.module.css";

import { Card, CardContent, Typography } from "@mui/material";

import { propostas, propostasExtras } from "./propostasData";

export default function Propostas() {
  return (
    <section id="propostas" className={styles.container}>
      <h2 className={styles.titulo}>Propostas</h2>

      <div className={styles.gridCards}>
        {propostas.map((item, index) => {
          const Icon = item.icon;

          return (
            <Card key={index} className={styles.card}>
              <CardContent>
                <Icon className={styles.icon} />

                <Typography variant="h6" gutterBottom>
                  {item.titulo}
                </Typography>

                <Typography variant="body2">{item.descricao}</Typography>
              </CardContent>
            </Card>
          );
        })}
      </div>

      <div className={styles.listaContainer}>
        <h3>Outras propostas</h3>

        <ul className={styles.listaFlex}>
          {propostasExtras.map((item, index) => (
            <li key={index} className={styles.listaItem}>
              {item}
            </li>
          ))}
        </ul>
      </div>
    </section>
  );
}
