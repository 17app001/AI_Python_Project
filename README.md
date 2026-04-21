# Taiwan Hot Stocks Scraper

A professional Python web scraper for Taiwan's hottest stocks with both CLI and GUI interfaces.

## Features

- **Dual Interface**: Both command-line and web-based GUI options
- **Real-time Data**: Fetches latest stock prices from Yahoo Finance
- **Interactive Dashboard**: Beautiful Streamlit web interface with charts
- **Data Export**: Save results to CSV and JSON formats
- **Easy Setup**: One-click installation and launch scripts
- **Professional Logging**: Comprehensive error handling and logging
- **Responsive Design**: Mobile-friendly web interface

## Quick Start

### Option 1: One-Click Setup (Recommended)

```bash
# Run the complete setup script
setup_and_run.bat
```

### Option 2: Manual Setup

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Choose your interface:
# CLI Mode:
python main.py

# GUI Mode:
streamlit run app.py
```

## Project Structure

```
AI_Python_Project/
|
|-- src/
|   |-- scraper.py          # Core scraping logic
|
|-- data/                    # Output files (CSV, JSON)
|-- logs/                    # Log files
|-- docs/                    # Documentation
|   |-- workflow_diagram.md  # System flowcharts
|   |-- startup_guide.md     # Launch instructions
|   |-- git_setup.md         # Git setup guide
|
|-- app.py                   # GUI application (Streamlit)
|-- main.py                  # CLI application
|-- requirements.txt         # Python dependencies
|
|-- Quick Launch Scripts:
|-- setup_and_run.bat        # Complete setup + launch
|-- run_cli.bat             # CLI launcher
|-- run_gui.bat             # GUI launcher
|
|-- README.md               # This file
|-- .gitignore              # Git ignore rules
```

## Interfaces

### CLI Mode

Perfect for automation and quick data retrieval:

```bash
python main.py
```

**Output**:
- Console display of stock information
- Automatic CSV export to `data/taiwan_hot_stocks.csv`
- JSON export to `data/taiwan_hot_stocks.json`

### GUI Mode

Interactive web dashboard for data visualization:

```bash
streamlit run app.py
```

**Features**:
- Real-time stock cards with price changes
- Interactive charts (price, volume, changes)
- Key metrics dashboard
- Data table with sorting
- CSV download functionality
- Auto-refresh option

**Access**: Open http://localhost:8501 in your browser

## Scraped Data

The scraper fetches the following information for Taiwan's top stocks:

- **Stock Code**: e.g., 2330.TW (TSMC)
- **Company Name**: Full company name
- **Current Price**: Latest stock price
- **Price Change**: Absolute change amount
- **Change Percentage**: Percentage change
- **Volume**: Trading volume
- **Market Cap**: Market capitalization
- **Timestamp**: When data was scraped

## Supported Stocks

Currently tracks Taiwan's most popular stocks:

1. **2330.TW** - Taiwan Semiconductor Manufacturing (TSMC)
2. **2454.TW** - MediaTek
3. **2317.TW** - Foxconn (Hon Hai)
4. **1303.TW** - Nan Ya PCB
5. **1301.TW** - Formosa Plastics
6. **2002.TW** - China Steel
7. **3008.TW** - Largan Precision
8. **2382.TW** - Quanta Computer
9. **2412.TW** - Chunghwa Telecom
10. **2882.TW** - Cathay Financial

*(Can be easily extended to add more stocks)*

## Dependencies

- **requests** - HTTP library for web scraping
- **beautifulsoup4** - HTML parsing
- **streamlit** - Web interface framework
- **pandas** - Data manipulation
- **plotly** - Interactive charts
- **altair** - Data visualization

## Installation

### Prerequisites

- Python 3.13+
- Internet connection
- Windows operating system

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Usage Examples

### CLI Example

```bash
# Basic usage
python main.py

# Output example:
============================================================
Taiwan Hot Stocks Scraper
============================================================
Starting to scrape Taiwan's top 5 hot stocks...
------------------------------------------------------------
[1] 2330.TW - Taiwan Semiconductor Manufacturing
    Current Price: 7,164.00
    Change: +16.00 (+0.22%)
    Volume: 27,088,285
    Market Cap: 53.162T
```

### GUI Example

```bash
# Launch web interface
streamlit run app.py

# Access at http://localhost:8501
```

## Configuration

### Modify Delay Settings

```python
# In main.py or app.py
scraper = WebScraper(delay=2.0, timeout=15)
```

### Change Stock List

Edit `src/scraper.py` in the `scrape_taiwan_hot_stocks` method:

```python
popular_stocks = [
    "2330.TW",  # Add or remove stocks here
    "2454.TW",
    # ... your custom list
]
```

## Output Files

### CSV Format
```csv
stock_code,company_name,current_price,price_change,price_change_percent,volume,market_cap,scraped_at
2330.TW,Taiwan Semiconductor Manufacturing,"7,164.00",+16.00,+0.17%,"27,088,285",53.162T,2026-04-21 18:05:33
```

### JSON Format
```json
[
  {
    "stock_code": "2330.TW",
    "company_name": "Taiwan Semiconductor Manufacturing",
    "current_price": "7,164.00",
    "price_change": "+16.00",
    "price_change_percent": "+0.17%",
    "volume": "27,088,285",
    "market_cap": "53.162T",
    "scraped_at": "2026-04-21 18:05:33"
  }
]
```

## Troubleshooting

### Common Issues

**"ModuleNotFoundError"**
```bash
# Reinstall dependencies
pip install -r requirements.txt
```

**"Port 8501 is already in use"**
```bash
# Use different port
streamlit run app.py --server.port 8502
```

**"Connection Timeout"**
```bash
# Check internet connection
# Or try again later (Yahoo Finance might be blocking)
```

**"Virtual Environment Issues"**
```bash
# Recreate environment
rmdir /s venv
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## Development

### Adding New Features

1. **Add New Stock Data**: Modify `_scrape_single_stock` method in `scraper.py`
2. **Add New Charts**: Update `create_*_chart` functions in `app.py`
3. **Add Export Formats**: Extend `save_to_*` methods in `scraper.py`

### Code Structure

- **WebScraper Class**: Core scraping functionality
- **Streamlit App**: Web interface components
- **Batch Scripts**: Easy deployment tools

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- **Yahoo Finance** - Real-time stock data source
- **Streamlit** - Web framework for the GUI
- **BeautifulSoup** - HTML parsing library
- **Plotly** - Interactive charting library

## Contact

- **GitHub**: https://github.com/17app001/AI_Python_Project
- **Issues**: Report bugs and feature requests on GitHub Issues

---

**Disclaimer**: This tool is for educational and informational purposes only. Stock market data is provided "as is" without any warranties. Always verify financial data from official sources before making investment decisions.

**Rate Limiting**: The scraper includes built-in delays to respect Yahoo Finance's terms of service. Please use responsibly.
