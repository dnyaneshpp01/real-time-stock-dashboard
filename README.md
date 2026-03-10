# 📈 Real-Time Stock Market ETL Pipeline & Dashboard

## Project Overview
An end-to-end data engineering and visualization project that automates the extraction of live financial data, manages storage in a relational database, and provides an interactive web interface for market analysis. 

## Architecture & Tech Stack
* **Data Extraction (API):** Python (`yfinance`) used to fetch live historical stock data for top-cap companies.
* **Data Engineering (ETL):** Python (`pandas`, `sqlalchemy`) used to clean, transform, and load data into a local database.
* **Database Management:** **MySQL** used as the backend storage layer to maintain historical records.
* **Frontend Dashboard:** **Streamlit** and **Plotly** used to build a full-stack, interactive web application featuring dynamic candlestick charts and automated KPI tracking.

## Key Features
* Automated ETL script for database updates.
* Interactive UI allowing users to filter by specific stock tickers.
* Dynamic candlestick charting for trend analysis.
* Calculated metrics for daily price fluctuations.
