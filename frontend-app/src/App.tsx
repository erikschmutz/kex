import React from "react";
import "./App.css";

import { Layout } from "antd";
import { Route, Switch } from "react-router-dom";

import Sidebar from "./components/Sidebar";
import Home from "./pages/Home";
import Train from "./pages/Train";
import Predict from "./pages/Predict";
import Config from "./pages/Config";
import NotFound from "./pages/NotFound";
import Header from "./components/Header";

const { Content, Sider } = Layout;

function App() {
  return (
    <Layout>
      <Sider>
        <Sidebar></Sidebar>
      </Sider>
      <Layout>
        <Header></Header>
        <Content id="content">
          <Route path="/">
            <Switch>
              <Route exact path="/" component={Home} />
              <Route path="/train" component={Train} />
              <Route path="/predict" component={Predict} />
              <Route path="/config" component={Config} />
              <Route component={NotFound} />
            </Switch>
          </Route>
        </Content>
      </Layout>
    </Layout>
  );
}

export default App;
