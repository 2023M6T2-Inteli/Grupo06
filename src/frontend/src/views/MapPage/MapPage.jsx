import React, { Fragment, useState, useEffect, useRef } from "react";
import { Row, Col, Table, Card, Button} from "antd";
import { NavBar } from "../../components/NavBar";
//import DownloadIcon from "@mui/icons-material/Download";
//import BotControllerNav from "../../../../simulation/.vscode";

export default function MapPage() {
  const Canvas = () => {
    
    const canvasRef = useRef(null);
    const canvas_width = 800;
    const canvas_height = 600;

    let position = 0
    let pos_x = 10
    let pos_y = 10

    useEffect(() => {
      const canvas = canvasRef.current
      const ctx = canvas.getContext('2d')

      var img = new Image();
      img.src = "down-arrow.png";

      const draw_player = (pos_x, pos_y) => {
        ctx.fillStyle = 'green';
        ctx.fillRect(pos_x, pos_y, 20, 20);
      }
      
      const animation = () => {
        ctx.clearRect(0, 0, canvas_width, canvas_height);
        draw_player(pos_x, pos_y);
        requestAnimationFrame(animation);
      }

      animation();
    });

    return(
          <div style={{display:"flex", justifyContent:"center", alignItems:"center"} }>
          <canvas ref={canvasRef} width={canvas_width} height={canvas_height} />;
          </div>
    );
  };


  return (
    <Fragment>
        <NavBar></NavBar>
        <Card style={{padding: 50}}>
        <Canvas></Canvas>
        </Card>

    </Fragment>
  );
}