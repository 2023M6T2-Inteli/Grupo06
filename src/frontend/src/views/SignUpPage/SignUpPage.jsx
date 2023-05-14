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
    // Aqui você pode adicionar a lógica para salvar o projeto
    console.log(values);
    setLoading(false);
    window.open("/project");
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
                name="titulo"
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
                name="tipo"
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
                  <Option value="opcao1">Opção 1</Option>
                  <Option value="opcao2">Opção 2</Option>
                  <Option value="opcao3">Opção 3</Option>
                </Select>
              </Form.Item>
              <Form.Item
                labelCol={{ span: 24 }}
                wrapperCol={{ span: 24 }}
                name="responsavel"
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
