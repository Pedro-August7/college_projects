import { useNavigate } from "react-router-dom";
import styled from "styled-components";
import { Input } from "../../components/common/Input";
import { Button } from "../../components/common/Button";

const LoginContainer = styled.div`
  padding: 30px 20px;
  display: flex;
  flex-direction: column;
  height: 100vh;
  justify-content: center;
`;

const Header = styled.div`
  text-align: center;
  margin-bottom: 40px;

  h1 {
    color: #0ea5e9;
    font-size: 2.5rem;
    margin-bottom: 8px;
  }

  p {
    color: #64748b;
  }
`;

export default function Login() {
  const navigate = useNavigate();

  const handleLoginPaciente = () => navigate("/paciente");
  const handleLoginTerapeuta = () => navigate("/terapeuta");

  return (
    <LoginContainer>
      <Header>
        <h1>MindCare</h1>
        <p>Acesse sua conta para continuar</p>
      </Header>

      <form onSubmit={(e) => e.preventDefault()}>
        <Input label="E-mail" type="email" placeholder="Digite seu e-mail" />

        <Input label="Senha" type="password" placeholder="Digite sua senha" />

        <div style={{ marginTop: "30px" }}>
          <Button onClick={handleLoginPaciente}>Entrar como Paciente</Button>

          <Button $variant="secondary" onClick={handleLoginTerapeuta}>
            Entrar como Terapeuta
          </Button>
        </div>
      </form>
    </LoginContainer>
  );
}
