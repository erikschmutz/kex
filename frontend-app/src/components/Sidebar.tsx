import React, { useContext } from "react";
import { Menu } from "antd";

import {
  HomeOutlined,
  SettingOutlined,
  CloudUploadOutlined,
  FileImageOutlined,
} from "@ant-design/icons";
import { Link } from "react-router-dom";
import Context from "../context";

export default function Sidebar() {
  const context = useContext(Context);

  const menu = [
    {
      page: "home",
      path: "/",
      icon: <HomeOutlined />,
    },
    {
      page: "train",
      path: "/train",
      icon: <CloudUploadOutlined />,
    },
    {
      page: "predict",
      path: "/predict",
      icon: <FileImageOutlined />,
    },
    {
      page: "configuration",
      path: "/config",
      icon: <SettingOutlined />,
    },
  ];

  return (
    <>
      <Menu
        selectedKeys={[context ? context.page : ""]}
        mode="inline"
        theme="dark"
      >
        {menu.map((item) => (
          <Menu.Item key={item.page} icon={item.icon}>
            <Link style={{ textTransform: "capitalize" }} to={item.path}>
              {item.page}
            </Link>
          </Menu.Item>
        ))}
      </Menu>
    </>
  );
}
