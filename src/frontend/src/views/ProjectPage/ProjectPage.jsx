import React, { Fragment, useState } from "react";
import Image from "next/image";
import tubo from "../../../public/images/tuboprovisorio.jpg";
import {
  Row,
  Col,
  Card,
  Select,
  Button,
  Space,
} from "antd";
import { Sidebar } from "../../components/Sidebar";
import { NavBar } from "../../components/NavBar";

const { Option } = Select;

export default function ProjectPage() {
  function onFinish(values) {
    // Aqui você pode enviar os dados para uma nova rota
    console.log("Coordenada X:", values.coordinateX);
    console.log("Coordenada Y:", values.coordinateY);

    const data = {
      x: 2.0,
      y: -3.5,
    };

    fetch("http://127.0.0.1:8000/position", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    })
      .then((response) => response.json())
      .then((data) => {
        console.log("Success:", data);
      })
      .catch((error) => {
        console.error("Error:", error);
      });

    fetch("http://127.0.0.1:8000/shape", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    })
      .then((response) => response.json())
      .then((data) => {
        console.log("Success:", data);
      })
      .catch((error) => {
        console.error("Error:", error);
      });

    fetch("http://127.0.0.1:8000/shape", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    })
      .then((response) => response.json())
      .then((data) => {
        console.log("Success:", data);
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  }

  return (
    <Fragment style={{ backgroundColor: "#1D0833" }}>
      <NavBar></NavBar>
      <Row style={{ backgroundColor: "#fff" }}>
        <Col span={4}>
          <Sidebar></Sidebar>
        </Col>
        <Col span={20}>
          <Row justify="left" style={{ backgroundColor: "#fff" }}>
            <Col span={10}>
              <Card
                style={{
                  height: "92%",
                  boxShadow: "0 3px 3px rgba(0,0,0,0.2)",
                  margin: "20px",
                }}
              >
                <h2 style={{ fontWeight: "300", marginBottom: 10 }}>
                  Status do projeto
                </h2>
                <Space
                  direction="vertical"
                  size="large"
                  style={{ display: "flex", marginTop: "20px" }}
                >
                  <Card bordered>
                    <h3 style={{ fontSize: "11px" }}>Concentração de O2:</h3>
                  </Card>
                  <Card bordered>
                    <h3 style={{ fontSize: "11px" }}> Status robô:</h3>
                  </Card>
                  <Card bordered>
                    <h3 style={{ fontSize: "11px" }}> Status operação:</h3>
                  </Card>
                </Space>
                <Row style={{ marginTop: "40px" }}>
                  <Button
                    type="primary"
                    style={{
                      backgroundColor: "red",
                      marginLeft: "5px",
                      marginRight: "10px",
                    }}
                  >
                    Parar
                  </Button>
                  <Button type="primary" style={{ backgroundColor: "green" }}>
                    Continuar
                  </Button>
                </Row>
              </Card>
            </Col>
            <Col span={14} justify="right">
              <Card
                align="center"
                style={{
                  boxShadow: "0 3px 3px rgba(0,0,0,0.2)",
                  margin: "20px",
                }}
              >
                <h2 style={{ fontWeight: "300", marginBottom: 10 }}>
                  Visualização da camera
                </h2>
                <Image
                  width={500}
                  src={tubo}
                  style={{ borderRadius: 50, border: "1px solid #000" }}
                ></Image>
              </Card>
            </Col>
          </Row>
          <Row justify="center">
            <Card
              style={{
                width: "90%",
                boxShadow: "0 3px 3px rgba(0,0,0,0.2)",
                margin: "20px",
              }}
            >
              <Row justify="center">
              <h2 style={{ fontWeight: "300", marginBottom: 10 }}>
                Informações do projeto
              </h2>
              </Row>
              <Space
                direction="vertical"
                size="middle"
                style={{ display: "flex" }}
              >
                <Card bordered>
                  <h3 style={{ fontSize: "11px" }}>Titulo:</h3>
                </Card>
                <Card bordered>
                  <h3 style={{ fontSize: "11px" }}> tipo de área:</h3>
                </Card>
                <Card bordered>
                  <h3 style={{ fontSize: "11px" }}> Responsável:</h3>
                </Card>
                <Card bordered>
                  <h3 style={{ fontSize: "11px" }}> Prazo:</h3>
                </Card>
              </Space>
            </Card>
          </Row>
        </Col>
      </Row>
    </Fragment>
  );
}
