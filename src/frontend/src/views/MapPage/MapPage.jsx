import React, { Fragment, useState, useEffect, useRef } from "react";
import { Row, Col, Table, Card, Button} from "antd";
import { NavBar } from "../../components/NavBar";
import DownloadIcon from "@mui/icons-material/Download";
//import BotControllerNav from "../../../../simulation/.vscode";
import {createClient} from "@supabase/supabase-js";
import { Inter } from "next/font/google";

const url = "https://etxrmfvkgcrpyzdpvvrn.supabase.co"
const key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImV0eHJtZnZrZ2NycHl6ZHB2dnJuIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTY4NjY4MDk4MCwiZXhwIjoyMDAyMjU2OTgwfQ.BosLYjeNsyNMhs88FlV_PNzH9QRBqeBgAUJJU4SzlQw"
const supabase = createClient(url, key)

export default function MapPage() {
  const Canvas = () => {

    const canvasRef = useRef(null);
    const canvas_width = 900;
    const canvas_height = 450;
    const canvas_mid_width = canvas_width / 2;
    const canvas_mid_height = canvas_height / 2;
    
    useEffect(() => {
      const canvas = canvasRef.current
      const ctx = canvas.getContext('2d');

      const draw_player = (px, py) => {
        ctx.fillStyle = 'green';
        console.log("Drawing player at: (" + px + ", " + py + ")");
        ctx.fillRect(px, py, 20, 20);
    }

    let first_time = true;
    let position = {"x": 0.00, "y": 0.00, "theta": 0.00};
    let first_position = {...position};

    var get_position = async () => {

      const { data, res } = await supabase.from('Coordinates').select()

      if (data && data.length > 0) {
        
        const last_data = data[data.length - 1]
        position = {...last_data}*10

        console.log("Position: ("+ position.x + ", " + position.y + ", " + position.theta + ")")

        for(var i=0; i < data.length; i++){
          const actual_data = data[i]
          const { res } = await supabase.from('Coordinates').delete().eq("id", actual_data.id)
        }

        if (first_time) {
          first_position.x = position.x;
          first_position.y = position.y;
          first_time = false;
        }
      }
    }
    
    const animation = () => {
      ctx.clearRect(0, 0, canvas_width, canvas_height);
      get_position();

      const posX = position.x - first_position.x + canvas_mid_width;
      const posY = position.y - first_position.y + canvas_mid_height;
      const posT = position.theta + first_position.theta;

      draw_player(posX, posY);
      requestAnimationFrame(animation);
    }

    animation();
  });

  return(
        <div style={{display:"flex", justifyContent:"center", alignItems:"center"} }>
        <canvas ref={canvasRef} width={canvas_width} height={canvas_height} />
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