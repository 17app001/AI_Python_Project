#!/usr/bin/env python3
"""
Python Web Scraper - Main Entry Point
Author: [Your Name]
Description: A professional web scraping application
"""

import sys
import os
from pathlib import Path

# Add src directory to Python path
sys.path.append(str(Path(__file__).parent / "src"))

from scraper import WebScraper


def main():
    """Main function - entry point of the application"""
    print("=" * 60)
    print("Taiwan Hot Stocks Scraper")
    print("=" * 60)
    
    # Initialize scraper with longer delay for stock data
    scraper = WebScraper(delay=2.0, timeout=15)
    
    try:
        print("Starting to scrape Taiwan's top 5 hot stocks...")
        print("-" * 60)
        
        # Scrape Taiwan hot stocks
        stocks_data = scraper.scrape_taiwan_hot_stocks(limit=5)
        
        if stocks_data:
            print(f"\nSuccessfully scraped {len(stocks_data)} stocks:")
            print("-" * 60)
            
            # Display stock information
            for i, stock in enumerate(stocks_data, 1):
                print(f"[{i}] {stock['stock_code']} - {stock['company_name']}")
                print(f"    Current Price: {stock['current_price']}")
                print(f"    Change: {stock['price_change']} ({stock['price_change_percent']})")
                print(f"    Volume: {stock['volume']}")
                print(f"    Market Cap: {stock['market_cap']}")
                print()
            
            # Save results to CSV
            output_file = scraper.save_stocks_to_csv(stocks_data)
            print(f"Results saved to: {output_file}")
            
            # Also save to JSON for easy viewing
            json_file = scraper.save_to_json(stocks_data, "taiwan_hot_stocks.json")
            print(f"JSON data saved to: {json_file}")
            
        else:
            print("No stock data was scraped successfully")
            print("This might be due to:")
            print("- Network connectivity issues")
            print("- Yahoo Finance blocking requests")
            print("- Market being closed")
    
    except Exception as e:
        print(f"Error occurred: {e}")
    
    finally:
        # Clean up
        scraper.close_session()
    
    print("=" * 60)
    print("Stock scraping completed")


if __name__ == "__main__":
    main()
