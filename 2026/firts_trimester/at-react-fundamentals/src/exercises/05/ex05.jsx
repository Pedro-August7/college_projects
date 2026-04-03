import FullscreenContainer from "../../components/fullScreenContainer";
import Saudacao from "./components/Saudacao";
import ContainerLivro from "../01/components/container/container";
import FormatadorData from "../02/components/formatador/Formatador";
import TelaContagemData from "../03/components/TelaContagemData";
import TelaContagemCores from "../04/components/TelaContagemCores";

export default function Ex05() {
  return (
    <FullscreenContainer>
      <Saudacao nome="Pedro Augusto" />

      <ContainerLivro dados={{ autor: "George Orwell", titulo: "1984", classificacao: 5 }} />

      <FormatadorData dados={{ dia: 13, mes: 9, ano: 2026 }} />

      <TelaContagemData dados={{ titulo: "Aniversário", dia: 13, mes: 9, ano: 2026 }} />

      <TelaContagemCores dados={{ titulo: "Natal", dia: 25, mes: 12, ano: 2026 }} />
    </FullscreenContainer>
  );
}
