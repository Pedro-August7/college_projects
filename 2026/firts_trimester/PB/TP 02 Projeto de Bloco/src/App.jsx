import { BrowserRouter, Routes, Route } from "react-router-dom";

import Login from "./pages/auth/Login";
import PatientDashboard from "./pages/patient/PatientDashboard";
import TherapistDashboard from "./pages/therapist/TherapistDashboard";

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/paciente" element={<PatientDashboard />} />
        <Route path="/terapeuta" element={<TherapistDashboard />} />
      </Routes>
    </BrowserRouter>
  );
}
