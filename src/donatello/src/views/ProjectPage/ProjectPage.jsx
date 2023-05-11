import React,{ useState } from 'react'
import { Row, Col, Card, Form, Input, Select, Button, Tooltip } from 'antd';
import { QuestionCircleOutlined, PlayCircleOutlined, PauseCircleOutlined } from '@ant-design/icons';
import VideocamIcon from '@mui/icons-material/Videocam';
import VideocamOffIcon from '@mui/icons-material/VideocamOff';
import PlayArrowIcon from '@mui/icons-material/PlayArrow';
import PauseIcon from '@mui/icons-material/Pause';
import { NavBar } from '../../components/NavBar';
  

const { Option } = Select;

export default function ProjectPage(){
   
  return (
    <>
      <NavBar></NavBar>
      <Row justify='center'>
      <Card style={{width: '80%'}}>
        <Row>
          <h1>Project Name</h1>
        </Row>
        <Row>
        <Col>
        <h1><PlayArrowIcon style={{fontSize: '42pt'}} /></h1>
        <h1><PauseIcon style={{fontSize: '42pt'}} /></h1>
        <h1><VideocamIcon style={{fontSize: '42pt'}}/></h1>
        <h1><VideocamOffIcon style={{fontSize: '42pt'}}/></h1>
        </Col>
        <Col></Col>
        </Row>
      </Card>
      </Row>
    </>
  );
};
