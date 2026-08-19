<div align="center">

# 🚀 InsightDB

<p>
<em>An AI-powered conversational data analysis platform that allows users to analyze datasets using natural language.</em>
</p>

<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/LangGraph-AI%20Agents-purple?style=for-the-badge" />
<img src="https://img.shields.io/badge/DuckDB-Database-orange?style=for-the-badge" />
<img src="https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB" />
<img src="https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white" />
<img src="https://img.shields.io/badge/Plotly-Visualization-blue?style=for-the-badge" />

</div>

<br />


# 📌 Overview

InsightDB is an AI-powered conversational analytics platform that enables users to analyze CSV datasets using natural language.

Instead of manually writing SQL queries or Python scripts, users can simply ask questions like:

- "Show monthly sales trends"
- "Find the top customers by revenue"
- "Detect unusual sales values"
- "Compare sales performance by region"

InsightDB understands the user's query, performs the required analysis, generates visualizations, and provides explainable results with generated SQL/Python code.


---

# 🤖 How InsightDB Works


```
User Question

      ↓

Supervisor Agent

      ↓

Planning Agent

      ↓

SQL / Python Analysis Agent

      ↓

Validator Agent

      ↓

Visualization Generator

      ↓

Report Generation

      ↓

Final Response
```


InsightDB uses a **LangGraph-based multi-agent architecture** where each AI agent performs a specialized task:

| Agent | Responsibility |
|---|---|
| Supervisor Agent | Routes user queries |
| Schema Profiler | Understands dataset structure |
| Planner Agent | Creates analysis strategy |
| Code Generator | Generates SQL/Python code |
| Sandbox Executor | Executes analysis securely |
| Validator | Checks results |
| Visualization Agent | Creates charts |
| Report Agent | Generates final reports |


---

# ✨ Key Features


- 📂 **CSV Dataset Analysis** — Upload datasets and automatically detect columns, data types, and statistics

- 🤖 **AI-Powered Analytics** — Ask questions in natural language instead of writing SQL or Python

- 🧠 **Multi-Agent Workflow** — Uses LangGraph agents for planning, execution, validation, and reporting

- 📊 **Automatic Visualizations** — Generates interactive charts including:
  - Line charts
  - Bar charts
  - Scatter plots
  - Histograms
  - Box plots

- 🔍 **Explainable Results** — View:
  - Generated SQL queries
  - Generated Python code
  - Execution results
  - Validation status

- 💬 **Conversational Memory** — Supports follow-up questions using previous analysis context

Example:

```
User:
Show top 10 customers by revenue

User:
Show only top 3
```

The system understands the previous request and updates the analysis.


- 📑 **Automated Reports** — Generates structured reports containing insights, tables, charts, and recommendations

- 🔐 **Safe Code Execution** — Executes generated Python analysis with validation, timeout, and resource limits


---

# 🛠️ Tech Stack


| Layer | Technologies |
|---|---|
| Frontend | React, TypeScript, Vite, Tailwind CSS |
| Backend | Python |
| AI Framework | LangGraph |
| Database | DuckDB, PostgreSQL (Optional) |
| Data Processing | Pandas, NumPy |
| Visualization | Plotly |


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
├── assets
│
└── README.md
```


---

# 🚀 How To Run


## 1. Clone Repository


```bash
git clone https://github.com/yourusername/InsightDB.git

cd InsightDB
```


---

# ⚙️ Backend Setup


Navigate to backend:

```bash
cd backend
```


Create virtual environment:


### Windows

```bash
python -m venv venv

venv\Scripts\activate
```


### Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```


Install dependencies:

```bash
pip install -r requirements.txt
```


Create `.env` file:


```
OPENAI_API_KEY=your_api_key
```


Start backend:

```bash
python main.py
```


Backend runs at:

```
http://localhost:8000
```


---

# 💻 Frontend Setup


Open another terminal:


```bash
cd frontend
```


Install dependencies:

```bash
npm install
```


Start frontend:

```bash
npm run dev
```


Frontend runs at:


```
http://localhost:5173
```


---

# ▶️ Using InsightDB


1. Open the frontend application
2. Upload a CSV dataset
3. Ask analytical questions
4. Explore:
   - Generated insights
   - Charts
   - SQL queries
   - Python code
   - Reports


---

# 🔮 Future Improvements


- Support for Excel datasets
- Direct SQL database connections
- AI-generated dashboards
- Cloud deployment
- Multi-user collaboration
- Automated machine learning recommendations



---

⭐ If you like InsightDB, consider giving the repository a star!
