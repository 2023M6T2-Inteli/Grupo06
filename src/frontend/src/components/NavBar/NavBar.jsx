import React, { useState } from "react";
import Image from "next/image";
import ExitToAppOutlinedIcon from "@mui/icons-material/ExitToAppOutlined";
import NotificationsOutlinedIcon from "@mui/icons-material/NotificationsOutlined";
import HelpOutlineOutlinedIcon from "@mui/icons-material/HelpOutlineOutlined";
import PermIdentityOutlinedIcon from "@mui/icons-material/PermIdentityOutlined";
import { Layout, Menu, Input, Row, Col, Button } from "antd";

import Logo from "../../../public/images/logo_lincore.png";
import { BorderBottom } from "@mui/icons-material";

const { Header } = Layout;
const { SubMenu } = Menu;
const { Search } = Input;

const NavBar = () => {
  const [collapsed, setCollapsed] = useState(false);

  const toggle = () => {
    setCollapsed(!collapsed);
  };

  const handleMenuClick = (e) => {
    if (e.key === "3") {
      window.location.href = "/login";
    }
  };

  return (
    <Row
      className="row-l"
      align="middle"
      justify="right"
      style={{
        backgroundColor: "#fff",
        height: "60px",
        border: "1px solid #d3d3d3",
      }}
    >
      <Col span={10}>
        <Image width={100} src={Logo}></Image>
      </Col>
      <Col span={14} align="center">
        <Row justify="end" align="middle">
          <Button type="link" style={{ color: "#000" }}>
            <HelpOutlineOutlinedIcon />
          </Button>
          <Button type="link" style={{ color: "#000" }}>
            <NotificationsOutlinedIcon />
          </Button>
          <Button type="link" style={{ color: "#000" }}>
            Geraldo
          </Button>
          <Button type="link" style={{ color: "#000" }}>
            <PermIdentityOutlinedIcon />
          </Button>
        </Row>
      </Col>
    </Row>
  );
};

export default NavBar;
