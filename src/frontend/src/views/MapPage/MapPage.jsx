import React, { Fragment, useState, useEffect, useRef } from "react";
import { Row, Col, Table, Card, Button} from "antd";
import { NavBar } from "../../components/NavBar";
import DownloadIcon from "@mui/icons-material/Download";

export default function MapPage() {
  const Canvas = () => {
    
    const canvasRef = useRef(null);
    const canvas_width = 800;
    const canvas_height = 600;
    
    useEffect(() => {
      const canvas = canvasRef.current.getContext('2d');
      canvas.fillStyle = 'darkblue';
      canvas.fillRect(0, 0, canvas_width, canvas_height);
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