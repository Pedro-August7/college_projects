import styled from "styled-components";

const CardContainer = styled.div`
  background-color: ${(props) => props.corFundo || "#3f617d"};
  color: #ffffff;

  padding: 16px;
  border-radius: 12px;

  display: flex;
  flex-direction: column;
  gap: 12px;

  width: 100%;
  max-width: 400px;

  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.25);

  transition:
    transform 0.2s ease,
    box-shadow 0.2s ease;

  &:hover {
    transform: translateY(-4px);
    box-shadow: 0 8px 18px rgba(0, 0, 0, 0.35);
  }

  @media (min-width: 768px) {
    padding: 20px;
  }

  @media (min-width: 1024px) {
    padding: 24px;
  }
`;

export function Card({ children, corFundo }) {
  return (
    <>
      <CardContainer corFundo={corFundo}>{children}</CardContainer>
    </>
  );
}
