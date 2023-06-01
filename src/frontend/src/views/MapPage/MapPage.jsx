import React, { Fragment, useState, useEffect, useRef } from "react";
import { Row, Col, Table, Card, Button} from "antd";
import { NavBar } from "../../components/NavBar";
import DownloadIcon from "@mui/icons-material/Download";

export default function MapPage() {
  const Canvas = () => {
    
    const canvasRef = useRef(null);
    
    useEffect(() => {
      const canvas = canvasRef.current;
      const context = canvas.getContext('2d');
      
      // Draw on the canvas
      context.fillStyle = 'red';
      context.fillRect(10, 10, 100, 100);
    }, []);
    return<div style={{display:"flex", justifyContent:"center", alignItems:"center"} }>
    <canvas ref={canvasRef} width={800} height={400} />;
    </div>;
  };

  return (
    <Fragment>
        <NavBar></NavBar>

        <Card style={{padding: 150}}>
        <Canvas></Canvas>
        </Card>

    </Fragment>
  );
}
