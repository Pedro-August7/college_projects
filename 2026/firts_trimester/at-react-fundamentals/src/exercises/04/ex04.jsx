import FullscreenContainer from "../../components/fullScreenContainer";
import TelaContagemData from "./components/TelaContagemCores";

const eventos = [
  {
    dia: 13,
    mes: 9,
    ano: 2026,
    titulo: "Aniversário do Pedrinho",
  },
  {
    dia: 5,
    mes: 4,
    ano: 2026,
    titulo: "Carla",
  },
  {
    dia: 7,
    mes: 4,
    ano: 2026,
    titulo: "Grazy",
  },
  {
    dia: 15,
    mes: 3,
    ano: 2027,
    titulo: "Viagem Especial",
  },
];

export default function Ex04() {
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
