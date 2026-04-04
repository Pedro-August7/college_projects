import { useState, useMemo } from "react";
import { faker } from "@faker-js/faker";
import FullscreenContainer from "../../components/fullScreenContainer";
import FuncionarioCard from "../13/components/FuncionarioCard";

export default function Ex14() {
  const funcionariosAleatorios = useMemo(() => {
    return Array.from({ length: 30 }).map(() => ({
      id: faker.string.uuid(),
      nome: faker.person.fullName(),
      cargo: faker.person.jobTitle(),
      departamento: faker.person.jobArea(),
    }));
  }, []);

  const funcionariosAgrupados = funcionariosAleatorios.reduce((acc, func) => {
    const depto = func.departamento;
    if (!acc[depto]) {
      acc[depto] = [];
    }
    acc[depto].push(func);
    return acc;
  }, {});

  const departamentos = Object.keys(funcionariosAgrupados).sort();

  return (
    <FullscreenContainer>
      <h1 style={{ marginBottom: "30px", textAlign: "center" }}>Organograma da Empresa (30 Colaboradores)</h1>

      <div style={{ width: "100%", maxWidth: "900px", paddingBottom: "50px" }}>
        {departamentos.map((depto) => (
          <section key={depto} style={{ marginBottom: "40px" }}>
            <div
              style={{
                display: "flex",
                alignItems: "center",
                gap: "15px",
                marginBottom: "15px",
                borderBottom: "2px solid #4ade80",
              }}
            >
              <h2 style={{ color: "#4ade80", margin: "0 0 5px 0" }}>{depto}</h2>
              <span
                style={{
                  backgroundColor: "#4f738f",
                  padding: "2px 10px",
                  borderRadius: "12px",
                  fontSize: "0.8rem",
                }}
              >
                {funcionariosAgrupados[depto].length} integrantes
              </span>
            </div>

            <div
              style={{
                display: "grid",
                gridTemplateColumns: "repeat(auto-fit, minmax(280px, 1fr))",
                gap: "15px",
              }}
            >
              {funcionariosAgrupados[depto].map((func) => (
                <FuncionarioCard key={func.id} funcionario={func} />
              ))}
            </div>
          </section>
        ))}
      </div>
    </FullscreenContainer>
  );
}
