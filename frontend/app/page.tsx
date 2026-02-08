import { getGameMessage } from "./games/snake/SnakeGame";

export default function HomePage() {
  return (
    <div>
      <h1>{getGameMessage()}</h1>
    </div>

    
  );
}

