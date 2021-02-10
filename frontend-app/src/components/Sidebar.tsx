import React, { useState } from "react";
import { Button, Menu } from "antd";

import {
  HomeOutlined,
  SettingOutlined,
  CloudUploadOutlined,
  FileImageOutlined,
} from "@ant-design/icons";
import { Link } from "react-router-dom";

export default function Sidebar() {
  return (
    <>
      <Menu defaultSelectedKeys={["1"]} mode="inline" theme="dark">
        <Menu.Item key="1" icon={<HomeOutlined />}>
          <Link to="/">Home</Link>
        </Menu.Item>
        <Menu.Item key="2" icon={<CloudUploadOutlined />}>
          <Link to="/train">Train</Link>
        </Menu.Item>
        <Menu.Item key="3" icon={<FileImageOutlined />}>
          <Link to="/predict">Predict</Link>
        </Menu.Item>
        <Menu.Item key="4" icon={<SettingOutlined />}>
          <Link to="/config">Configuration</Link>
        </Menu.Item>
      </Menu>
    </>
  );
}
