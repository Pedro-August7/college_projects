import { useState } from "react";
import { createUserWithEmailAndPassword } from "firebase/auth";
import { auth } from "../../services/firebaseConfig";
import FullscreenContainer from "../../components/fullScreenContainer";
import { Card } from "../../components/Card";
import Alerta from "../06/components/Alerta";

export default function Ex07() {
  const [email, setEmail] = useState("");
  const [senha, setSenha] = useState("");
  const [status, setStatus] = useState({ tipo: "", mensagem: "" });

  const handleCadastro = async (e) => {
    e.preventDefault();
    setStatus({ tipo: "", mensagem: "" });

    try {
      await createUserWithEmailAndPassword(auth, email, senha);
      setStatus({ tipo: "SUCESSO", mensagem: "Conta criada com sucesso!" });
      setEmail("");
      setSenha("");
    } catch (error) {
      let msg = "Erro ao criar conta.";
      if (error.code === "auth/email-already-in-use") msg = "Este e-mail já está em uso.";
      if (error.code === "auth/weak-password") msg = "A senha deve ter no mínimo 6 caracteres.";

      setStatus({ tipo: "ERRO", mensagem: msg });
    }
  };

  return (
    <FullscreenContainer>
      <Card>
        <form onSubmit={handleCadastro} style={{ display: "flex", flexDirection: "column", gap: "15px" }}>
          <h2 style={{ textAlign: "center" }}>Criar Conta</h2>

          <input
            type="email"
            placeholder="Seu melhor e-mail"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            style={{ padding: "10px", borderRadius: "5px", border: "1px solid #ccc" }}
            required
          />

          <input
            type="password"
            placeholder="Senha (mínimo 6 dígitos)"
            value={senha}
            onChange={(e) => setSenha(e.target.value)}
            style={{ padding: "10px", borderRadius: "5px", border: "1px solid #ccc" }}
            required
          />

          <button type="submit" style={{ padding: "10px", backgroundColor: "#4f738f", color: "white", border: "none", borderRadius: "5px", cursor: "pointer" }}>
            Cadastrar
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
