import { useContext, useEffect } from "react";
import Context from "../context";

export default function Home() {
  const context = useContext(Context);

  useEffect(() => {
    context?.setPage("home");
  });

  return (
    <div>
      <p>Home</p>
    </div>
  );
}
