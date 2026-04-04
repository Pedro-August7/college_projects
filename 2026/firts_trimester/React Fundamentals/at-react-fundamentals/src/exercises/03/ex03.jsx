import FullscreenContainer from "../../components/fullScreenContainer";
import TelaContagemData from "./components/TelaContagemData";

const eventos = [
  {
    dia: 13,
    mes: 9,
    ano: 2026,
    titulo: "Aniversário do Pedrinho",
  },
  {
    dia: 25,
    mes: 12,
    ano: 2026,
    titulo: "Natal em Família",
  },
  {
    dia: 1,
    mes: 1,
    ano: 2027,
    titulo: "Ano Novo",
  },
  {
    dia: 15,
    mes: 3,
    ano: 2027,
    titulo: "Viagem Especial",
  },
];

export default function Ex03() {
  return (
    <>
      <FullscreenContainer>
        {eventos.map((item, index) => (
          <TelaContagemData key={index} dados={item} />
        ))}
      </FullscreenContainer>
    </>
  );
}
