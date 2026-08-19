# 🚀 InsightDB  
## AI-Powered Conversational Data Analysis Platform


<p align="center">
  <img src="./assets/insightdb-banner.png" width="800" alt="InsightDB Banner">
</p>


## 📌 Overview

InsightDB is an AI-powered conversational data analysis platform that allows users to analyze CSV datasets using natural language.

Instead of manually writing SQL queries or Python code, users can simply ask questions like:

- "Show monthly sales trends"
- "Find the top customers by revenue"
- "Detect unusual values"
- "Compare sales by region"

InsightDB understands the question, performs the required analysis, generates visualizations, and provides explainable results with generated SQL/Python code.


---

# ✨ Features

### 📂 CSV Data Analysis
- Upload CSV datasets
- Automatic dataset profiling
- Detect columns, data types, and statistics
- Fast analytical queries using DuckDB


### 🤖 AI Agent Workflow

InsightDB uses a LangGraph-based multi-agent architecture:

```
User Question
      |
      ↓
Supervisor Agent
      |
      ↓
Planning Agent
      |
      ↓
SQL / Python Analysis Agent
      |
      ↓
Validator
      |
      ↓
Visualization + Report Generation
```


### 📊 Data Visualization

Automatically generates:

- Line charts
- Bar charts
- Scatter plots
- Histograms
- Box plots


### 🔍 Explainable Analysis

Users can view:

- Generated SQL queries
- Generated Python code
- Analysis results
- Validation status


### 💬 Conversational Memory

Supports follow-up questions.

Example:

```
User:
Show top 10 customers

User:
Show only top 3
```

The system understands the previous context.


---

# 🛠️ Tech Stack

## Frontend

- React
- TypeScript
- Vite
- Tailwind CSS
- Plotly


## Backend

- Python
- LangGraph
- DuckDB
- Pandas
- NumPy
- PostgreSQL (optional)


---

# 📂 Project Structure

```
InsightDB

├── frontend
│
├── backend
│   ├── agents
│   ├── database
│   ├── execution
│   └── reports
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

# Backend Setup


Go to backend:

```bash
cd backend
```


Create virtual environment:

```bash
python -m venv venv
```


Activate:

### Windows

```bash
venv\Scripts\activate
```


### Linux/Mac

```bash
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


Run backend:

```bash
python main.py
```

Backend runs on:

```
http://localhost:8000
```


---

# Frontend Setup


Open another terminal:


```bash
cd frontend
```


Install packages:

```bash
npm install
```


Run frontend:

```bash
npm run dev
```


Frontend runs on:

```
http://localhost:5173
```


---

# ▶️ Usage

1. Open the frontend URL
2. Upload a CSV file
3. Ask analytical questions
4. View:
   - Results
   - Charts
   - Generated Code
   - Reports


---
