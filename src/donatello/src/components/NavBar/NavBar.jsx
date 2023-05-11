import React, { useState } from 'react';
import Image from 'next/image';
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
import { Layout, Menu, Input, Badge, Dropdown } from 'antd';

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
    <Header className="site-layout-background" style={{ padding: 0, lineHeight: 0 }}>
      <Menu theme="dark" mode="horizontal" defaultSelectedKeys={['2']}>

       <Image width={50}src={Logo}></Image>
      </Menu>
    </Header>
  );
};

export default NavBar;