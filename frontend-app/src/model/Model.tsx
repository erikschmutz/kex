import { IConfig } from "./interfaces";

class Model {
  API = "http://localhost:8000";

  processResponse(response: any) {
    if (response.code === 500)
      return {
        error: "Something went wrong.",
      };
    if (response.ok) return response.json();

    return response.text().then((error: string) => {
      return {
        error,
      };
    });
  }

  get(path: string): any {
    return fetch(this.API + path)
      .then(this.processResponse)
      .catch((err) => console.error(err));
  }

  post(path: string, data = {}) {
    return fetch(this.API + path, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    }).then(this.processResponse);
  }
}

export default new Model();
