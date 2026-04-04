import { useState, useEffect } from "react";
import FullscreenContainer from "../../components/fullScreenContainer";
import TodoItem from "../11/components/TodoItem";

const usuariosFicticios = [
  { id: 1, nome: "Pedro Augusto" },
  { id: 2, nome: "Ana Costa" },
  { id: 3, nome: "Carlos Silva" },
  { id: 4, nome: "Mariana Souza" },
  { id: 5, nome: "Lucas Oliveira" },
];

export default function Ex12() {
  const [usuarioId, setUsuarioId] = useState(1);
  const [todos, setTodos] = useState([]);
  const [carregando, setCarregando] = useState(false);

  useEffect(() => {
    const buscarTodosPorUsuario = async () => {
      setCarregando(true);
      try {
        const resposta = await fetch(`https://jsonplaceholder.typicode.com/users/${usuarioId}/todos`);
        const dados = await resposta.json();
        setTodos(dados);
      } catch (error) {
        console.error("Erro ao buscar tarefas:", error);
      } finally {
        setCarregando(false);
      }
    };

    buscarTodosPorUsuario();
  }, [usuarioId]);
  return (
    <FullscreenContainer>
      <div style={{ textAlign: "center", marginBottom: "2rem", width: "100%", maxWidth: "500px" }}>
        <h1 style={{ marginBottom: "1rem" }}>Gerenciador de Tarefas</h1>

        <label htmlFor="todo-user-select" style={{ display: "block", marginBottom: "10px" }}>
          Filtrar tarefas por responsável:
        </label>

        <select
          id="todo-user-select"
          value={usuarioId}
          onChange={(e) => setUsuarioId(e.target.value)}
          style={{
            padding: "12px",
            borderRadius: "8px",
            width: "100%",
            backgroundColor: "#3f617d",
            color: "white",
            border: "1px solid #4f738f",
            fontSize: "1rem",
            cursor: "pointer",
          }}
        >
          {usuariosFicticios.map((u) => (
            <option key={u.id} value={u.id}>
              {u.nome}
            </option>
          ))}
        </select>
      </div>

      <div
        style={{
          display: "flex",
          flexDirection: "column",
          gap: "12px",
          width: "100%",
          maxWidth: "500px",
        }}
      >
        {carregando ? (
          <p style={{ textAlign: "center" }}>Carregando lista de {usuariosFicticios.find((u) => u.id == usuarioId)?.nome}...</p>
        ) : (
          todos.map((tarefa) => <TodoItem key={tarefa.id} todo={tarefa} />)
        )}
      </div>
    </FullscreenContainer>
  );
}
