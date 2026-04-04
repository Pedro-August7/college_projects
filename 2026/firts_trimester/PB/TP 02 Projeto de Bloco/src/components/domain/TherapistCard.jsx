import styled from "styled-components";
import { Button } from "../common/Button";

const CardContainer = styled.div`
  background-color: #ffffff;
  border: 1px solid #e2e8f0;
  border-radius: 12px;
  padding: 16px;
  margin-bottom: 16px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.02);
`;

const Header = styled.div`
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 12px;
`;

const Name = styled.h3`
  font-size: 1.1rem;
  color: #0f172a;
  margin-bottom: 4px;
`;

const Specialty = styled.span`
  font-size: 0.85rem;
  color: #0ea5e9;
  background-color: #e0f2fe;
  padding: 4px 8px;
  border-radius: 12px;
  font-weight: 600;
`;

const Rating = styled.div`
  font-size: 0.9rem;
  color: #eab308;
  font-weight: bold;
`;

const Description = styled.p`
  font-size: 0.9rem;
  color: #64748b;
  line-height: 1.4;
  margin-bottom: 16px;
`;

export function TherapistCard({ name, specialty, rating, description }) {
  return (
    <CardContainer>
      <Header>
        <div>
          <Name>{name}</Name>
          <Specialty>{specialty}</Specialty>
        </div>
        <Rating>★ {rating}</Rating>
      </Header>
      <Description>{description}</Description>
      <Button>Ver Perfil</Button>
    </CardContainer>
  );
}
