# Taiwan Hot Stocks Scraper - Startup Guide

## Quick Start

### Prerequisites
- Python 3.13 installed
- Internet connection
- Windows operating system

### Step 1: Setup Virtual Environment
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate
```

### Step 2: Install Dependencies
```bash
# Install required packages
pip install -r requirements.txt
```

## Launch Options

### Option 1: CLI Mode (Command Line Interface)
**Best for**: Quick data retrieval and automation

```bash
# Activate virtual environment
venv\Scripts\activate

# Run CLI application
python main.py
```

**Output**: Console display + CSV/JSON files in `data/` directory

### Option 2: GUI Mode (Streamlit Web Interface)
**Best for**: Interactive visualization and analysis

```bash
# Activate virtual environment
venv\Scripts\activate

# Run GUI application
streamlit run app.py
```

**Access**: Open browser to `http://localhost:8501`

### Option 3: GUI Mode with Custom Port
```bash
# Activate virtual environment
venv\Scripts\activate

# Run GUI on specific port
streamlit run app.py --server.port 8501
```

## Launch Scripts

### Windows Batch Files

#### 1. Create CLI Launcher (`run_cli.bat`)
```batch
@echo off
echo Starting Taiwan Hot Stocks Scraper - CLI Mode...
echo.

cd /d "%~dp0"
call venv\Scripts\activate
python main.py

pause
```

#### 2. Create GUI Launcher (`run_gui.bat`)
```batch
@echo off
echo Starting Taiwan Hot Stocks Scraper - GUI Mode...
echo.

cd /d "%~dp0"
call venv\Scripts\activate
streamlit run app.py --server.port 8501 --server.headless true
```

#### 3. Create Setup Script (`setup.bat`)
```batch
@echo off
echo Setting up Taiwan Hot Stocks Scraper...
echo.

cd /d "%~dp0"

echo Creating virtual environment...
python -m venv venv

echo Activating virtual environment...
call venv\Scripts\activate

echo Installing dependencies...
pip install -r requirements.txt

echo.
echo Setup complete!
echo.
echo Choose your launch option:
echo 1. Run CLI: run_cli.bat
echo 2. Run GUI: run_gui.bat
echo.
pause
```

### PowerShell Scripts

#### 1. Create CLI Launcher (`run_cli.ps1`)
```powershell
# Taiwan Hot Stocks Scraper - CLI Launcher
Write-Host "Starting Taiwan Hot Stocks Scraper - CLI Mode..." -ForegroundColor Green

Set-Location $PSScriptRoot
& ".\venv\Scripts\Activate.ps1"
python main.py

Read-Host "Press Enter to exit"
```

#### 2. Create GUI Launcher (`run_gui.ps1`)
```powershell
# Taiwan Hot Stocks Scraper - GUI Launcher
Write-Host "Starting Taiwan Hot Stocks Scraper - GUI Mode..." -ForegroundColor Green

Set-Location $PSScriptRoot
& ".\venv\Scripts\Activate.ps1"
streamlit run app.py --server.port 8501 --server.headless true
```

## One-Click Setup

### Complete Setup Script (`setup_and_run.bat`)
```batch
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
```

## Troubleshooting

### Common Issues

#### 1. Virtual Environment Issues
```bash
# Recreate virtual environment
rmdir /s venv
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

#### 2. Port Already in Use
```bash
# Kill existing streamlit processes
taskkill /F /IM streamlit.exe

# Or use different port
streamlit run app.py --server.port 8502
```

#### 3. Permission Issues
```bash
# Run as administrator or check firewall settings
# Ensure port 8501 is not blocked
```

#### 4. Python Version Issues
```bash
# Check Python version
python --version

# Should be Python 3.13.x
# If not, install correct Python version
```

### Error Messages

#### "ModuleNotFoundError"
```bash
# Solution: Reinstall dependencies
pip install -r requirements.txt
```

#### "Connection Timeout"
```bash
# Solution: Check internet connection
# Or try again later (Yahoo Finance might be blocking)
```

#### "Port 8501 is already in use"
```bash
# Solution: Use different port
streamlit run app.py --server.port 8502
```

## Advanced Options

### Custom Configuration
```bash
# Run with custom settings
streamlit run app.py --server.port 8501 --server.headless false --browser.gatherUsageStats false
```

### Development Mode
```bash
# Run with auto-reload
streamlit run app.py --server.port 8501 --server.runOnSave true
```

### Production Mode
```bash
# Run with security settings
streamlit run app.py --server.port 8501 --server.headless true --server.enableCORS false
```

## File Structure After Setup

```
AI_Python_Project/
|
|-- venv/                    # Virtual environment
|-- src/
|   |-- scraper.py          # Core scraping logic
|-- data/                    # Output files (CSV, JSON)
|-- logs/                    # Log files
|-- docs/                    # Documentation
|   |-- workflow_diagram.md
|   |-- startup_guide.md
|-- app.py                   # GUI application
|-- main.py                  # CLI application
|-- requirements.txt         # Dependencies
|-- run_cli.bat             # CLI launcher
|-- run_gui.bat             # GUI launcher
|-- setup_and_run.bat       # Complete setup script
```

## Next Steps

1. **Run the setup script**: `setup_and_run.bat`
2. **Choose your preferred interface**: CLI or GUI
3. **Explore the data**: Check `data/` directory for output files
4. **View documentation**: Open `docs/workflow_diagram.md` for system overview

## Support

For issues or questions:
1. Check the troubleshooting section above
2. Review log files in `logs/` directory
3. Verify internet connection and Yahoo Finance accessibility
