import React, { useState } from "react";
import Image from "next/image";
import { Row, Col, Card, Form, Input, Select, Button, Tooltip } from "antd";
import { QuestionCircleOutlined } from "@ant-design/icons";
import { NavBar } from "../../components/NavBar";

const { Option } = Select;

import Logo from "../../../public/images/logo_lincore.png";

export default function SignUpPage() {
  const [form] = Form.useForm();
  const [loading, setLoading] = useState(false);

  const onFinish = (values) => {
    setLoading(true);
    console.log(JSON.stringify(values));
    fetch('http://127.0.0.1:3001/report', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(values),
    })
      .then(response => {
        console.log(response);
        return response.json(); // retorna a promessa para tratamento posterior
      })
      .then(data => {
        console.log(data);
        setLoading(false);
        window.open("/project");
      })
      .catch(error => {
        console.error('Erro:', error);
        setLoading(false);
      });
  };

  return (
    <>
      <Row
        justify="center"
        style={{ height: "100vh", backgroundColor: "#1D0833", padding: 100 }}
      >
        <Col xs={24} md={12}>
          <Card style={{ boxShadow: "0 3px 3px rgba(0,0,0,0.2)" }}>
            <Row justify='center'>
              <Image width={200} src={Logo}></Image>
            </Row>
            <h1 style={{ textAlign: "center" }}>Cadastro de Projeto </h1>
            <Form form={form} onFinish={onFinish}>
              <Form.Item
                labelCol={{ span: 24 }}
                wrapperCol={{ span: 24 }}
                name="reportName"
                label={
                  <span>
                    Título do Projeto&nbsp;
                    <Tooltip title="Informe o título do seu projeto">
                      <QuestionCircleOutlined />
                    </Tooltip>
                  </span>
                }
                rules={[
                  {
                    required: true,
                    message: "Por favor, informe o título do seu projeto",
                  },
                ]}
              >
                <Input />
              </Form.Item>
              <Form.Item
                labelCol={{ span: 24 }}
                wrapperCol={{ span: 24 }}
                name="typePlace"
                label={
                  <span>
                    Tipo de Área Analisada&nbsp;
                    <Tooltip title="Selecione o tipo de área que será analisada no seu projeto">
                      <QuestionCircleOutlined />
                    </Tooltip>
                  </span>
                }
                rules={[
                  {
                    required: true,
                    message: "Por favor, selecione o tipo de área analisada",
                  },
                ]}
              >
                <Select>
                  <Option value={1}>Opção 1</Option>
                  <Option value={2}>Opção 2</Option>
                  <Option value={3}>Opção 3</Option>
                </Select>
              </Form.Item>
              <Form.Item
                labelCol={{ span: 24 }}
                wrapperCol={{ span: 24 }}
                name="operator"
                label={
                  <span>
                    Responsável pela Atividade&nbsp;
                    <Tooltip title="Informe o nome do responsável pela atividade">
                      <QuestionCircleOutlined />
                    </Tooltip>
                  </span>
                }
                rules={[
                  {
                    required: true,
                    message:
                      "Por favor, informe o nome do responsável pela atividade",
                  },
                ]}
              >
                <Input />
              </Form.Item>
              <Row justify="end">
                <Form.Item>
                  <Button type="primary" htmlType="submit">
                    Enviar
                  </Button>
                </Form.Item>
              </Row>
            </Form>
          </Card>
        </Col>
      </Row>
    </>
  );
}
