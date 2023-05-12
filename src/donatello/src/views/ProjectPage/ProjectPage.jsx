import React, { Fragment, useState } from "react";
import Image from "next/image";
import {
  Row,
  Col,
  Card,
  Form,
  Input,
  Select,
  Button,
  Tooltip,
  Space,
  Divider,
} from "antd";
import {
  QuestionCircleOutlined,
  PlayCircleOutlined,
  PauseCircleOutlined,
} from "@ant-design/icons";
import VideocamIcon from "@mui/icons-material/Videocam";
import VideocamOffIcon from "@mui/icons-material/VideocamOff";
import PlayArrowIcon from "@mui/icons-material/PlayArrow";
import PauseIcon from "@mui/icons-material/Pause";
import { NavBar } from "../../components/NavBar";

import Camera from "../../../public/images/camera.png";
import Turtlebot from "../../../public/images/turtlebot.png";
import Simulation from "../../../public/images/simulation.png";

const { Option } = Select;

export default function ProjectPage() {
  return (
    <Fragment style={{ backgroundColor: "#1D0833" }}>
      <NavBar></NavBar>
      <Row justify="center" style={{ padding: "2%", backgroundColor: "#fff" }}>
        <Row align="bottom">
          <Col span={8}>
            <Row justify="start">
              <Image width={100} src={Turtlebot}></Image>
            </Row>
            <Row>
              <p style={{ fontSize: "24pt" }}>Rota Tubo 3c Ouro Branco</p>
            </Row>
            <Space>
              <Button type="primary" href="http://127.0.0.1:8000/shape" >G</Button>
            <Button type="primary" href="http://127.0.0.1:8000/shape" >□</Button>
            <Button type="primary" href="http://127.0.0.1:8000/position">Ponto</Button>
            </Space>
            <Row justify="start">
              <h1>
                <VideocamIcon style={{ fontSize: "42pt" }} />
              </h1>
              <h1>
                <VideocamOffIcon style={{ fontSize: "42pt" }} />
              </h1>
              <h1>
                <PlayArrowIcon style={{ fontSize: "42pt" }} />
              </h1>
              <h1>
                <PauseIcon style={{ fontSize: "42pt" }} />
              </h1>
            </Row>
          </Col>
          <Col span={15}>
            <Row justify="end">
              <Image width={750} src={Camera}></Image>
            </Row>
          </Col>
        </Row>
      </Row>
      <Row
        justify="center"
        style={{ padding: "2%", backgroundColor: "#1D0833" }}
      >
        <Card style={{ width: "80%", boxShadow: "0 3px 3px rgba(0,0,0,0.2)" }}>
          <h2 style={{ fontWeight: "300", marginBottom: 10 }}>
            Características do Projeto
          </h2>
          <Space direction="vertical" size="middle" style={{ display: "flex" }}>
            <Card bordered></Card>
            <Card bordered></Card>
            <Card bordered></Card>
            <Card bordered></Card>
            <Card bordered></Card>
          </Space>
        </Card>
      </Row>
      <Row justify="center" style={{ backgroundColor: "#1D0833" }}>
        <h1 style={{ fontWeight: "300", textAlign: "center", color: "#fff" }}>
          Análise de Gases do Ambiente <Divider></Divider>
        </h1>
      </Row>
      <Row
        justify="center"
        style={{ padding: "2%", backgroundColor: "#1D0833" }}
      >
        <Space direction="horizontal" size="middle" style={{ display: "flex" }}>
          <Col>
            <Card
              bordered
              style={{
                width: "20vw",
                backgroundColor: "black",
                height: "25vh",
                boxShadow: "0 3px 3px rgba(0,0,0,0.2)",
                background:
                  "radial-gradient(circle, rgba(103,2,2,1) 0%, rgba(56,1,1,1) 100%)",
              }}
            >
               <Row justify='center'>
                <h1 style={{color:"#fff"}}>O2</h1>
              </Row>
              <Row justify='center'>
                <h1 style={{fontSize:"54pt", color:"#fff"}}>30%</h1>
              </Row>
            </Card>
          </Col>
          <Col>
            <Card
              bordered
              style={{
                width: "20vw",
                height: "25vh",
                boxShadow: "0 3px 3px rgba(0,0,0,0.2)",
                background:
                  "radial-gradient(circle, rgba(226,149,5,1) 0%, rgba(98,63,5,1) 100%)",
              }}
            >
               <Row justify='center'>
                <h1 style={{color:"#fff"}}>O2</h1>
              </Row>
              <Row justify='center'>
                <h1 style={{fontSize:"54pt", color:"#fff"}}>30%</h1>
              </Row>
            </Card>
          </Col>
          <Col>
            <Card
              bordered
              style={{
                width: "20vw",
                height: "25vh",
                boxShadow: "0 3px 3px rgba(0,0,0,0.2)",
                background:
                  "radial-gradient(circle, rgba(103,2,2,1) 0%, rgba(56,1,1,1) 100%)",
              }}
            >
              <Row justify="center">
                <h1 style={{ color: "#fff" }}>O2</h1>
              </Row>
              <Row justify="center">
                <h1 style={{ fontSize: "54pt", color: "#fff" }}>30%</h1>
              </Row>
            </Card>
          </Col>
          <Col>
            <Card
              bordered
              style={{
                width: "20vw",
                height: "25vh",
                boxShadow: "0 3px 3px rgba(0,0,0,0.2)",
                background:
                  "radial-gradient(circle, rgba(42,135,7,1) 0%, rgba(19,45,0,1) 100%)",
              }}
            >
              <Row justify="center">
                <h1 style={{ color: "#fff" }}>O2</h1>
              </Row>
              <Row justify="center">
                <h1 style={{ fontSize: "54pt", color: "#fff" }}>30%</h1>
              </Row>
            </Card>
          </Col>
        </Space>
      </Row>
      <Row
        justify="center"
        style={{ paddingBottom: "5%", backgroundColor: "#1D0833" }}
      >
        <Card style={{ width: "80%", boxShadow: "0 3px 3px rgba(0,0,0,0.2)" }}>
          <Row align="bottom">
            <Col>
              <Image
                width={700}
                src={Simulation}
                style={{ borderRadius: 50 }}
              ></Image>
            </Col>
            <Col style={{ padding: 15 }}>
              <p style={{ fontSize: "18pt" }}>Simulação: 2634</p>
              <p style={{ fontSize: "18pt" }}>
                Projeto: Rota Tubo 3c Ouro branco
              </p>
              <p style={{ fontSize: "18pt" }}>Software: TurtleBot</p>
              <p style={{ fontSize: "18pt" }}>Data de Atualização: DD/MM/AA</p>
              <p style={{ fontSize: "18pt" }}>Hora de Atualização: HH:MM:SS</p>
            </Col>
          </Row>
        </Card>
      </Row>
    </Fragment>
  );
}
