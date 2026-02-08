"use client";

import { useRef, useEffect } from "react";

const tileSize = 32;
const rowCount = 21;
const columnCount = 19;
const boardWidth = columnCount * tileSize;
const boardHeight = rowCount * tileSize;
const head: tile = {
  x: 300,
  y: 300,
  width: tileSize,
  height: tileSize,
  color: "red",
};
type tile = {
  x: number;
  y: number;
  width: number;
  height: number;
  color: string;
};

export default function SnakeGame() {
  const canvasRef = useRef<HTMLCanvasElement | null>(null);

  useEffect(() => {
    function handleKeyDown(event: KeyboardEvent) {
      if (event.key == "ArrowUp") {
        alert("We are about to increment");
        head.y += 50;
        alert("We incremented");
      }
    }

    class Node<T> {
      public data: T;
      public next: Node<T> | null;
      constructor(data: T, next: Node<T> | null) {
        this.data = data;
        this.next = next;
      }
    }

    const board = canvasRef.current;
    if (!board) return;
    board.height = boardHeight;
    board.width = boardWidth;

    window.addEventListener("keydown", handleKeyDown);

    const context = board.getContext("2d");
    draw(head);
    const top = new Node<tile>(head, null);
    console.log("Canvas is Open and Ready!");

    function draw(item: tile) {
      if (!context) return;
      context.fillStyle = item.color;
      context.fillRect(item.x, item.y, item.width, item.height);
    }
  }, []);
  return <canvas ref={canvasRef} id="snake" />;
}
