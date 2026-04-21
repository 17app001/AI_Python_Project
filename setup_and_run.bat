@echo off
title Taiwan Hot Stocks Scraper - Setup and Launch

echo ========================================
echo Taiwan Hot Stocks Scraper
echo ========================================
echo.

cd /d "%~dp0"

REM Check if virtual environment exists
if not exist "venv\Scripts\activate.bat" (
    echo Creating virtual environment...
    python -m venv venv
    echo Virtual environment created.
    echo.
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate

REM Install dependencies
echo Installing dependencies...
pip install -r requirements.txt >nul 2>&1
echo Dependencies installed.
echo.

REM Choose launch mode
:menu
echo ========================================
echo Choose launch mode:
echo 1. CLI Mode (Command Line)
echo 2. GUI Mode (Web Interface)
echo 3. Exit
echo ========================================
set /p choice="Enter your choice (1-3): "

if "%choice%"=="1" goto cli
if "%choice%"=="2" goto gui
if "%choice%"=="3" goto exit
echo Invalid choice. Please try again.
goto menu

:cli
echo.
echo Starting CLI Mode...
python main.py
goto end

:gui
echo.
echo Starting GUI Mode...
echo Opening browser...
timeout /t 3 /nobreak >nul
start http://localhost:8501
streamlit run app.py --server.port 8501
goto end

:exit
echo Goodbye!
exit /b 0

:end
pause
