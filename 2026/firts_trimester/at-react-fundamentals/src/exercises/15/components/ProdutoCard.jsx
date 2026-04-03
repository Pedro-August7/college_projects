import { Card } from "../../../components/Card";

export default function ProdutoCard({ produto }) {
  return (
    <Card>
      <div style={{ display: "flex", flexDirection: "column", height: "100%", justifyContent: "space-between" }}>
        <div>
          <span
            style={{
              backgroundColor: "#4ade80",
              color: "#011627",
              padding: "2px 8px",
              borderRadius: "4px",
              fontSize: "0.7rem",
              fontWeight: "bold",
              textTransform: "uppercase",
            }}
          >
            {produto.adjetivo}
          </span>

          <h3 style={{ margin: "10px 0 5px 0", fontSize: "1.1rem", color: "#fff" }}>{produto.nome}</h3>

          <p
            style={{
              fontSize: "0.85rem",
              color: "#94a3b8",
              margin: "0 0 15px 0",
              display: "-webkit-box",
              WebkitLineClamp: "2",
              WebkitBoxOrient: "vertical",
              overflow: "hidden",
            }}
          >
            {produto.descricao}
          </p>
        </div>

        <div style={{ borderTop: "1px solid #4f738f", paddingTop: "10px" }}>
          <span style={{ fontSize: "1.2rem", fontWeight: "bold", color: "#4ade80" }}>R$ {produto.preco}</span>
          <button
            style={{
              width: "100%",
              marginTop: "10px",
              padding: "8px",
              backgroundColor: "#4f738f",
              color: "white",
              border: "none",
              borderRadius: "6px",
              cursor: "pointer",
              fontWeight: "600",
            }}
          >
            Adicionar ao Carrinho
          </button>
        </div>
      </div>
    </Card>
  );
}
