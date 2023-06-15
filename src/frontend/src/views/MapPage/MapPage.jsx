import React, { Fragment, useState, useEffect, useRef } from "react";
import { Row, Col, Table, Card, Button} from "antd";
import { NavBar } from "../../components/NavBar";
import DownloadIcon from "@mui/icons-material/Download";
import BotControllerNav from "../../../../simulation/.vscode";
import {createClient} from "@supabase/supabase-js";

const url = "https://etxrmfvkgcrpyzdpvvrn.supabase.co"
const key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImV0eHJtZnZrZ2NycHl6ZHB2dnJuIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTY4NjY4MDk4MCwiZXhwIjoyMDAyMjU2OTgwfQ.BosLYjeNsyNMhs88FlV_PNzH9QRBqeBgAUJJU4SzlQw"
const supabase = createClient(url, key)

export default function MapPage() {
  const Canvas = () => {

    const canvasRef = useRef(null);
    const canvas_width = 800;
    const canvas_height = 600;

    let position_X = 0
    let position_Y = 0
    
    useEffect(() => {
      const canvas = canvasRef.current
      const ctx = canvas.getContext('2d');

      const draw_player = (px, py) => {
        ctx.fillStyle = 'green';
        ctx.fillRect(px, py, 20, 20);
      }

      const get_position = async () => {
        
        const { data, error } = await supabase
        .from('Coordinates')
        .select()

        console.log(data)

      }
      
      const animation = () => {
        ctx.clearRect(0, 0, canvas_width, canvas_height);
        draw_player(position_X, position_Y);
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