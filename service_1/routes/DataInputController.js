import { Router } from "express";
import { getData } from "../controllers/DataInputController.js";

const DataInputController = Router();

DataInputController.post("/api/v1/data", getData);

export { DataInputController };
