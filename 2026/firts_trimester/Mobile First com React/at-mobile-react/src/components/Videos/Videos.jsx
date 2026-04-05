import styles from "./Videos.module.css";

export default function Videos() {
  const videos = [
    {
      id: "v1",
      youtubeId: "5zLq7jXwd7Q",
      titulo: "Dr. Enéas - Congresso Mineiro",
    },
    {
      id: "v2",
      youtubeId: "pmxTbANqGJI",
      titulo: "Dr. Enéas - 1989 - Trecho de coletiva de imprensa",
    },
    {
      id: "v3",
      youtubeId: "54CXNpeUWgM",
      titulo: " Dr. Enéas em 89 - P03 - Político Profissional - 15 segundos ",
    },
  ];

  return (
    <section id="videos" className={styles.container}>
      <h2 className={styles.titulo}>Vídeos da Campanha</h2>

      <div className={styles.grid}>
        {videos.map((video) => (
          <div key={video.id} className={styles.videoWrapper}>
            <iframe
              src={`https://www.youtube.com/embed/${video.youtubeId}`}
              title={video.titulo}
              loading="lazy"
              allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
              allowFullScreen
            />
          </div>
        ))}
      </div>
    </section>
  );
}
