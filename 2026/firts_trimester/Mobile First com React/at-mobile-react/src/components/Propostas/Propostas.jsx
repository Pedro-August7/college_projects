import styles from "./Propostas.module.css";
import { Card, CardContent, Typography, Box } from "@mui/material";
import { propostas, propostasExtras } from "./propostasData";

export default function Propostas() {
  return (
    <section id="propostas" className={styles.container}>
      <h2 className={styles.titulo}>Propostas</h2>

      <div className={styles.gridCards}>
        {propostas.map((item, index) => {
          const Icon = item.icon;

          return (
            <Card
              key={index}
              className={styles.card}
              sx={{
                "&:hover": {
                  transform: "translateY(-8px)",
                  boxShadow: 6,
                  transition: "all 0.3s ease-in-out",
                },
              }}
            >
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
        <h3>Outras Propostas</h3>

        <ul className={styles.listaFlex}>
          {propostasExtras.map((item, index) => (
            <Box
              key={index}
              component="li"
              className={styles.listaItem}
              sx={{
                cursor: "pointer",
                transition: "all 0.3s ease-in-out",
                border: "1px solid transparent",
                "&:hover": {
                  transform: "translateY(-4px)",
                  backgroundColor: "var(--color-card)",
                  borderColor: "var(--color-primary)",
                  color: "var(--color-primary)",
                  boxShadow: "0 4px 12px rgba(0,0,0,0.1)",
                },
              }}
            >
              {item}
            </Box>
          ))}
        </ul>
      </div>
    </section>
  );
}
