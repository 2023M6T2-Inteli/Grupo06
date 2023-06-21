import React, { Fragment, useState, useEffect } from "react";
import { Row, Col, Table, Card, Button } from "antd";
import { NavBar } from "../../components/NavBar";
import DownloadIcon from "@mui/icons-material/Download";
import { Sidebar } from "../../components/Sidebar";
import {
  PlusOutlined
} from "@ant-design/icons";

export default function HistoricPage() {
  const [data, setData] = useState([]);
  const [columns, setColumns] = useState([]);
  const onClicks = () => {
    window.open("/SignUp");
  };
  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = () => {
    fetch("http://127.0.0.1:3001/report")
      .then(response => response.json())
      .then(data => {
        console.log(data.reports);
        setColumns(data.reports)
        if (Array.isArray(data)) {
          setData(data);
        } else {
          setData([]);
        }
      })
      .catch(error => {
        console.error("Erro:", error);
      });
  };

  const items = [
    { title: "Nome da Inspeção", dataIndex: "reportName", key: "reportName" },
    { title: "Opção de area", dataIndex: "typePlace", key: "typePlace" },
    { title: "Responsável", dataIndex: "operator", key: "operator" },
    { title: "Visualizar", key: "view",
    render: (_, record) => (
      <Button
        type="primary"
        shape = "circle"
        onClick={() => handleView(record)}
        //função aleatória para chamar quando clickar
        icon = {<PlusOutlined />}
      >
      </Button>
    ),
  },
  ];

  return (
    <Fragment>
      <NavBar></NavBar>
      <Row style={{ backgroundColor: "#fff" }}>
        <Col span={4}>
          <Sidebar></Sidebar>
        </Col>
        <Col span={20}>
          <Card style={{ padding: 60, width: "90%" }}>
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
                  dataSource={columns}
                  columns={items}
                  style={{maxHeight: "400px"}}
                  scroll={{ y: 400 }}
                />
                <Button
                  type="primary"
                  style={{ backgroundColor: "blue", marginTop:"80px" }}
                  onClick={onClicks}
                >
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