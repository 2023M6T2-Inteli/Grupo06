import React, { Fragment, useState } from "react";
import { Row, Col, Table, Card, Button} from "antd";
import { NavBar } from "../../components/NavBar";
import DownloadIcon from "@mui/icons-material/Download";

export default function HistoricPage() {
  const dataSource = [
    { name: "Inspeção rotina 3c Ouro Preto", data: "25/05/2023", hora: "10:00", concO2: "16%", concN: "78%", download: <Button type="primary"> <DownloadIcon></DownloadIcon> </Button>},
    { name: "Gosigua tubulação geral", data: "02/04/2023", hora: "15:00", concO2: "13%", concN: "75%", download: <Button type="primary"> <DownloadIcon></DownloadIcon> </Button>},
    { name: "Urgencia Açonorte", data: "23/01/2023", hora: "13:00", concO2: "2%", concN: "93%", download: <Button type="primary"> <DownloadIcon></DownloadIcon> </Button>},
  ];

  const columns = [
    { title: "Nome da Inspeção", dataIndex: "name", key: "name"},
    { title: "Data", dataIndex: "data", key: "data" },
    { title: "Hora", dataIndex: "hora", key: "hora" },
    { title: "O2%", dataIndex: "concO2", key: "concO2" },
    { title: "N%", dataIndex: "concN", key: "concN"},
    { title: "Baixar PDF", dataIndex: "download", key: "download", align: "center"}
  ];

  return (
    <Fragment>
        <NavBar></NavBar>

        <Card>
        <Row>
            <Col>
                <h1 style={{color:"black", paddingLeft:"10px"}}>Histórico de inspeções</h1>
            </Col>
        </Row>

        <Row>
            <Col span ={24}>
                <Table dataSource={dataSource} columns={columns} style={{overflowX:"auto"}}/>
            </Col>
        </Row>
        </Card>

    </Fragment>
  );
}
