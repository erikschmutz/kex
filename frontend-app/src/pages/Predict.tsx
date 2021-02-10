import React, { useContext, useEffect } from "react";
import Context from "../context";

export default function Predict() {
  const context = useContext(Context);

  useEffect(() => {
    context?.setPage("predict");
  });

  return (
    <div>
      <p>Predict</p>
    </div>
  );
}
