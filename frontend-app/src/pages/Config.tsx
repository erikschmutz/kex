import Title from "antd/lib/typography/Title";
import React from "react";

export default function Config() {
  let config = {
    dataset: "fruits-360",
    activation: "relu",
    script: "train.py",
  };

  return (
    <div>
      <Title>Dataset</Title>
    </div>
  );
}
