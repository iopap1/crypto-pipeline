@echo off
cd /d "C:\Users\papou\crypto-pipeline"

REM Run Python directly from your virtual environment
"C:\Users\papou\crypto-pipeline\venv\Scripts\python.exe" run_pipeline.py >> pipeline_log.txt 2>&1
