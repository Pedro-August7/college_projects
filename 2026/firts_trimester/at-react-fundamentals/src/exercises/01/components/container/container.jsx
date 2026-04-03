import styled from "styled-components";
import { Card } from "../../../../components/Card";

export default function Container({ dados }) {
  return (
    <>
      <Card valorClassificacao={dados.classificacao}>
        <h2>{dados.titulo}</h2>
        <p>Autor: {dados.autor}</p>
        <p>Classificação: {dados.classificacao}</p>
      </Card>
    </>
  );
}
