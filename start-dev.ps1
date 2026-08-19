# Start DataAgent Pro (Windows)
$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot

Write-Host "Starting without Docker (in-memory sessions enabled)..."
$env:POSTGRES_ENABLED = "false"

if (-not (Test-Path "$PSScriptRoot\.venv\Scripts\python.exe")) {
  throw "Python virtual environment not found. Run: python -m venv .venv; .\.venv\Scripts\python.exe -m pip install -r requirements.txt"
}

if (-not (Test-Path "$PSScriptRoot\frontend\node_modules")) {
  throw "Frontend dependencies not found. Run: cd frontend; npm install"
}

Write-Host "Starting backend on http://localhost:8000 ..."
Start-Process -FilePath "$PSScriptRoot\.venv\Scripts\python.exe" -ArgumentList "-m","uvicorn","backend.main:app","--reload","--host","127.0.0.1","--port","8000" -WorkingDirectory $PSScriptRoot

Write-Host "Starting frontend on http://localhost:5173 ..."
Start-Process -FilePath "npm" -ArgumentList "run","dev" -WorkingDirectory "$PSScriptRoot\frontend"

Write-Host ""
Write-Host "Open http://localhost:5173"
Write-Host "Upload uploads\sample_sales.csv to try the workspace."
Write-Host "Put your GROQ_API_KEY or GOOGLE_API_KEY in .env for analysis to work."
