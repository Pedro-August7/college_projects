import { useState, useEffect } from "react";
import FullscreenContainer from "../../components/fullScreenContainer";
import TodoItem from "./components/TodoItem";

export default function Ex11() {
  const [todos, setTodos] = useState([]);
  const [carregando, setCarregando] = useState(true);

  useEffect(() => {
    const buscarTodos = async () => {
      try {
        const resposta = await fetch("https://jsonplaceholder.typicode.com/users/1/todos");
        const dados = await resposta.json();
        setTodos(dados);
      } catch (error) {
        console.error("Erro ao buscar tarefas:", error);
      } finally {
        setCarregando(false);
      }
    };

    buscarTodos();
  }, []);

  return (
    <FullscreenContainer>
      <h1 style={{ marginBottom: "20px" }}>Minhas Tarefas (Usuário #1)</h1>

      {carregando ? (
        <p>Carregando lista...</p>
      ) : (
        <div
          style={{
            display: "flex",
            flexDirection: "column",
            gap: "12px",
            width: "100%",
            maxWidth: "500px",
          }}
        >
          {todos.map((tarefa) => (
            <TodoItem key={tarefa.id} todo={tarefa} />
          ))}
        </div>
      )}
    </FullscreenContainer>
  );
}
