import { Card } from "../../../components/Card";

export default function PostItem({ post }) {
  return (
    <Card>
      <h3 style={{ textTransform: "capitalize", marginBottom: "10px", color: "#4ade80" }}>{post.title}</h3>
      <p style={{ lineHeight: "1.5", fontSize: "0.9rem", color: "#e2e8f0" }}>{post.body}</p>
    </Card>
  );
}
