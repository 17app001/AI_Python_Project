@echo off
echo Starting Taiwan Hot Stocks Scraper - CLI Mode...
echo.

cd /d "%~dp0"
call venv\Scripts\activate
python main.py

pause
