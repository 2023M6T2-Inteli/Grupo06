import React, { useState } from 'react';
import Image from 'next/image';
import ExitToAppOutlinedIcon from '@mui/icons-material/ExitToAppOutlined';
import {
  AppstoreOutlined,
  MailOutlined,
  MenuFoldOutlined,
  MenuUnfoldOutlined,
  NotificationOutlined,
  SearchOutlined,
  SettingOutlined,
  UserOutlined,
} from '@ant-design/icons';
import { Layout, Menu, Input, Badge, Dropdown, Row, Col, Divider, Button } from 'antd';

import Logo from  '../../../public/images/logo_lincore.png'

const { Header } = Layout;
const { SubMenu } = Menu;
const { Search } = Input;

const NavBar = () => {
  const [collapsed, setCollapsed] = useState(false);

  const toggle = () => {
    setCollapsed(!collapsed);
  };

  const handleMenuClick = (e) => {
    if (e.key === '3') {
      window.location.href = '/login';
    }
  };

  return (
        <Row align='middle' justify="center" style={{ boxShadow: "0 3px 3px gray;"}}>
          <Col span={10}>
          <Image width={100}src={Logo}></Image>
          </Col>
          <Col span={12} align='center'>
            <Row justify="end" align="middle">
            <Button type='link' style={{color:"#2E202C"}}>ACOMPANHAMENTO</Button>
            <Button type='link' style={{color:"#2E202C"}}>PROJETO</Button>
            <Button type='link' style={{color:"#2E202C"}}>GASES</Button>
            <Button type='link' style={{color:"#2E202C"}}>SIMULAÇÃO</Button>
            <Button type="link" style={{color:"#2E202C"}}><ExitToAppOutlinedIcon/></Button>
            </Row>
          </Col>
        </Row>
  );
};

export default NavBar;