import { Router } from "express";
import { HomeController } from "../controllers/HomeController.js";
const HomeRouter = Router();

HomeRouter.get("/api", HomeController);

export { HomeRouter };
