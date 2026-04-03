import { useState, useMemo } from "react";
import { faker } from "@faker-js/faker";
import FullscreenContainer from "../../components/fullScreenContainer";
import ProdutoCard from "../15/components/ProdutoCard";
export default function Ex16() {
  const produtosAleatorios = useMemo(() => {
    return Array.from({ length: 50 }).map(() => ({
      id: faker.string.uuid(),
      nome: faker.commerce.productName(),
      descricao: faker.commerce.productDescription(),
      adjetivo: faker.commerce.productAdjective(),
      preco: faker.commerce.price({ min: 10, max: 1000, dec: 2 }),
      departamento: faker.commerce.department(),
    }));
  }, []);

  const produtosAgrupados = produtosAleatorios.reduce((acc, produto) => {
    const depto = produto.departamento;
    if (!acc[depto]) {
      acc[depto] = [];
    }
    acc[depto].push(produto);
    return acc;
  }, {});

  const nomesDepartamentos = Object.keys(produtosAgrupados).sort();

  return (
    <FullscreenContainer>
      <header style={{ textAlign: "center", marginBottom: "40px" }}>
        <h1 style={{ fontSize: "2.2rem", color: "#4ade80" }}>Catálogo por Categoria</h1>
        <p>Explore nossos produtos organizados por setor</p>
      </header>

      <div style={{ width: "100%", maxWidth: "1100px", paddingBottom: "60px" }}>
        {nomesDepartamentos.map((depto) => (
          <section key={depto} style={{ marginBottom: "50px" }}>
            <div
              style={{
                display: "flex",
                justifyContent: "space-between",
                alignItems: "baseline",
                borderBottom: "2px solid #3f617d",
                marginBottom: "20px",
                paddingBottom: "5px",
              }}
            >
              <h2 style={{ color: "#fff", margin: 0 }}>{depto}</h2>
              <span style={{ color: "#94a3b8", fontSize: "0.9rem" }}>{produtosAgrupados[depto].length} itens encontrados</span>
            </div>

            <div
              style={{
                display: "grid",
                gridTemplateColumns: "repeat(auto-fill, minmax(240px, 1fr))",
                gap: "20px",
              }}
            >
              {produtosAgrupados[depto].map((prod) => (
                <ProdutoCard key={prod.id} produto={prod} />
              ))}
            </div>
          </section>
        ))}
      </div>
    </FullscreenContainer>
  );
}
