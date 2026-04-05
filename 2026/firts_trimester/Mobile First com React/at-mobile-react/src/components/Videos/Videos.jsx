import styles from "./Videos.module.css";

export default function Videos() {
  const videos = [
    {
      id: "v1",
      youtubeId: "dQw4w9WgXcQ",
      titulo: "Discurso Histórico",
    },
    {
      id: "v2",
      youtubeId: "3GwjfUFyY6M",
      titulo: "Entrevista Clássica",
    },
    {
      id: "v3",
      youtubeId: "kJQP7kiw5Fk",
      titulo: "Momento de Campanha",
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
