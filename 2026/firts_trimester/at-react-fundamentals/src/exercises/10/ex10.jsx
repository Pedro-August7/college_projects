import { useState, useEffect } from "react";
import FullscreenContainer from "../../components/fullScreenContainer";
import PostItem from "../09/components/PostItem";

const usuariosFicticios = [
  { id: 1, nome: "Pedro Augusto" },
  { id: 2, nome: "Ana Costa" },
  { id: 3, nome: "Carlos Silva" },
  { id: 4, nome: "Mariana Souza" },
  { id: 5, nome: "Lucas Oliveira" },
];

export default function Ex10() {
  const [usuarioId, setUsuarioId] = useState(1);
  const [posts, setPosts] = useState([]);
  const [carregando, setCarregando] = useState(false);

  useEffect(() => {
    const buscarPostsPorUsuario = async () => {
      setCarregando(true);
      try {
        const resposta = await fetch(`https://jsonplaceholder.typicode.com/users/${usuarioId}/posts`);
        const dados = await resposta.json();
        setPosts(dados);
      } catch (error) {
        console.error("Erro ao buscar posts:", error);
      } finally {
        setCarregando(false);
      }
    };

    buscarPostsPorUsuario();
  }, [usuarioId]);

  return (
    <FullscreenContainer>
      <div style={{ textAlign: "center", marginBottom: "2rem", width: "100%", maxWidth: "500px" }}>
        <h1 style={{ marginBottom: "1rem" }}>Filtro de Posts</h1>

        <label htmlFor="user-select" style={{ display: "block", marginBottom: "10px" }}>
          Selecione um Autor:
        </label>

        <select
          id="user-select"
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
          }}
        >
          {usuariosFicticios.map((u) => (
            <option key={u.id} value={u.id}>
              {u.nome}
            </option>
          ))}
        </select>
      </div>

      <div style={{ display: "flex", flexDirection: "column", gap: "20px", width: "100%", maxWidth: "500px" }}>
        {carregando ? (
          <p style={{ textAlign: "center" }}>Buscando posts de {usuariosFicticios.find((u) => u.id == usuarioId)?.nome}...</p>
        ) : (
          posts.map((post) => <PostItem key={post.id} post={post} />)
        )}
      </div>
    </FullscreenContainer>
  );
}
