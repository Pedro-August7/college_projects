import { useState } from "react";
import { faker } from "@faker-js/faker";
import FullscreenContainer from "../../components/fullScreenContainer";
import ProdutoCard from "./components/ProdutoCard";

export default function Ex15() {
  const [produtos] = useState(() => {
    return Array.from({ length: 50 }).map(() => ({
      id: faker.string.uuid(),
      nome: faker.commerce.productName(),
      descricao: faker.commerce.productDescription(),
      adjetivo: faker.commerce.productAdjective(),
      preco: faker.commerce.price({ min: 10, max: 1000, dec: 2 }),
    }));
  });

  return (
    <FullscreenContainer>
      <header style={{ textAlign: "center", marginBottom: "40px" }}>
        <h1 style={{ fontSize: "2.5rem", color: "#4ade80" }}>Nossa Loja</h1>
        <p>Confira nossos 50 lançamentos exclusivos</p>
      </header>

      <div
        style={{
          display: "grid",
          gridTemplateColumns: "repeat(auto-fill, minmax(250px, 1fr))",
          gap: "25px",
          width: "100%",
          maxWidth: "1200px",
          padding: "0 20px 60px 20px",
        }}
      >
        {produtos.map((produto) => (
          <ProdutoCard key={produto.id} produto={produto} />
        ))}
      </div>
    </FullscreenContainer>
  );
}
