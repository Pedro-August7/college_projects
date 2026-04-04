import { useState } from "react";
import styled from "styled-components";
import { FaArchive, FaTrash, FaEdit } from "react-icons/fa";

const Wrapper = styled.div`
  position: relative;
  width: 100%;
  margin-bottom: 16px;
  overflow: hidden;
  border-radius: 12px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.02);
`;

const ActionsContainer = styled.div`
  position: absolute;
  top: 0;
  right: 0;
  height: 100%;
  display: flex;
  background-color: #f1f5f9;
`;

const ActionButton = styled.button`
  height: 100%;
  width: 60px;
  display: flex;
  justify-content: center;
  align-items: center;
  color: white;
  background-color: ${(props) => props.$color || "#94a3b8"};
  font-size: 1.2rem;
`;

const Card = styled.div`
  position: relative;
  background-color: #ffffff;
  padding: 16px;
  border: 1px solid #e2e8f0;
  border-radius: 12px;
  width: 100%;
  z-index: 2;
  transition: transform 0.2s ease-out;
  transform: translateX(${(props) => props.$offset}px);
`;

const Header = styled.div`
  display: flex;
  justify-content: space-between;
  margin-bottom: 8px;
`;

const PatientName = styled.h3`
  font-size: 1.1rem;
  color: #0f172a;
`;

const DateText = styled.span`
  font-size: 0.85rem;
  color: #64748b;
`;

const Notes = styled.p`
  font-size: 0.9rem;
  color: #475569;
  line-height: 1.4;
`;

export function SessionCard({ patientName, date, notes }) {
  const [offset, setOffset] = useState(0);
  const [startX, setStartX] = useState(0);

  const handleTouchStart = (e) => {
    setStartX(e.touches[0].clientX);
  };

  const handleTouchMove = (e) => {
    const currentX = e.touches[0].clientX;
    const diff = currentX - startX;
    if (diff < 0 && diff > -180) {
      setOffset(diff);
    }
  };

  const handleTouchEnd = () => {
    if (offset < -90) {
      setOffset(-180);
    } else {
      setOffset(0);
    }
  };

  return (
    <Wrapper>
      <ActionsContainer>
        <ActionButton $color="#eab308">
          <FaEdit />
        </ActionButton>
        <ActionButton $color="#0ea5e9">
          <FaArchive />
        </ActionButton>
        <ActionButton $color="#ef4444">
          <FaTrash />
        </ActionButton>
      </ActionsContainer>
      <Card $offset={offset} onTouchStart={handleTouchStart} onTouchMove={handleTouchMove} onTouchEnd={handleTouchEnd}>
        <Header>
          <PatientName>{patientName}</PatientName>
          <DateText>{date}</DateText>
        </Header>
        <Notes>{notes}</Notes>
      </Card>
    </Wrapper>
  );
}
