import styled from "styled-components";
import { Link } from "react-router-dom";
import { SessionCard } from "../../components/domain/SessionCard";

const DashboardContainer = styled.div`
  padding: 20px;
  padding-bottom: 40px;
`;

const Header = styled.header`
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 24px;
`;

const Title = styled.h2`
  color: #0f172a;
  font-size: 1.5rem;
`;

const BackLink = styled(Link)`
  color: #64748b;
  font-size: 0.9rem;
`;

const HelperText = styled.p`
  font-size: 0.85rem;
  color: #64748b;
  margin-bottom: 20px;
  text-align: center;
`;

const mockSessions = [
  {
    id: 1,
    patientName: "Carlos Silva",
    date: "21 Fev 2026 - 14:00",
    notes: "Paciente relatou melhora nos quadros de ansiedade após início das atividades físicas.",
  },
  {
    id: 2,
    patientName: "Mariana Souza",
    date: "20 Fev 2026 - 10:30",
    notes: "Sessão focada em resolução de conflitos no ambiente de trabalho.",
  },
  {
    id: 3,
    patientName: "Roberto Alves",
    date: "18 Fev 2026 - 16:00",
    notes: "Revisão das metas estabelecidas no mês anterior.",
  },
];

export default function TherapistDashboard() {
  return (
    <DashboardContainer>
      <Header>
        <Title>Gestão de Sessões</Title>
        <BackLink to="/">Sair</BackLink>
      </Header>

      <HelperText>Deslize o card para a esquerda para ver as opções</HelperText>

      <div>
        {mockSessions.map((session) => (
          <SessionCard key={session.id} patientName={session.patientName} date={session.date} notes={session.notes} />
        ))}
      </div>
    </DashboardContainer>
  );
}
