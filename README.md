# AI Research Assistant

![React](https://img.shields.io/badge/React-17.0.2-blue?logo=react) 
![Node.js](https://img.shields.io/badge/Node.js-18-green?logo=node.js) 
![FastAPI](https://img.shields.io/badge/FastAPI-0.100.0-lightgrey?logo=fastapi) 
![Python](https://img.shields.io/badge/Python-3.13-yellow?logo=python) 
![RabbitMQ](https://img.shields.io/badge/RabbitMQ-3.11-orange?logo=rabbitmq) 
![Docker](https://img.shields.io/badge/Docker-24-blue?logo=docker)

A modular AI research assistant for summarizing research papers and handling AI queries using a distributed architecture with **React frontend**, **Node.js for authentication**, **FastAPI for AI processing**, and **RabbitMQ for RPC communication**.

---

## Table of Contents
- [Project Structure](#project-structure)  
- [Features](#features)  
- [Tech Stack](#tech-stack)  
- [Setup & Installation](#setup--installation)  
- [Usage](#usage)  
- [Architecture Overview](#architecture-overview)  
- [License](#license)  

---

## Project Structure
/
├── Frontend            # React SPA handling user login and UI
├── service_1           # Node.js service handling authentication and request management
├── service_2           # FastAPI service for AI research summarization using LangChain + Google Gemini API

---

## Features
- **Authentication:** OAuth2 authentication handled by Node.js backend.  
- **AI Research Summarization:** FastAPI service processes research papers using LangChain + Google Gemini API.  
- **RPC Communication:** RabbitMQ handles async request/response between Node.js and FastAPI.  
- **Modular Design:** Clear separation between frontend, authentication, and AI processing services.  
- **Scalable Architecture:** Services communicate asynchronously via RabbitMQ, allowing easy scaling.  

---

## Tech Stack
- **Frontend:** React, React Router, Axios  
- **Backend:** Node.js (Express)  
- **AI Service:** FastAPI, Python, LangChain, Google Gemini API  
- **Message Queue:** RabbitMQ (CloudAMQP / self-hosted)  
- **Containerization:** Docker (for backend services)  
- **Deployment:** Vercel (frontend), Render (backend + FastAPI)  

---

## Setup & Installation

### Clone the repository
`git clone <repository-url>
cd <repository-root>`
### Frontend
`cd Frontend
npm install
npm start`

### Node.js Backend (service_1)

`
cd service_1
npm install
npm run dev
`

### FastAPI Backend (service_2)
`
cd service_2
python -m venv env
source env/bin/activate  # Windows: env\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
`
	•	Set .env for RabbitMQ URL and EXCHANGE name.


### Usage
	1.	Visit the React frontend in your browser.
	2.	Log in using OAuth credentials.
	3.	Submit a research paper query.
	4.	Node.js backend sends the request via RabbitMQ to FastAPI.
	5.	FastAPI processes the request and sends the summary back via RPC.
	6.	Node.js returns the result to the frontend for display.

### Architecture Overview
`
React SPA (Frontend)
       |
       v
Node.js (Auth + Request Manager)
       |
  RabbitMQ RPC
       |
FastAPI (AI Summarization)
       |
  RabbitMQ RPC
       |
Node.js
       |
React SPA
`

	•	RPC pattern: Ensures async communication between services.
	•	Message Queue: Handles job routing and response correlation.
	•	Modularity: Frontend and backends are decoupled for scalability and maintenance.
