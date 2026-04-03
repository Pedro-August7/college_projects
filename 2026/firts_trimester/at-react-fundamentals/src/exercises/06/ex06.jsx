import FullscreenContainer from "../../components/fullScreenContainer";
import Alerta from "./components/Alerta";

export default function Ex06() {
  return (
    <FullscreenContainer>
      <h1 style={{ marginBottom: "2rem" }}>Central de Alertas</h1>

      <Alerta tipo="SUCESSO" mensagem="Seu formulário foi enviado com sucesso! Parabéns." />

      <Alerta tipo="ATENCAO" mensagem="Seu armazenamento está quase cheio. Libere espaço." />

      <Alerta tipo="ERRO" mensagem="Não foi possível conectar ao servidor. Tente novamente." />
    </FullscreenContainer>
  );
}
