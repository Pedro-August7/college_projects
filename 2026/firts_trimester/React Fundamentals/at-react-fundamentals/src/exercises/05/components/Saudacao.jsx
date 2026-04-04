export default function Saudacao({ nome }) {
  const horaAtual = new Date().getHours();
  let cumprimento = "";

  if (horaAtual < 12) cumprimento = "Bom dia";
  else if (horaAtual < 18) cumprimento = "Boa tarde";
  else cumprimento = "Boa noite";

  return (
    <h1 style={{ textAlign: "center", marginBottom: "2rem" }}>
      {cumprimento}, {nome}!
    </h1>
  );
}
