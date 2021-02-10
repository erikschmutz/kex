import React, { useState } from "react";
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
import { ContextProvider } from "./context";

const { Content, Sider } = Layout;

function App() {
  const [page, setPage] = useState("home");

  return (
    <ContextProvider value={{ page, setPage }}>
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
    </ContextProvider>
  );
}

export default App;
