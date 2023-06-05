import { Layout, Menu, Button } from "antd";
import {
  AppstoreOutlined,
  AuditOutlined,
  FileAddOutlined,
  ProjectOutlined,
} from "@ant-design/icons";
import Link from "next/link";
function getItem(label, key, icon, children, type, path) {
  return {
    key,
    icon,
    children,
    label,
    type,
    path,
  };
}
const items = [
  getItem(
    "Menu",
    "grp",
    null,
    [
      getItem("Histórico", "hist", <AuditOutlined />, null, null, "/historic"),
      getItem(
        "Simulação",
        "simu",
        <AppstoreOutlined />,
        null,
        null,
        "/project"
      ),
      getItem("Add projeto", "addp", <FileAddOutlined />, null, null, "/"),
      getItem(
        "Projeto",
        "project",
        <ProjectOutlined />,
        null,
        null,
        "/project"
      ),
    ],
    "group"
  ),
];
const Sidebar = () => {
  const onClick = (e) => {
    if (e == "hist") {
      console.log("funciona");
    }
    console.log("click ", e);
  };
  const { Sider } = Layout;
  return (
    <Sider
      width={200}
      style={{
        height: "100%",
        backgroundColor: "#fff",
        boxShadow: "0 3px 10px rgba(0,0,0,0.2)",
      }}
    >
      <Menu
        onClick={onClick}
        style={{
          width: 200,
        }}
        defaultSelectedKeys={["1"]}
        defaultOpenKeys={["sub1"]}
        mode="inline"
      >
        {items.map((item) => {
          if (item.type === "group") {
            return (
              <Menu.SubMenu key={item.key} title={item.label} icon={item.icon}>
                {item.children.map((child) => (
                  <Menu.Item key={child.key} icon={child.icon}>
                    <Link href={child.path}>{child.label}</Link>
                  </Menu.Item>
                ))}
              </Menu.SubMenu>
            );
          } else {
            return (
              <Menu.Item key={item.key} icon={item.icon}>
                <Link href={item.path}>{item.label}</Link>
              </Menu.Item>
            );
          }
        })}
      </Menu>
    </Sider>
  );
};
export default Sidebar;
