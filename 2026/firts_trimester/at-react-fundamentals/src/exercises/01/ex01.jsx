import Container from "./components/container/container";
import FullScreenContainer from "../../components/fullScreenContainer";

const listaDeLivros = [
  { autor: "George Orwell", titulo: "1984", classificacao: 5 },
  { autor: "J.R.R. Tolkien", titulo: "O Senhor dos Anéis", classificacao: 3 },
  { autor: "Machado de Assis", titulo: "Dom Casmurro", classificacao: 2 },
  { autor: "Clarice Lispector", titulo: "A Hora da Estrela", classificacao: 4 },
  { autor: "Dan Brown", titulo: "O Código Da Vinci", classificacao: 3 },
];

export default function Ex01() {
  return (
    <>
      <FullScreenContainer>
        <h1>Lista de Livros</h1>
        {listaDeLivros.map((filme, index) => (
          <Container key={index} dados={filme} />
        ))}
      </FullScreenContainer>
    </>
  );
}
