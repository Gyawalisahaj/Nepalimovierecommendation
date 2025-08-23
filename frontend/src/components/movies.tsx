interface Movie {
  title: string;
  genre: string;
  image_url?: string;
  video_url?: string;
}

interface MovieDescriptionProps {
  movie: Movie;
}

export default function MovieList({ movie }: MovieDescriptionProps) {
  return (
    <div className="shadow-md p-4 w-80 h-auto rounded-2xl border-8 border-[#6D271B] bg-[#F2ECE3]">
      <h2 className="text-2xl font-bold text-orange-800 mb-2">{movie.title}</h2>
      <div className="bg-orange-200 rounded-2xl text-orange-800 border ">
        <p className="m-2"><strong>Genre:</strong> {movie.genre}</p>
        {movie.image_url && (
          movie.video_url ? (
            <a href={movie.video_url} target="_blank" rel="noopener noreferrer">
              <img
                src={movie.image_url}
                alt={movie.title}
                className="mt-3 rounded-md w-full"
              />
            </a>
          ) : (
            <img
              src={movie.image_url}
              alt={movie.title}
              className="mt-3 rounded-md w-full opacity-60"
            />
          )
        )}
      </div>
    </div>
  );
}