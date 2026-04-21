#!/usr/bin/env python3
"""
Web Scraper Module
Encapsulates all web scraping logic and functionality
"""

import requests
import time
import csv
import json
import re
from bs4 import BeautifulSoup
from typing import Dict, List, Optional, Any
from pathlib import Path
import logging


class WebScraper:
    """Professional web scraper class with encapsulated logic"""
    
    def __init__(self, delay: float = 1.0, timeout: int = 10):
        """
        Initialize the web scraper
        
        Args:
            delay: Delay between requests in seconds
            timeout: Request timeout in seconds
        """
        self.delay = delay
        self.timeout = timeout
        self.session = requests.Session()
        self.setup_logging()
        
        # Set default headers
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
        }
        
    def setup_logging(self):
        """Setup logging configuration"""
        log_dir = Path("logs")
        log_dir.mkdir(exist_ok=True)
        
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(log_dir / "scraper.log"),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)
        
    def scrape_url(self, url: str) -> Optional[Dict[str, Any]]:
        """
        Scrape a single URL and extract basic information
        
        Args:
            url: URL to scrape
            
        Returns:
            Dictionary containing scraped data or None if failed
        """
        try:
            self.logger.info(f"Scraping URL: {url}")
            
            # Make HTTP request
            response = self._make_request(url)
            if not response:
                return None
                
            # Parse HTML
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Extract data
            data = {
                'url': url,
                'title': self._extract_title(soup),
                'description': self._extract_description(soup),
                'headings': self._extract_headings(soup),
                'links_count': len(soup.find_all('a')),
                'images_count': len(soup.find_all('img')),
                'status_code': response.status_code,
                'content_length': len(response.content),
                'scraped_at': time.strftime('%Y-%m-%d %H:%M:%S')
            }
            
            self.logger.info(f"Successfully scraped: {url}")
            return data
            
        except Exception as e:
            self.logger.error(f"Error scraping {url}: {e}")
            return None
            
        finally:
            # Apply delay between requests
            time.sleep(self.delay)
    
    def _make_request(self, url: str) -> Optional[requests.Response]:
        """
        Make HTTP request with error handling
        
        Args:
            url: Target URL
            
        Returns:
            Response object or None if failed
        """
        try:
            response = self.session.get(
                url,
                headers=self.headers,
                timeout=self.timeout
            )
            response.raise_for_status()
            return response
            
        except requests.exceptions.RequestException as e:
            self.logger.error(f"Request failed for {url}: {e}")
            return None
    
    def _extract_title(self, soup: BeautifulSoup) -> str:
        """Extract page title"""
        title_tag = soup.find('title')
        return title_tag.get_text(strip=True) if title_tag else ""
    
    def _extract_description(self, soup: BeautifulSoup) -> str:
        """Extract meta description"""
        meta_desc = soup.find('meta', attrs={'name': 'description'})
        return meta_desc.get('content', '') if meta_desc else ""
    
    def _extract_headings(self, soup: BeautifulSoup) -> Dict[str, int]:
        """Count heading tags"""
        headings = {}
        for i in range(1, 7):
            tag = f'h{i}'
            headings[tag] = len(soup.find_all(tag))
        return headings
    
    def scrape_multiple_urls(self, urls: List[str]) -> List[Dict[str, Any]]:
        """
        Scrape multiple URLs
        
        Args:
            urls: List of URLs to scrape
            
        Returns:
            List of scraped data dictionaries
        """
        results = []
        
        for url in urls:
            data = self.scrape_url(url)
            if data:
                results.append(data)
                
        return results
    
    def save_to_csv(self, data: List[Dict[str, Any]], filename: str) -> str:
        """
        Save scraped data to CSV file
        
        Args:
            data: List of dictionaries containing scraped data
            filename: Output filename
            
        Returns:
            Path to saved file
        """
        if not data:
            self.logger.warning("No data to save")
            return ""
        
        # Create data directory if it doesn't exist
        data_dir = Path("data")
        data_dir.mkdir(exist_ok=True)
        
        # Save to CSV
        filepath = data_dir / filename
        
        # Flatten nested dictionaries for CSV
        flattened_data = []
        for item in data:
            flattened_item = item.copy()
            
            # Flatten headings dictionary
            if 'headings' in flattened_item and isinstance(flattened_item['headings'], dict):
                for key, value in flattened_item['headings'].items():
                    flattened_item[f'heading_{key}'] = value
                del flattened_item['headings']
            
            flattened_data.append(flattened_item)
        
        # Write to CSV
        with open(filepath, 'w', newline='', encoding='utf-8') as csvfile:
            if flattened_data:
                fieldnames = flattened_data[0].keys()
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(flattened_data)
        
        self.logger.info(f"Data saved to {filepath}")
        return str(filepath)
    
    def save_to_json(self, data: List[Dict[str, Any]], filename: str) -> str:
        """
        Save scraped data to JSON file
        
        Args:
            data: List of dictionaries containing scraped data
            filename: Output filename
            
        Returns:
            Path to saved file
        """
        if not data:
            self.logger.warning("No data to save")
            return ""
        
        # Create data directory if it doesn't exist
        data_dir = Path("data")
        data_dir.mkdir(exist_ok=True)
        
        # Save to JSON
        filepath = data_dir / filename
        
        with open(filepath, 'w', encoding='utf-8') as jsonfile:
            json.dump(data, jsonfile, indent=2, ensure_ascii=False)
        
        self.logger.info(f"Data saved to {filepath}")
        return str(filepath)
    
    def get_session_stats(self) -> Dict[str, Any]:
        """
        Get session statistics
        
        Returns:
            Dictionary with session information
        """
        return {
            'session_cookies': len(self.session.cookies),
            'session_headers': dict(self.session.headers),
            'delay_setting': self.delay,
            'timeout_setting': self.timeout
        }
    
    def scrape_taiwan_hot_stocks(self, limit: int = 5) -> List[Dict[str, Any]]:
        """
        Scrape Taiwan's most active/hot stocks from Yahoo Finance
        
        Args:
            limit: Number of top stocks to retrieve
            
        Returns:
            List of dictionaries containing stock information
        """
        try:
            self.logger.info("Scraping Taiwan hot stocks...")
            
            # Taiwan's most popular stocks (based on market cap and trading volume)
            # These are commonly the most traded stocks on TWSE
            popular_stocks = [
                "2330.TW",  # TSMC
                "2454.TW",  # MediaTek
                "2317.TW",  # Foxconn (Hon Hai)
                "1303.TW",  # Nan Ya PCB
                "1301.TW",  # Formosa Plastics
                "2002.TW",  # China Steel
                "3008.TW",  # Largan Precision
                "2382.TW",  # Quanta Computer
                "2412.TW",  # Chunghwa Telecom
                "2882.TW",  # Cathay Financial
                "2881.TW",  # Fubon Financial
                "2890.TW",  # E.Sun Financial
                "3037.TW",  # Want Want
                "1216.TW",  # Uni-President
                "1101.TW",  # Taiwan Cement
                "2105.TW",  # Wistron
                "2379.TW",  # Realtek
                "2357.TW",  # Asustek Computer
                "2325.TW",  # Compal Electronics
                "2345.TW",  # Acer
                "2885.TW",  # Mega Financial
            ]
            
            hot_stocks_data = []
            
            # Scrape each stock's data
            for stock_code in popular_stocks[:limit]:
                stock_data = self._scrape_single_stock(stock_code)
                if stock_data:
                    hot_stocks_data.append(stock_data)
                    
            self.logger.info(f"Successfully scraped {len(hot_stocks_data)} hot stocks")
            return hot_stocks_data
            
        except Exception as e:
            self.logger.error(f"Error scraping Taiwan hot stocks: {e}")
            return []
    
    def _scrape_single_stock(self, stock_code: str) -> Optional[Dict[str, Any]]:
        """
        Scrape data for a single stock from Yahoo Finance
        
        Args:
            stock_code: Stock symbol (e.g., "2330.TW")
            
        Returns:
            Dictionary containing stock data or None if failed
        """
        try:
            url = f"https://finance.yahoo.com/quote/{stock_code}"
            
            response = self._make_request(url)
            if not response:
                return None
                
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Extract stock data
            stock_data = {
                'stock_code': stock_code,
                'company_name': self._extract_company_name(soup),
                'current_price': self._extract_current_price(soup),
                'price_change': self._extract_price_change(soup),
                'price_change_percent': self._extract_price_change_percent(soup),
                'volume': self._extract_volume(soup),
                'market_cap': self._extract_market_cap(soup),
                'scraped_at': time.strftime('%Y-%m-%d %H:%M:%S')
            }
            
            self.logger.info(f"Successfully scraped {stock_code}: {stock_data['company_name']}")
            return stock_data
            
        except Exception as e:
            self.logger.error(f"Error scraping stock {stock_code}: {e}")
            return None
    
    def _extract_company_name(self, soup: BeautifulSoup) -> str:
        """Extract company name from Yahoo Finance page"""
        # Try multiple selectors for company name
        selectors = [
            'h1',
            '[data-test="qsp-name"]',
            '.D(ib) h1',
            'title'
        ]
        
        for selector in selectors:
            element = soup.select_one(selector)
            if element:
                name = element.get_text(strip=True)
                # Remove stock code from name if present
                name = re.sub(r'\(\d+\.\w+\)', '', name).strip()
                return name
                
        return "Unknown"
    
    def _extract_current_price(self, soup: BeautifulSoup) -> str:
        """Extract current stock price"""
        selectors = [
            '[data-test="qsp-price"]',
            '.Trsdu span',
            '[data-symbol]',
            '.price-value',
            'span[data-field="regularMarketPrice"]'
        ]
        
        for selector in selectors:
            element = soup.select_one(selector)
            if element:
                return element.get_text(strip=True)
                
        return "N/A"
    
    def _extract_price_change(self, soup: BeautifulSoup) -> str:
        """Extract price change"""
        selectors = [
            '[data-test="qsp-price-change"]',
            '[data-field="regularMarketChange"]',
            '.Trsdu',
            'span[data-symbol]'
        ]
        
        for selector in selectors:
            element = soup.select_one(selector)
            if element:
                return element.get_text(strip=True)
                
        return "N/A"
    
    def _extract_price_change_percent(self, soup: BeautifulSoup) -> str:
        """Extract price change percentage"""
        selectors = [
            '[data-test="qsp-change-percent"]',
            '[data-field="regularMarketChangePercent"]',
            '.Trsdu',
            'span[data-symbol]'
        ]
        
        for selector in selectors:
            element = soup.select_one(selector)
            if element:
                return element.get_text(strip=True)
                
        return "N/A"
    
    def _extract_volume(self, soup: BeautifulSoup) -> str:
        """Extract trading volume"""
        # Look for volume in the data table
        volume_selectors = [
            '[data-test="TD_VOLUME-value"]',
            '[data-field="regularMarketVolume"]',
            'td:contains("Volume")',
            'span:contains("Volume")'
        ]
        
        for selector in volume_selectors:
            element = soup.select_one(selector)
            if element:
                return element.get_text(strip=True)
                
        return "N/A"
    
    def _extract_market_cap(self, soup: BeautifulSoup) -> str:
        """Extract market capitalization"""
        # Look for market cap in the data table
        cap_selectors = [
            '[data-test="MARKET_CAP-value"]',
            '[data-field="marketCap"]',
            'td:contains("Market Cap")',
            'span:contains("Market Cap")'
        ]
        
        for selector in cap_selectors:
            element = soup.select_one(selector)
            if element:
                return element.get_text(strip=True)
                
        return "N/A"
    
    def save_stocks_to_csv(self, stocks_data: List[Dict[str, Any]], filename: str = "taiwan_hot_stocks.csv") -> str:
        """
        Save stock data to CSV file
        
        Args:
            stocks_data: List of stock dictionaries
            filename: Output filename
            
        Returns:
            Path to saved file
        """
        if not stocks_data:
            self.logger.warning("No stock data to save")
            return ""
        
        # Create data directory if it doesn't exist
        data_dir = Path("data")
        data_dir.mkdir(exist_ok=True)
        
        # Save to CSV
        filepath = data_dir / filename
        
        # Define CSV headers
        headers = [
            'stock_code', 'company_name', 'current_price', 
            'price_change', 'price_change_percent', 'volume', 
            'market_cap', 'scraped_at'
        ]
        
        with open(filepath, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=headers)
            writer.writeheader()
            
            for stock in stocks_data:
                # Ensure all required fields are present
                row = {header: stock.get(header, 'N/A') for header in headers}
                writer.writerow(row)
        
        self.logger.info(f"Stock data saved to {filepath}")
        return str(filepath)
    
    def close_session(self):
        """Close the requests session"""
        self.session.close()
        self.logger.info("Session closed")


# Utility functions
def validate_url(url: str) -> bool:
    """
    Basic URL validation
    
    Args:
        url: URL to validate
        
    Returns:
        True if URL appears valid, False otherwise
    """
    return url.startswith(('http://', 'https://'))


def sanitize_filename(filename: str) -> str:
    """
    Sanitize filename for safe file system usage
    
    Args:
        filename: Original filename
        
    Returns:
        Sanitized filename
    """
    invalid_chars = '<>:"/\\|?*'
    for char in invalid_chars:
        filename = filename.replace(char, '_')
    return filename
