@echo off
echo Starting Taiwan Hot Stocks Scraper - GUI Mode...
echo.

cd /d "%~dp0"
call venv\Scripts\activate
streamlit run app.py --server.port 8501 --server.headless true
