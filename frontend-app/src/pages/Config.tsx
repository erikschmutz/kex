import { Typography } from "antd";
import React, { useContext, useEffect } from "react";
import Context from "../context";
import { useConfig } from "../model/interfaces";

const { Title, Text } = Typography;

export default function Config() {
  const context = useContext(Context);
  const config = useConfig();

  useEffect(() => {
    context?.setPage("configuration");
  }, []);

  return (
    <div>
      <Title level={2}>Target</Title>
      <Text editable={false}>{config?.target}</Text>
      <Title level={2}>Solver</Title>
      <Text editable={false}>{config?.solver}</Text>
      <Title level={2}>Activation</Title>
      <Text editable={false}>{config?.activation}</Text>
    </div>
  );
}
