import React from "react";
import ReactDOM from "react-dom";
import "./index.css";
import { App } from "~/root/App";
import { QueryClient, QueryClientProvider } from "react-query";

const client = new QueryClient();

ReactDOM.render(
  <React.StrictMode>
    <QueryClientProvider client={client}>
      <App/>
    </QueryClientProvider>
  </React.StrictMode>,
  document.getElementById("root")
);
