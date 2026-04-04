import { Card } from "../../../components/Card";

export default function Alerta({ mensagem, tipo }) {
  const cores = {
    SUCESSO: "#4ade80",
    ERRO: "#f87171",
    ATENCAO: "#facc15",
  };

  const corEscolhida = cores[tipo] || "#94a3b8";

  return (
    <Card corFundo={corEscolhida}>
      <div style={{ display: "flex", flexDirection: "column", alignItems: "center" }}>
        <strong style={{ fontSize: "1.2rem", marginBottom: "8px" }}>{tipo}</strong>
        <p style={{ textAlign: "center", margin: 0 }}>{mensagem}</p>
      </div>
    </Card>
  );
}
