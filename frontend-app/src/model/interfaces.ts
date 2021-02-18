import { useState, useEffect } from "react";

export interface IConfig {
  target: string;
  solver: string;
  activation: string;
}

const getLocalConfig = () => {
  const json_string = localStorage.getItem("config");
  if (json_string) return JSON.parse(json_string);
  else
    return {
      target: "example",
      activation: "relu",
      solver: "adam",
    };
};

const setLocalConfig = (config: any) => {
  const json_string = JSON.stringify(config);
  localStorage.setItem("config", json_string);
};

export function useConfig() {
  const config = getLocalConfig();

  useEffect(() => setLocalConfig(config), [config]);

  return config;
}
