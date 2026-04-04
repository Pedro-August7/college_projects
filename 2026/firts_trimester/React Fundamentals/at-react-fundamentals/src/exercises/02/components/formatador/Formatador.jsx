import { Card } from "../../../../components/Card";

export default function Formarador({ dados }) {
  const dataFormatada = new Date(dados.ano, dados.mes - 1, dados.dia);
  const mesExtenso = new Intl.DateTimeFormat("pt-BR", { month: "long" }).format(dataFormatada);
  const diaSemanaExtenso = new Intl.DateTimeFormat("pt-BR", { weekday: "long" }).format(dataFormatada);
  const diaZeroEsquerda = String(dados.dia).padStart(2, "0");
  const mesZeroEsquerda = String(dados.mes).padStart(2, "0");

  return (
    <>
      <Card>
        <h2>
          {diaZeroEsquerda}/{mesZeroEsquerda}/{dados.ano}
          <p>Dia da semana: {diaSemanaExtenso}</p>
          <p>Mês: {mesExtenso}</p>
        </h2>
      </Card>
    </>
  );
}
