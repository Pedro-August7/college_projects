import { Card } from "../../../components/Card";

export default function TodoItem({ todo }) {
  const estiloTexto = {
    textDecoration: todo.completed ? "line-through" : "none",
    color: todo.completed ? "#94a3b8" : "#ffffff",
    transition: "all 0.3s ease",
  };

  const corCard = todo.completed ? "#16a34a" : "#3f617d";

  return (
    <Card corFundo={corCard}>
      <div style={{ display: "flex", alignItems: "center", gap: "12px" }}>
        <input type="checkbox" checked={todo.completed} readOnly style={{ width: "20px", height: "20px", cursor: "default" }} />
        <span style={estiloTexto}>{todo.title}</span>
      </div>
    </Card>
  );
}
