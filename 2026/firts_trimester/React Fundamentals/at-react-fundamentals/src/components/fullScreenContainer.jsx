import styled from "styled-components";

const FullScreenContainer = styled.main`
  --color-bg-main: #011627;
  --color-card: #3f617d;
  --color-text-primary: #ffffff;
  --color-border: #4f738f;

  min-height: 100vh;
  width: 100%;

  display: flex;
  justify-content: center;
  align-items: center;

  padding: 16px;

  background-color: var(--color-bg-main);
  color: var(--color-text-primary);

  /* Tablet */
  @media (min-width: 768px) {
    padding: 24px;
  }

  /* Desktop */
  @media (min-width: 1024px) {
    padding: 32px;
  }
`;

const Content = styled.div`
  width: 100%;
  max-width: 1200px;

  margin: 0 auto;

  display: flex;
  flex-direction: column;
  align-items: center;

  gap: 16px;

  /* Tablet */
  @media (min-width: 768px) {
    gap: 24px;
  }

  /* Desktop */
  @media (min-width: 1024px) {
    gap: 32px;
  }
`;

export default function FullscreenContainer({ children }) {
  return (
    <FullScreenContainer>
      <Content>{children}</Content>
    </FullScreenContainer>
  );
}
