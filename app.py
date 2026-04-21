#!/usr/bin/env python3
"""
Taiwan Hot Stocks GUI Application
Streamlit-based web interface for stock data visualization
"""

import streamlit as st
import sys
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import time
from datetime import datetime
from pathlib import Path

# Add src directory to Python path
sys.path.append(str(Path(__file__).parent / "src"))

from scraper import WebScraper


def setup_page_config():
    """Setup Streamlit page configuration"""
    st.set_page_config(
        page_title="Taiwan Hot Stocks",
        page_icon=":chart_with_upwards_trend:",
        layout="wide",
        initial_sidebar_state="expanded"
    )


def load_css():
    """Load custom CSS for better styling"""
    st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 1rem;
    }
    .stock-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 10px;
        margin: 0.5rem 0;
        color: white;
    }
    .price-up {
        color: #00c853;
        font-weight: bold;
    }
    .price-down {
        color: #d32f2f;
        font-weight: bold;
    }
    .metric-container {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 8px;
        margin: 0.5rem 0;
    }
    </style>
    """, unsafe_allow_html=True)


def create_stock_card(stock_data):
    """Create a styled card for stock information"""
    price_change = stock_data['price_change']
    is_positive = '+' in price_change
    
    change_class = "price-up" if is_positive else "price-down"
    change_symbol = "arrow_up" if is_positive else "arrow_down"
    
    card_html = f"""
    <div class="stock-card">
        <h3>{stock_data['stock_code']} - {stock_data['company_name']}</h3>
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <div>
                <h2 style="margin: 0;">{stock_data['current_price']}</h2>
                <p class="{change_class}" style="margin: 0;">
                    {stock_data['price_change']} ({stock_data['price_change_percent']})
                </p>
            </div>
            <div style="text-align: right;">
                <p style="margin: 0;">Volume: {stock_data['volume']}</p>
                <p style="margin: 0;">Market Cap: {stock_data['market_cap']}</p>
            </div>
        </div>
    </div>
    """
    
    return card_html


def create_price_chart(stocks_data):
    """Create a price comparison chart"""
    df = pd.DataFrame(stocks_data)
    
    # Clean price data (remove commas and convert to float)
    df['price_numeric'] = df['current_price'].str.replace(',', '').astype(float)
    
    fig = px.bar(
        df, 
        x='stock_code', 
        y='price_numeric',
        title='Stock Price Comparison',
        labels={'price_numeric': 'Price (NT$)', 'stock_code': 'Stock Code'},
        color='price_numeric',
        color_continuous_scale='viridis'
    )
    
    fig.update_layout(
        xaxis_title="Stock Code",
        yaxis_title="Price (NT$)",
        showlegend=False
    )
    
    return fig


def create_volume_chart(stocks_data):
    """Create a volume comparison chart"""
    df = pd.DataFrame(stocks_data)
    
    # Clean volume data (remove commas and convert to int)
    df['volume_numeric'] = df['volume'].str.replace(',', '').astype(int)
    
    fig = px.bar(
        df,
        x='stock_code',
        y='volume_numeric',
        title='Trading Volume Comparison',
        labels={'volume_numeric': 'Volume', 'stock_code': 'Stock Code'},
        color='volume_numeric',
        color_continuous_scale='blues'
    )
    
    fig.update_layout(
        xaxis_title="Stock Code",
        yaxis_title="Volume",
        showlegend=False
    )
    
    return fig


def create_change_chart(stocks_data):
    """Create a price change chart"""
    df = pd.DataFrame(stocks_data)
    
    # Extract numeric change values
    df['change_numeric'] = df['price_change'].str.replace('+', '').str.replace(',', '').astype(float)
    df['change_percent_numeric'] = df['price_change_percent'].str.replace('%', '').str.replace('+', '').astype(float)
    
    fig = make_subplots(
        rows=1, cols=2,
        subplot_titles=('Price Change (NT$)', 'Change (%)'),
        specs=[[{"secondary_y": False}, {"secondary_y": False}]]
    )
    
    # Add bar chart for price change
    colors = ['green' if x >= 0 else 'red' for x in df['change_numeric']]
    fig.add_trace(
        go.Bar(x=df['stock_code'], y=df['change_numeric'], name='Change (NT$)', marker_color=colors),
        row=1, col=1
    )
    
    # Add bar chart for percentage change
    fig.add_trace(
        go.Bar(x=df['stock_code'], y=df['change_percent_numeric'], name='Change (%)', marker_color=colors),
        row=1, col=2
    )
    
    fig.update_layout(
        title_text="Stock Price Changes",
        showlegend=False,
        height=400
    )
    
    return fig


def display_metrics(stocks_data):
    """Display key metrics in columns"""
    df = pd.DataFrame(stocks_data)
    
    # Calculate metrics
    total_volume = df['volume'].str.replace(',', '').astype(int).sum()
    avg_change = df['price_change_percent'].str.replace('%', '').str.replace('+', '').astype(float).mean()
    highest_price = df['current_price'].str.replace(',', '').astype(float).max()
    lowest_price = df['current_price'].str.replace(',', '').astype(float).min()
    
    # Display metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            "Total Volume",
            f"{total_volume:,}",
            delta=None
        )
    
    with col2:
        st.metric(
            "Average Change",
            f"{avg_change:.2f}%",
            delta=None
        )
    
    with col3:
        st.metric(
            "Highest Price",
            f"NT${highest_price:,.2f}",
            delta=None
        )
    
    with col4:
        st.metric(
            "Lowest Price",
            f"NT${lowest_price:,.2f}",
            delta=None
        )


def main():
    """Main Streamlit application"""
    setup_page_config()
    load_css()
    
    # Header
    st.markdown('<h1 class="main-header">Taiwan Hot Stocks Dashboard</h1>', unsafe_allow_html=True)
    st.markdown("---")
    
    # Sidebar
    st.sidebar.header("Control Panel")
    
    # Refresh button
    if st.sidebar.button("Refresh Data", type="primary"):
        st.rerun()
    
    # Auto-refresh option
    auto_refresh = st.sidebar.checkbox("Auto-refresh (30 seconds)")
    if auto_refresh:
        st.rerun()
    
    # Stock count selector
    stock_count = st.sidebar.slider("Number of stocks to display", 1, 10, 5)
    
    # Main content
    try:
        with st.spinner("Fetching stock data..."):
            # Initialize scraper
            scraper = WebScraper(delay=1.5, timeout=15)
            
            # Scrape stock data
            stocks_data = scraper.scrape_taiwan_hot_stocks(limit=stock_count)
            
            if stocks_data:
                # Display last update time
                st.sidebar.info(f"Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
                
                # Display metrics
                st.subheader("Key Metrics")
                display_metrics(stocks_data)
                
                st.markdown("---")
                
                # Display stock cards
                st.subheader("Stock Information")
                cols = st.columns(min(len(stocks_data), 3))
                
                for i, stock in enumerate(stocks_data):
                    with cols[i % len(cols)]:
                        st.markdown(create_stock_card(stock), unsafe_allow_html=True)
                
                st.markdown("---")
                
                # Charts section
                st.subheader("Visualizations")
                
                # Chart tabs
                tab1, tab2, tab3 = st.tabs(["Price Comparison", "Volume Analysis", "Price Changes"])
                
                with tab1:
                    fig_price = create_price_chart(stocks_data)
                    st.plotly_chart(fig_price, use_container_width=True)
                
                with tab2:
                    fig_volume = create_volume_chart(stocks_data)
                    st.plotly_chart(fig_volume, use_container_width=True)
                
                with tab3:
                    fig_change = create_change_chart(stocks_data)
                    st.plotly_chart(fig_change, use_container_width=True)
                
                st.markdown("---")
                
                # Data table
                st.subheader("Detailed Data")
                df = pd.DataFrame(stocks_data)
                st.dataframe(df, use_container_width=True)
                
                # Download button
                csv = df.to_csv(index=False)
                st.download_button(
                    label="Download CSV",
                    data=csv,
                    file_name=f"taiwan_stocks_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                    mime="text/csv"
                )
                
            else:
                st.error("Failed to fetch stock data. Please try again later.")
                st.info("Possible reasons:")
                st.info("- Network connectivity issues")
                st.info("- Yahoo Finance blocking requests")
                st.info("- Market being closed")
    
    except Exception as e:
        st.error(f"An error occurred: {e}")
        st.info("Please try refreshing the page.")
    
    # Footer
    st.markdown("---")
    st.markdown(
        "<div style='text-align: center; color: gray;'>"
        "Taiwan Hot Stocks Dashboard | Data source: Yahoo Finance"
        "</div>", 
        unsafe_allow_html=True
    )


if __name__ == "__main__":
    main()
