import styled from "styled-components";

export const Button = styled.button`
  width: 100%;
  padding: 14px;
  background-color: ${(props) => (props.$variant === "secondary" ? "#10b981" : "#0ea5e9")};
  color: white;
  border-radius: 8px;
  font-size: 1rem;
  font-weight: bold;
  transition: opacity 0.2s;
  margin-bottom: 10px;

  &:active {
    opacity: 0.8;
  }
`;
