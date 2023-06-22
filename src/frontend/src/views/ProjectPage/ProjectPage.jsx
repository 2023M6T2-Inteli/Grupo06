import React, { Fragment, useState } from "react";
import Image from "next/image";
import tubo from "../../../public/images/tuboprovisorio.jpg";
import Cookies from 'js-cookie';
import {
  Row,
  Col,
  Card,
  Select,
  Button,
  Space,
  Carousel
} from "antd";
import { Sidebar } from "../../components/Sidebar";
import { NavBar } from "../../components/NavBar";

const { Option } = Select;

export default function ProjectPage() {
  const [content, setContent] = useState({});
  const cookieValue = Cookies.get('projectID');
  console.log(cookieValue);

  fetch(`http://127.0.0.1:3001/report/${cookieValue}`, {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json',
    },
  })
    .then((response) => response.json())
    .then((data) => {
      setContent(data.report)
      console.log(content)
      console.log('Success:', data);
    })

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
                  <Button type="primary" style={{ backgroundColor: "blue" }} onClick={() => finalizarProjeto(record)}>
                    Finalizar projeto
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
                <Carousel autoplay>
                  {content.images && content.images.map((image) => (
                      <img src={image.url}/>
                  ))}
                </Carousel>
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
