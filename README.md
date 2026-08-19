<div align="center">

# 🚀 InsightDB

<p>
<em>An AI-powered conversational data analysis platform that allows users to analyze datasets using natural language.</em>
</p>

<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB" />
<img src="https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white" />
<img src="https://img.shields.io/badge/LangGraph-AI_Agents-purple?style=for-the-badge" />

</div>


<br />


# 📌 Overview

**InsightDB** is an AI-powered conversational analytics platform that enables users to analyze CSV datasets using natural language.

Instead of manually writing SQL queries or Python scripts, users can simply ask questions such as:

- "Show monthly sales trends"
- "Find the top customers by revenue"
- "Detect unusual sales values"
- "Compare sales performance by region"

InsightDB understands user intent, creates an analysis workflow, generates SQL/Python code, executes the analysis, and provides explainable results.


---

# 🤖 AI Agent Workflow


InsightDB uses a **LangGraph-based multi-agent architecture** where different AI agents handle different stages of analysis.


```
                User Question

                      ↓

              Supervisor Agent

                      ↓

              Schema Profiler

                      ↓

              Planning Agent

                      ↓

          SQL / Python Analysis Agent

                      ↓

              Validator Agent

                      ↓

             Report Generation

                      ↓

              Final Response
```


## Agent Responsibilities


| Agent | Purpose |
|---|---|
| Supervisor Agent | Determines the required analysis workflow |
| Schema Profiler | Understands dataset structure and column relationships |
| Planner Agent | Creates analysis strategy |
| Code Generator | Generates SQL/Python analysis code |
| Sandbox Executor | Executes generated analysis securely |
| Validator Agent | Checks results and handles errors |
| Report Agent | Generates analytical explanations |


---

# ✨ Key Features


## 📂 CSV Dataset Analysis

- Upload CSV datasets
- Automatic dataset profiling
- Detect columns and data types
- Generate dataset statistics
- Execute analytical queries using DuckDB


---

## 🤖 Natural Language Data Analysis

Users can ask questions instead of writing SQL queries or Python scripts.

Example:

```text
Show monthly revenue trends
```

InsightDB automatically:

- Understands user intent
- Creates an analysis plan
- Generates SQL/Python code
- Executes the analysis
- Returns analytical insights


---

## 🔍 Explainable AI Results

Users can inspect:

- Generated SQL queries
- Generated Python analysis code
- Execution results
- Validation status
- Analysis workflow


This makes AI-generated insights transparent and reproducible.


---

## 💬 Conversational Memory

InsightDB supports follow-up questions using session context.


Example:

```text
User:
Show top 10 customers by sales


InsightDB:
Displays top 10 customers


User:
Show only top 3
```


The system understands previous conversation context and updates the analysis accordingly.


---

## 🔐 Safe Code Execution

Generated Python analysis is executed with:

- Code validation checks
- Execution limits
- Error handling
- Retry mechanisms


---

## 📊 Data Analysis Results

InsightDB provides structured analytical outputs including:

- Dataset profiling
- Statistical summaries
- Query execution results
- Generated SQL queries
- Generated Python analysis code
- Explainable analytical insights

Visualization capabilities are planned as part of future development.


---

# 🛠️ Tech Stack


## Frontend

| Technology | Purpose |
|---|---|
| React | User Interface |
| TypeScript | Type Safety |
| Vite | Frontend Build Tool |
| Tailwind CSS | Styling |


## Backend

| Technology | Purpose |
|---|---|
| Python | Backend Processing |
| LangGraph | AI Agent Orchestration |
| DuckDB | Analytical Database |
| Pandas | Data Processing |
| NumPy | Numerical Analysis |
| PostgreSQL | Persistent Storage (Optional) |


---

# 📂 Project Structure


```
InsightDB

│
├── frontend
│   ├── src
│   ├── components
│   └── pages
│
├── backend
│   ├── agents
│   ├── database
│   ├── execution
│   └── reports
│
├── requirements.txt
│
├── start-dev.ps1
│
└── README.md
```


---

# 🚀 How To Run


## Prerequisites

Make sure you have installed:

- Python 3.10+
- Node.js 18+
- npm
- Git


---

# 1. Clone Repository


```bash
git clone https://github.com/yourusername/InsightDB.git

cd InsightDB
```


---

# 2. Backend Setup


```powershell
cd E:\InsightDB

.\.venv\Scripts\Activate.ps1

$env:POSTGRES_ENABLED="false"

python -m uvicorn backend.main:app --reload --host 127.0.0.1 --port 8000
```


---

# 3. Frontend Setup


```powershell
cd E:\InsightDB\frontend

npm install

npm run dev
```


---

# ▶️ Usage


1. Open the frontend application

2. Upload a CSV dataset

3. Ask analytical questions

4. Explore:

- AI-generated insights
- Generated SQL queries
- Python analysis code
- Execution results
- Analytical reports


---

# 🔮 Future Improvements


- Automatic visualization generation using Plotly
- AI-generated interactive dashboards
- Excel dataset support
- Direct SQL database connections
- Cloud deployment
- Multi-user collaboration
- Automated machine learning recommendations


---

# 📌 Future Vision


InsightDB aims to become an AI-powered data analyst capable of transforming raw datasets into meaningful insights through natural language interaction, automated reasoning, and intelligent analytical workflows.


---
