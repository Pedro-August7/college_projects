import styled from "styled-components";
import { Link } from "react-router-dom";
import { TherapistCard } from "../../components/domain/TherapistCard";

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

const mockTherapists = [
  {
    id: 1,
    name: "Dra. Ana Silva",
    specialty: "Psicologia Clínica",
    rating: 4.9,
    description: "Especialista em ansiedade e depressão com abordagem cognitivo-comportamental.",
  },
  {
    id: 2,
    name: "Dr. Marcos Costa",
    specialty: "Psicanálise",
    rating: 4.7,
    description: "Foco em desenvolvimento pessoal, autoconhecimento e relacionamentos.",
  },
  {
    id: 3,
    name: "Dra. Júlia Mendes",
    specialty: "Terapia Familiar",
    rating: 4.8,
    description: "Atendimento voltado para conflitos familiares e mediação de casais.",
  },
];

export default function PatientDashboard() {
  return (
    <DashboardContainer>
      <Header>
        <Title>Encontrar Terapeutas</Title>
        <BackLink to="/">Sair</BackLink>
      </Header>

      <div>
        {mockTherapists.map((therapist) => (
          <TherapistCard key={therapist.id} name={therapist.name} specialty={therapist.specialty} rating={therapist.rating} description={therapist.description} />
        ))}
      </div>
    </DashboardContainer>
  );
}
