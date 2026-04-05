import { useState } from "react";
import TextField from "@mui/material/TextField";
import Button from "@mui/material/Button";

import styles from "./Contato.module.css";

export default function Contato() {
  const [form, setForm] = useState({
    nome: "",
    email: "",
    mensagem: "",
  });

  function handleChange(e) {
    setForm({
      ...form,
      [e.target.name]: e.target.value,
    });
  }

  function handleSubmit(e) {
    e.preventDefault();

    alert("Mensagem enviada com sucesso!");

    setForm({
      nome: "",
      email: "",
      mensagem: "",
    });
  }

  return (
    <section id="contato" className={styles.container}>
      <h2 className={styles.titulo}>Entre em Contato</h2>

      <form className={styles.form} onSubmit={handleSubmit}>
        <TextField label="Nome" name="nome" value={form.nome} onChange={handleChange} required fullWidth />

        <TextField label="E-mail" name="email" type="email" value={form.email} onChange={handleChange} required fullWidth />

        <TextField label="Mensagem" name="mensagem" value={form.mensagem} onChange={handleChange} required multiline rows={4} fullWidth />

        <Button variant="contained" type="submit" className={styles.botao}>
          Enviar Mensagem
        </Button>
      </form>
    </section>
  );
}
