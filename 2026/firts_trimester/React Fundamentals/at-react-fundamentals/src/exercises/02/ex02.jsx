import FullScreenContainer from "../../components/fullScreenContainer.jsx";
import Formarador from "./components/formatador/Formatador";

const feriados = [
  { dia: 1, mes: 1, ano: 2026 },
  { dia: 21, mes: 4, ano: 2026 },
  { dia: 1, mes: 5, ano: 2026 },
  { dia: 7, mes: 9, ano: 2026 },
  { dia: 12, mes: 10, ano: 2026 },
  { dia: 2, mes: 11, ano: 2026 },
  { dia: 15, mes: 11, ano: 2026 },
  { dia: 25, mes: 12, ano: 2026 },
];

export default function Ex02() {
  return (
    <>
      <FullScreenContainer>
        <h1>Datas:</h1>
        {feriados.map((item, index) => (
          <Formarador key={index} dados={item} />
        ))}
      </FullScreenContainer>
    </>
  );
}
