import { CloudUploadOutlined } from "@ant-design/icons";
import { Upload, message, Button } from "antd";
import React, { useContext, useEffect } from "react";
import Context from "../context";
import { useConfig } from "../model/interfaces";
import Model from "../model/Model";

const { Dragger } = Upload;

export default function Train() {
  const context = useContext(Context);
  const config = useConfig();

  useEffect(() => {
    context?.setPage("train");
  });

  const train = () => {
    Model.train(config)
      .then((res) => console.log(res))
      .catch((err) => console.log(err));
  };

  const props = {
    name: "file",
    multiple: true,
    action: "https://www.mocky.io/v2/5cc8019d300000980a055e76",
    onChange(info: any) {
      const { status } = info.file;
      if (status !== "uploading") {
        console.log(info.file, info.fileList);
      }
      if (status === "done") {
        message.success(`${info.file.name} file uploaded successfully.`);
      } else if (status === "error") {
        message.error(`${info.file.name} file upload failed.`);
      }
    },
  };
  return (
    <>
      <Button onClick={train}>Train</Button>
      <Dragger {...props}>
        <p className="ant-upload-drag-icon">
          <CloudUploadOutlined />
        </p>
        <p className="ant-upload-text">
          Click or drag file to this area to upload
        </p>
        <p className="ant-upload-hint">
          Support for a single or bulk upload. Strictly prohibit from uploading
          company data or other band files
        </p>
      </Dragger>
    </>
  );
}
