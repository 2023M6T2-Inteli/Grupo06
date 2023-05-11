import React,{ useState } from 'react'
import Image from 'next/image';
import { Row, Col, Card, Form, Input, Select, Button, Tooltip, Space, Divider } from 'antd';
import { QuestionCircleOutlined, PlayCircleOutlined, PauseCircleOutlined } from '@ant-design/icons';
import VideocamIcon from '@mui/icons-material/Videocam';
import VideocamOffIcon from '@mui/icons-material/VideocamOff';
import PlayArrowIcon from '@mui/icons-material/PlayArrow';
import PauseIcon from '@mui/icons-material/Pause';
import { NavBar } from '../../components/NavBar';
  
import Camera from '../../../public/images/camera.png'

const { Option } = Select;

export default function ProjectPage(){
   
  return (
    <>
      <NavBar></NavBar>
      <Row justify='center' style={{padding: '2%'}}>
      <Card style={{width: '80%', boxShadow:"0 3px 3px rgba(0,0,0,0.2)"}}>
        <Row>
          <p style={{fontSize:'24pt'}}>Project Name</p>
        </Row>
        <Row align='bottom'>
        <Col span={5}>
        <h1><PlayArrowIcon style={{fontSize: '42pt'}} /></h1>
        <h1><PauseIcon style={{fontSize: '42pt'}} /></h1>
        <h1><VideocamIcon style={{fontSize: '42pt'}}/></h1>
        <h1><VideocamOffIcon style={{fontSize: '42pt'}}/></h1>
        </Col>
        <Col span={18}>
          <Row justify="end">
          <Image width={750} src={Camera}></Image>
          </Row>
        </Col>
        </Row>
      </Card>
      </Row>
      <Row justify='center' style={{padding: '2%'}}>
      <Card style={{width: '80%', boxShadow:"0 3px 3px rgba(0,0,0,0.2)"}}>
        <h2 style={{fontWeight: "300", marginBottom: 10}}>Características do Projeto</h2>
        <Space direction="vertical" size="middle" style={{ display: 'flex' }}>
        <Card bordered></Card>
        <Card bordered></Card>
        <Card bordered></Card>
        <Card bordered></Card>
        <Card bordered></Card>
        </Space>
      </Card>
      </Row>
      <Row justify="center">
      <h1 style={{fontWeight: "300", textAlign:"center"}}>Análise de Gases do Ambiente <Divider></Divider></h1>
      </Row>
      <Row justify='center' style={{padding: '2%'}}>
        <Space direction="horizontal" size="middle" style={{ display: 'flex' }}>
        <Card bordered style={{width:"20vw", boxShadow:"0 3px 3px rgba(0,0,0,0.2)"}}></Card>
        <Card bordered style={{width:"20vw", boxShadow:"0 3px 3px rgba(0,0,0,0.2)"}}></Card>
        <Card bordered style={{width:"20vw", boxShadow:"0 3px 3px rgba(0,0,0,0.2)"}}></Card>
        <Card bordered style={{width:"20vw", boxShadow:"0 3px 3px rgba(0,0,0,0.2)"}}></Card>
        </Space>
      </Row>
    </>
  );
};
