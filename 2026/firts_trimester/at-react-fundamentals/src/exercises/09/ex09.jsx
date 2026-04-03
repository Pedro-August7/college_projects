import { useState, useEffect } from "react";
import FullscreenContainer from "../../components/fullScreenContainer";
import PostItem from "./components/PostItem";

export default function Ex09() {
  const [posts, setPosts] = useState([]);
  const [carregando, setCarregando] = useState(true);

  useEffect(() => {
    const buscarPosts = async () => {
      try {
        const resposta = await fetch("https://jsonplaceholder.typicode.com/users/1/posts");
        const dados = await resposta.json();
        setPosts(dados);
      } catch (error) {
        console.error("Erro ao buscar posts:", error);
      } finally {
        setCarregando(false);
      }
    };

    buscarPosts();
  }, []);

  return (
    <FullscreenContainer>
      <h1 style={{ marginBottom: "20px" }}>Posts do Usuário #1</h1>

      {carregando ? (
        <p>Carregando mensagens...</p>
      ) : (
        <div
          style={{
            display: "flex",
            flexDirection: "column",
            gap: "20px",
            width: "100%",
            maxWidth: "500px",
          }}
        >
          {posts.map((item) => (
            <PostItem key={item.id} post={item} />
          ))}
        </div>
      )}
    </FullscreenContainer>
  );
}
