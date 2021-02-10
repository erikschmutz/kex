import { Typography } from "antd";
import React, { useContext, useEffect, useState } from "react";
import Context from "../context";
import { IConfig } from "../model/interfaces";
import Model from "../model/Model";

const { Title, Text } = Typography;

export default function Config() {
  const context = useContext(Context);

  const [config, setConfig] = useState<IConfig>();

  useEffect(() => {
    context?.setPage("configuration");
  }, []);

  useEffect(() => {
    if (!config) fetchConfig();
  }, [config]);

  const fetchConfig = async () => {
    const res = await Model.get("/config");
    if (res && !("error" in res)) setConfig(res);
  };

  return (
    <div>
      <Title level={2}>Dataset</Title>
      <Text editable={false}>{config?.dataset}</Text>
      <Title level={2}>Script</Title>
      <Text editable={false}>{config?.script}</Text>
      <Title level={2}>Activation</Title>
      <Text editable={false}>{config?.activation}</Text>
    </div>
  );
}
