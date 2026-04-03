import { useState } from "react";
import { faker } from "@faker-js/faker";
import FullscreenContainer from "../../components/fullScreenContainer";
import FuncionarioCard from "./components/FuncionarioCard";

export default function Ex13() {
  const [funcionarios] = useState(() => {
    return Array.from({ length: 10 }).map(() => ({
      id: faker.string.uuid(),
      nome: faker.person.fullName(),
      cargo: faker.person.jobTitle(),
      departamento: faker.person.jobArea(),
    }));
  });

  return (
    <FullscreenContainer>
      <h1 style={{ marginBottom: "20px", textAlign: "center" }}>Quadro de Funcionários</h1>

      <div
        style={{
          display: "grid",
          gridTemplateColumns: "repeat(auto-fit, minmax(300px, 1fr))",
          gap: "20px",
          width: "100%",
          maxWidth: "1000px",
          paddingBottom: "40px",
        }}
      >
        {funcionarios.map((func) => (
          <FuncionarioCard key={func.id} funcionario={func} />
        ))}
      </div>
    </FullscreenContainer>
  );
}
