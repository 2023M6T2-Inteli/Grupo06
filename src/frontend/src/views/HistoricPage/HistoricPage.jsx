import React, { Fragment, useState } from "react";
import { Row, Col, Table, Card, Button } from "antd";
import { NavBar } from "../../components/NavBar";
import DownloadIcon from "@mui/icons-material/Download";
import { Sidebar } from "../../components/Sidebar";

export default function HistoricPage() {
  const onClick = () => 
  {
    window.open("/SignUp")
  }
  const dataSource = [
    {
      name: "Inspeção rotina 3c Ouro Preto",
      data: "25/05/2023",
      hora: "10:00 - 10:25",
      concO2: "OK",
      concN: "OK",
      concNO2: "OK",
      concAR: "OK",
      download: (
        <Button type="primary">
          {" "}
          <DownloadIcon></DownloadIcon>{" "}
        </Button>
      ),
    },
    {
      name: "Gosigua tubulação geral",
      data: "02/04/2023",
      hora: "15:00 - 15:30",
      concO2: "OK",
      concN: "OK",
      concNO2: "OK",
      concAR: "OK",
      download: (
        <Button type="primary">
          {" "}
          <DownloadIcon></DownloadIcon>{" "}
        </Button>
      ),
    },
    {
      name: "Urgencia Açonorte",
      data: "23/01/2023",
      hora: "13:00 - 13:50",
      concO2: "OK",
      concN: "OK",
      concNO2: "ALTA",
      concAR: "OK",
      download: (
        <Button type="primary">
          {" "}
          <DownloadIcon></DownloadIcon>{" "}
        </Button>
      ),
    },
  ];

  const columns = [
    { title: "Nome da Inspeção", dataIndex: "name", key: "name" },
    {
      title: "Data - Início / Fim",
      title: () => (
        <div>
          <p style={{ margin: "0", display: "inline", float: "left" }}>Data</p>
          <p
            style={{
              margin: "0",
              display: "inline",
              float: "right",
              whiteSpace: "nowrap",
              marginRight: "10px",
            }}
          >
            Início / Fim
          </p>
        </div>
      ),
      render: (_, record) => (
        <div>
          <p style={{ margin: "0", display: "inline", float: "left" }}>
            {record.data}
          </p>
          <p
            style={{
              margin: "0",
              display: "inline",
              float: "right",
              justifyItems: "stretch",
              whiteSpace: "nowrap",
            }}
          >
            {record.hora}
          </p>
        </div>
      ),
      dataIndex: "data",
      key: "data",
    },
    { title: "O2%", dataIndex: "concO2", key: "concO2" },
    { title: "N%", dataIndex: "concN", key: "concN" },
    { title: "NO2%", dataIndex: "concNO2", key: "concNO2" },
    { title: "AR%", dataIndex: "concAR", key: "concAR" },
    {
      title: "Baixar PDF",
      dataIndex: "download",
      key: "download",
      align: "center",
    },
  ];

  return (
    <Fragment>
      <NavBar></NavBar>
      <Row style={{backgroundColor: "#fff"}}>
        <Col span={4}>
          <Sidebar></Sidebar>
        </Col>
        <Col span={20}>
        <Card style={{ padding: 60}}>
          <Row>
            <Col>
              <h1 style={{ color: "black", paddingLeft: "10px" }}>
                Histórico de inspeções
              </h1>
            </Col>
          </Row>
          <Row>
            <Col span={24}>
              <Table
                dataSource={dataSource}
                columns={columns}
                style={{ overflowX: "auto" }}
              />
              <Button type="primary" style={{ backgroundColor: "blue" }} onClick={onClick}>
                Adicionar projeto
              </Button>
            </Col>
          </Row>
        </Card>
        </Col>
      </Row>
    </Fragment>
  );
}
