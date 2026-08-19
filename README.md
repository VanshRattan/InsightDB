# 🚀 InsightDB  
## AI-Powered Conversational Data Analysis Platform

<p align="center">
<img src="assets/insightdb-banner.png" width="900">
</p>

<p align="center">
<b>Ask questions. Analyze data. Generate insights using natural language.</b>
</p>

<p align="center">

![React](https://img.shields.io/badge/Frontend-React-blue)
![TypeScript](https://img.shields.io/badge/Language-TypeScript-blue)
![Python](https://img.shields.io/badge/Backend-Python-yellow)
![LangGraph](https://img.shields.io/badge/AI-LangGraph-purple)
![DuckDB](https://img.shields.io/badge/Database-DuckDB-orange)
![Plotly](https://img.shields.io/badge/Visualization-Plotly-green)

</p>


---

# 📌 Overview

InsightDB is an AI-powered conversational data analytics platform that allows users to analyze datasets using natural language instead of manually writing SQL queries or Python scripts.

Users can upload CSV files and ask analytical questions such as:

```
Show monthly sales trends.

Find the top customers by revenue.

Calculate correlation between sales and quantity.

Detect unusual sales values.

Compare sales performance by region.
```

InsightDB understands the user's intent, performs the required analysis, generates visualizations, and provides explainable analytical reports.

The platform combines:

- Large Language Models
- Multi-Agent AI Workflows
- DuckDB Analytical Processing
- Python Statistical Analysis
- Automated Visualization Generation


---

# 🎥 Application Preview

<p align="center">
<img src="assets/demo.gif" width="850">
</p>


Workflow:

```
Upload CSV Dataset
          |
          ↓
Dataset Profiling
          |
          ↓
Ask Natural Language Question
          |
          ↓
AI Agent Analysis
          |
          ↓
Generated SQL / Python Code
          |
          ↓
Visualization
          |
          ↓
Analytical Report
```


---

# ✨ Features


## 📂 Dataset Upload & Profiling

InsightDB allows users to upload CSV datasets and automatically understands their structure.

Features:

- Dataset isolation using sessions
- Automatic column detection
- Data type identification
- Row count analysis
- Statistical profiling
- DuckDB-based storage


<p align="center">
<img src="assets/data-profile.png" width="650">
</p>


---

# 🤖 Multi-Agent AI Architecture

InsightDB uses a LangGraph-based multi-agent workflow instead of a single LLM response.

<p align="center">
<img src="assets/agent-workflow.png" width="850">
</p>


## AI Agent Workflow


```mermaid
flowchart TD

A[User Question]

A --> B[Supervisor Agent]

B --> C[Schema Profiler]

B --> D[Planner Agent]

D --> E[Code Generator]

E --> F[Sandbox Executor]

F --> G[Validator Agent]

G --> H[Reflection Agent]

G --> I[Visualization Agent]

I --> J[Report Generator]

J --> K[Final Response]
```


---

# 🧠 AI Agents


## Supervisor Agent

Determines which analytical capability is required.

Example:

```
User:
Show monthly revenue growth

Supervisor:
Trend Analysis Required
```


---

## Schema Profiler

Understands the uploaded dataset:

- Column names
- Data types
- Number of rows
- Missing values
- Statistical properties


---

## Planner Agent

Creates an analysis strategy before execution.

Example:

```
Question:
Which region generated maximum revenue?


Plan:

1. Identify revenue column
2. Group data by region
3. Calculate total revenue
4. Sort results
5. Generate visualization
```


---

## Code Generator Agent

Generates executable:

- SQL queries
- Python scripts
- Pandas operations
- Statistical calculations


---

## Sandbox Executor

Executes generated Python code securely using:

- Process isolation
- Timeout limits
- Memory restrictions
- Execution validation


---

## Validator Agent

Validates:

- Generated code
- SQL queries
- Execution output
- Analytical results


---

## Reflection Agent

Automatically handles failures.

Workflow:

```
Execution Failure
        |
        ↓
Failure Analysis
        |
        ↓
Code Regeneration
        |
        ↓
Retry Execution
```


---

# 📊 Visualization Engine


<p align="center">
<img src="assets/charts.png" width="750">
</p>


InsightDB automatically selects suitable visualizations.


| Analysis Type | Visualization |
|---|---|
| Time Trends | Line Chart |
| Category Comparison | Bar Chart |
| Relationship Analysis | Scatter Plot |
| Distribution | Histogram |
| Outlier Detection | Box Plot |
| Contribution Analysis | Pie Chart |


---

# 💬 Conversational Memory

InsightDB supports follow-up questions using LangGraph state management.


Example:

```
User:
Show top 10 customers by sales


InsightDB:
Returns top 10 customers


User:
Show only top 3


InsightDB:
Updates previous analysis
```


The system understands context from previous conversations.


---

# 📑 Automated Reports


<p align="center">
<img src="assets/report.png" width="750">
</p>


Generated reports include:

- Query interpretation
- Summary insights
- Data tables
- Statistical findings
- Visualizations
- Recommendations


Reports can optionally be exported as PDF.


---

# 🔍 Explainability & Observability


<p align="center">
<img src="assets/explainability.png" width="750">
</p>


InsightDB makes every analysis transparent.

Users can inspect:

✅ Generated SQL  
✅ Generated Python Code  
✅ Execution Results  
✅ Validation Status  
✅ Retry Information  
✅ Workflow Execution Trace  
✅ Runtime Metrics  
✅ Historical Reports  


---

# 🏗️ System Architecture


<p align="center">
<img src="assets/system-architecture.png" width="900">
</p>


Architecture:

```
                  User

                   |

            React Frontend

                   |

              Backend API

                   |

            LangGraph Engine

                   |

        ----------------------

        |          |          |

      SQL      Python    Visualization

     Agent     Agent        Agent


                   |

             Report Generator

                   |

              Final Response
```


---

# 🛠️ Technology Stack


## Frontend

| Technology | Purpose |
|---|---|
| React | UI Framework |
| TypeScript | Type Safety |
| Vite | Build Tool |
| Tailwind CSS | Styling |
| Plotly | Interactive Visualization |


## Backend

| Technology | Purpose |
|---|---|
| Python | Backend Logic |
| LangGraph | AI Agent Workflow |
| DuckDB | Analytical Database |
| Pandas | Data Processing |
| NumPy | Numerical Analysis |
| PostgreSQL | Persistent Storage |


---

# 📂 Project Structure


```
InsightDB

│
├── frontend
│   ├── src
│   ├── components
│   ├── pages
│   └── charts
│
├── backend
│
│   ├── agents
│   │   ├── supervisor
│   │   ├── planner
│   │   ├── validator
│   │   ├── visualization
│   │   └── reporter
│   │
│   ├── database
│   ├── execution
│   └── analytics
│
├── assets
│
└── README.md
```


---

# 🚀 Installation & Running


## Prerequisites

Install:

- Python >= 3.10
- Node.js >= 18
- npm
- Git


Check versions:

```bash
python --version

node --version

npm --version
```


---

# 1. Clone Repository


```bash
git clone https://github.com/yourusername/InsightDB.git

cd InsightDB
```


---

# 2. Backend Setup


```bash
cd backend
```


Create virtual environment:


### Windows

```bash
python -m venv venv

venv\Scripts\activate
```


### Linux / Mac

```bash
python3 -m venv venv

source venv/bin/activate
```


Install dependencies:

```bash
pip install -r requirements.txt
```


---

# 3. Environment Variables


Create:

```
backend/.env
```


Example:

```env
OPENAI_API_KEY=your_api_key

DATABASE_URL=postgresql://username:password@localhost:5432/insightdb

MAX_EXECUTION_TIME=30

MAX_MEMORY_LIMIT=512
```


---

# 4. Start Backend


```bash
python main.py
```


or:

```bash
uvicorn main:app --reload
```


Backend:

```
http://localhost:8000
```


API Documentation:

```
http://localhost:8000/docs
```


---

# 5. Frontend Setup


Open another terminal:


```bash
cd frontend
```


Install dependencies:

```bash
npm install
```


Create:

```
frontend/.env
```


Add:

```env
VITE_API_URL=http://localhost:8000
```


---

# 6. Start Frontend


```bash
npm run dev
```


Frontend:

```
http://localhost:5173
```


---

# ▶️ Running Application


You need two terminals:


### Backend

```bash
cd backend

activate environment

python main.py
```


### Frontend

```bash
cd frontend

npm run dev
```


Open:

```
http://localhost:5173
```


---

# 🐳 Docker Deployment


Build:

```bash
docker-compose build
```


Run:

```bash
docker-compose up
```


Services:

```
Frontend:
localhost:5173


Backend:
localhost:8000
```


---

# 🔐 Security Features


InsightDB provides:

- Dataset isolation
- Controlled code execution
- Memory limitations
- Timeout handling
- Validation before execution
- Failure recovery


---

# 🔮 Future Improvements


- Excel file support
- SQL database connectors
- AI-generated dashboards
- Voice-based analytics
- Cloud deployment
- Multi-user collaboration
- Automated ML recommendations


---

# 🎯 Why InsightDB?

Traditional analytics requires knowledge of:

- SQL
- Python
- Statistics
- Visualization tools


InsightDB removes this complexity by allowing users to communicate with data naturally while maintaining transparency through generated code and explainable workflows.


---
If you like InsightDB, consider giving this repository a star ⭐
