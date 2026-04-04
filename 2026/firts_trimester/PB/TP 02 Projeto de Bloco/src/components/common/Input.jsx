import styled from "styled-components";

const InputWrapper = styled.div`
  display: flex;
  flex-direction: column;
  gap: 6px;
  width: 100%;
  margin-bottom: 16px;
`;

const Label = styled.label`
  font-size: 0.9rem;
  font-weight: 600;
  color: #475569;
`;

const StyledInput = styled.input`
  padding: 14px;
  border: 1px solid #cbd5e1;
  border-radius: 8px;
  font-size: 1rem;
  background-color: #ffffff;
  color: #334155;
  outline: none;
  transition: border-color 0.2s;

  &:focus {
    border-color: #0ea5e9;
  }
`;

export function Input({ label, ...props }) {
  return (
    <InputWrapper>
      {label && <Label>{label}</Label>}
      <StyledInput {...props} />
    </InputWrapper>
  );
}
