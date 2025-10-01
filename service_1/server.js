import express from "express";
import { HomeRouter } from "./routes/HomeRouter.js";
import { DataInputController } from "./routes/DataInputController.js";

const app = express();

app.use(express.json());

app.use("/", HomeRouter);
app.use("/", DataInputController);

app.listen(8080, () => {
  console.log("Server is runing on port 8080");
});
