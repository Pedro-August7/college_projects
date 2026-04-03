import { Card } from "../../../components/Card";

export default function FuncionarioCard({ funcionario }) {
  return (
    <Card>
      <div style={{ display: "flex", flexDirection: "column", gap: "4px" }}>
        <span style={{ fontSize: "0.8rem", color: "#4ade80", fontWeight: "bold" }}>ID: #{funcionario.id.slice(0, 8)}</span>
        <h3 style={{ margin: "0", color: "#fff" }}>{funcionario.nome}</h3>
        <p style={{ margin: "0", fontWeight: "500", color: "#e2e8f0" }}>{funcionario.cargo}</p>
        <p style={{ margin: "0", fontSize: "0.9rem", color: "#94a3b8" }}>Setor: {funcionario.departamento}</p>
      </div>
    </Card>
  );
}
