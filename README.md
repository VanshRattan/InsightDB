```html
<!DOCTYPE html>
<html>

<head>
<title>InsightDB - AI Powered Data Analysis Platform</title>
</head>

<body>

<h1 align="center">
🚀 InsightDB
</h1>

<h2 align="center">
AI-Powered Conversational Data Analysis Platform
</h2>


<p align="center">
<img src="assets/insightdb-banner.png" width="900">
</p>


<p align="center">
<b>
Ask questions. Analyze data. Generate insights using natural language.
</b>
</p>


<p align="center">

<img src="https://img.shields.io/badge/Frontend-React-blue">
<img src="https://img.shields.io/badge/Language-TypeScript-blue">
<img src="https://img.shields.io/badge/Backend-Python-yellow">
<img src="https://img.shields.io/badge/AI-LangGraph-purple">
<img src="https://img.shields.io/badge/Database-DuckDB-orange">
<img src="https://img.shields.io/badge/Visualization-Plotly-green">

</p>


<hr>


<h1>📌 Overview</h1>


<p>
<b>InsightDB</b> is an AI-powered conversational analytics platform that allows users to analyze datasets using natural language instead of manually writing SQL queries or Python scripts.
</p>


<p>
Users can upload CSV files and ask questions like:
</p>


<ul>

<li>Show monthly sales trends</li>

<li>Find top customers by revenue</li>

<li>Calculate correlation between sales and quantity</li>

<li>Detect unusual sales values</li>

<li>Compare sales performance by region</li>

</ul>


<p>
InsightDB understands user intent, performs analysis, generates visualizations, and provides explainable reports.
</p>



<h1>🎥 Application Demo</h1>


<p align="center">

<img src="assets/demo.gif" width="850">

</p>



<h1>✨ Features</h1>


<h2>📂 Dataset Upload & Profiling</h2>


<ul>

<li>Upload CSV datasets</li>

<li>Create isolated dataset sessions</li>

<li>Load data into DuckDB</li>

<li>Automatically detect columns and data types</li>

<li>Generate dataset statistics</li>

</ul>


<img src="assets/data-profile.png" width="650">



<hr>



<h1>🤖 Multi-Agent AI Architecture</h1>


<p>
InsightDB uses a LangGraph-based multi-agent architecture where every agent performs a specialized task.
</p>


<img src="assets/agent-workflow.png" width="850">



<h2>Agent Workflow</h2>


<pre>

User Question

      |

Supervisor Agent

      |

----------------------------

|          |              |

Schema   Planner       Analysis

Agent    Agent         Agent


      |

Code Generator

      |

Sandbox Executor

      |

Validator

      |

Visualization Agent

      |

Report Generator

      |

Final Response


</pre>




<h1>🧠 AI Agents</h1>


<h2>Supervisor Agent</h2>

<p>
Routes user requests to the required analytical workflow.
</p>


<h2>Schema Profiler</h2>

<p>
Understands dataset structure:
</p>


<ul>

<li>Columns</li>
<li>Data Types</li>
<li>Rows</li>
<li>Statistics</li>

</ul>



<h2>Planner Agent</h2>

<p>
Creates a step-by-step execution strategy before analysis.
</p>



<h2>Code Generation Agent</h2>

<p>
Generates:
</p>


<ul>

<li>SQL queries</li>
<li>Python analysis scripts</li>
<li>Pandas operations</li>

</ul>




<h2>Sandbox Executor</h2>

<p>
Executes generated code safely with:
</p>


<ul>

<li>Timeout limits</li>
<li>Memory restrictions</li>
<li>Process isolation</li>

</ul>



<h2>Validator Agent</h2>

<p>
Checks generated code and analysis results before returning output.
</p>



<h2>Reflection Agent</h2>

<p>
Automatically fixes failures by regenerating and retrying analysis.
</p>




<h1>📊 Visualization Engine</h1>


<img src="assets/charts.png" width="750">


<p>
InsightDB automatically generates:
</p>


<table border="1">

<tr>
<th>Analysis</th>
<th>Visualization</th>
</tr>


<tr>
<td>Trends</td>
<td>Line Chart</td>
</tr>


<tr>
<td>Comparison</td>
<td>Bar Chart</td>
</tr>


<tr>
<td>Relationships</td>
<td>Scatter Plot</td>
</tr>


<tr>
<td>Distribution</td>
<td>Histogram</td>
</tr>


<tr>
<td>Outliers</td>
<td>Box Plot</td>
</tr>


</table>




<h1>💬 Conversational Memory</h1>


<p>
InsightDB remembers previous conversations using LangGraph state management.
</p>


<pre>

User:
Show top 10 customers by sales


InsightDB:
Returns top customers


User:
Show only top 3


InsightDB:
Updates previous analysis


</pre>



<h1>📑 Automated Reports</h1>


<img src="assets/report.png" width="750">


<p>
Generated reports contain:
</p>


<ul>

<li>Summary insights</li>

<li>Query interpretation</li>

<li>Data tables</li>

<li>Statistics</li>

<li>Visualizations</li>

<li>Recommendations</li>

</ul>



<h1>🔍 Explainability</h1>


<img src="assets/explainability.png" width="750">


<ul>

<li>Generated SQL</li>

<li>Generated Python Code</li>

<li>Execution Results</li>

<li>Validation Status</li>

<li>Workflow Logs</li>

<li>Runtime Metrics</li>

</ul>



<h1>🏗️ System Architecture</h1>


<img src="assets/system-architecture.png" width="900">



<pre>

             User

              |

       React Frontend

              |

          Backend API

              |

       LangGraph Engine

              |

 --------------------------------

 |              |               |

DuckDB       Python        Visualization

Database     Analysis        Engine


              |

          Reports


</pre>




<h1>🛠️ Technology Stack</h1>


<h2>Frontend</h2>


<ul>

<li>React</li>
<li>TypeScript</li>
<li>Vite</li>
<li>Tailwind CSS</li>
<li>Plotly</li>

</ul>



<h2>Backend</h2>


<ul>

<li>Python</li>
<li>LangGraph</li>
<li>DuckDB</li>
<li>Pandas</li>
<li>NumPy</li>
<li>PostgreSQL</li>

</ul>



<h1>📂 Project Structure</h1>


<pre>

InsightDB

│
├── frontend
│
├── backend
│
│── agents
│   ├── supervisor
│   ├── planner
│   ├── validator
│   └── reporter
│
├── database
│
├── execution
│
├── assets
│
└── README.html


</pre>




<h1>🚀 Installation & Running</h1>


<h2>Prerequisites</h2>


<ul>

<li>Python 3.10+</li>

<li>Node.js 18+</li>

<li>npm</li>

<li>Git</li>

</ul>



<h2>Clone Repository</h2>


<pre>

git clone https://github.com/yourusername/InsightDB.git

cd InsightDB

</pre>



<h2>Backend Setup</h2>


<pre>

cd backend

python -m venv venv

pip install -r requirements.txt

python main.py

</pre>




<h2>Frontend Setup</h2>


<pre>

cd frontend

npm install

npm run dev

</pre>



<h2>Application URLs</h2>


<pre>

Frontend:
http://localhost:5173


Backend:
http://localhost:8000


API Docs:
http://localhost:8000/docs

</pre>




<h1>🐳 Docker Setup</h1>


<pre>

docker-compose build

docker-compose up

</pre>



<h1>🔐 Security</h1>


<ul>

<li>Dataset isolation</li>

<li>Controlled execution environment</li>

<li>Code validation</li>

<li>Memory limits</li>

<li>Failure recovery</li>

</ul>




<h1>🔮 Future Improvements</h1>


<ul>

<li>Excel support</li>

<li>SQL database connectors</li>

<li>AI dashboards</li>

<li>Voice analytics</li>

<li>Cloud deployment</li>

<li>Multi-user collaboration</li>

</ul>




<h1>👨‍💻 Author</h1>


<p>
<b>Your Name</b>
<br>
Computer Science Engineering Student
</p>



<h2 align="center">
⭐ If you like InsightDB, consider starring the repository!
</h2>


</body>

</html>
```
