import { Card } from "../../../components/Card";

export default function TelaContagemData({ dados }) {
  const diaZeroEsquerda = String(dados.dia).padStart(2, "0");
  const mesZeroEsquerda = String(dados.mes).padStart(2, "0");
  const now = new Date();
  const dataEvento = new Date(dados.ano, dados.mes - 1, dados.dia);
  const diferencaMilissegundos = dataEvento - now;
  const diasFaltando = Math.ceil(diferencaMilissegundos / (1000 * 60 * 60 * 24));

  let corDinamica = "";
  if (diasFaltando > 7) {
    corDinamica = "#4ade80";
  } else if (diasFaltando > 3) {
    corDinamica = "#facc15";
  } else {
    corDinamica = "#f87171";
  }

  return (
    <>
      <Card corFundo={corDinamica}>
        <h1>{dados.titulo}</h1>
        <p>
          Data: {diaZeroEsquerda}/{mesZeroEsquerda}/{dados.ano}
        </p>
        <p>Faltam {diasFaltando} dias</p>
      </Card>
    </>
  );
}
