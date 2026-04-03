import { useState } from "react";
import { signInWithEmailAndPassword } from "firebase/auth";
import { auth } from "../../services/firebaseConfig";
import FullscreenContainer from "../../components/fullScreenContainer";
import { Card } from "../../components/Card";
import Alerta from "../06/components/Alerta";

export default function Ex08() {
  const [email, setEmail] = useState("");
  const [senha, setSenha] = useState("");
  const [status, setStatus] = useState({ tipo: "", mensagem: "" });

  const handleLogin = async (e) => {
    e.preventDefault();
    setStatus({ tipo: "", mensagem: "" });

    try {
      await signInWithEmailAndPassword(auth, email, senha);

      setStatus({
        tipo: "SUCESSO",
        mensagem: "Login realizado com sucesso! Bem-vindo de volta.",
      });
    } catch (error) {
      let msg = "Erro ao realizar login.";

      if (error.code === "auth/invalid-credential") {
        msg = "Credenciais Invalidas";
      } else if (error.code === "auth/user-not-found") {
        msg = "Usuário não encontrado.";
      } else if (error.code === "auth/wrong-password") {
        msg = "Senha incorreta.";
      }

      setStatus({ tipo: "ERRO", mensagem: msg });
    }
  };

  return (
    <FullscreenContainer>
      <Card>
        <form onSubmit={handleLogin} style={{ display: "flex", flexDirection: "column", gap: "15px" }}>
          <h2 style={{ textAlign: "center", color: "#fff" }}>Entrar no Sistema</h2>

          <input
            type="email"
            placeholder="E-mail cadastrado"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            style={{ padding: "10px", borderRadius: "5px", border: "1px solid #ccc" }}
            required
          />

          <input
            type="password"
            placeholder="Suae senha"
            value={senha}
            onChange={(e) => setSenha(e.target.value)}
            style={{ padding: "10px", borderRadius: "5px", border: "1px solid #ccc" }}
            required
          />

          <button
            type="submit"
            style={{
              padding: "10px",
              backgroundColor: "#4f738f",
              color: "white",
              border: "none",
              borderRadius: "5px",
              cursor: "pointer",
              fontWeight: "bold",
            }}
          >
            Acessar Conta
          </button>
        </form>
      </Card>

      {status.tipo && (
        <div style={{ marginTop: "20px", width: "100%", maxWidth: "400px" }}>
          <Alerta tipo={status.tipo} mensagem={status.mensagem} />
        </div>
      )}
    </FullscreenContainer>
  );
}
