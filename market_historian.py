import yfinance as yf
import sys
from datetime import datetime, timedelta
import numpy as np
import matplotlib.pyplot as plt
import argparse

def print_price_difference(assets, data):
    price_diff = {}
    percentage_change = {}

    for asset in assets:
        start_price = data['Close'][asset].loc[data['Close'][asset].first_valid_index()]
        end_price = data['Close'][asset].loc[data['Close'][asset].last_valid_index()]
        price_diff[asset] = end_price - start_price
        percentage_change[asset] = (price_diff[asset] / start_price) * 100

    sorted_assets = sorted(assets, key=lambda x: percentage_change[x], reverse=True)

    for asset in sorted_assets:
        if not np.isnan(price_diff[asset]) and not np.isnan(percentage_change[asset]):
            print(f"{asset}: Price difference: {price_diff[asset]:.2f}, Percentage change: {percentage_change[asset]:.2f}%")
        else:
            print(f"{asset}: Data not available")

def plot_stock_prices(assets, data):
    fig, ax = plt.subplots()

    for asset in assets:
        ax.plot(data['Close'][asset], label=asset)

    ax.legend()
    ax.set_title("Stock Prices Over Time")
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")

    plt.show()

def print_raw_data(assets, data):
    for date in data.index:
        stock_prices = [f"{asset} ({data['Close'][asset][date]:.2f})" if not np.isnan(data['Close'][asset][date]) else f"{asset} (nan)" for asset in assets]
        print(f"{date.strftime('%Y-%m-%d')}: {', '.join(stock_prices)}")

def main():
    parser = argparse.ArgumentParser(description="Fetch historical stock price data.")
    parser.add_argument("--weeks", type=int, required=True, help="Number of weeks of historical data to fetch.")
    parser.add_argument("--output", choices=["text", "graph", "all", "raw"], required=True, help="Choose output type: text, graph, all, or raw.")
    parser.add_argument("--symbols", nargs="+", required=True, help="List of stock symbols.")

    args = parser.parse_args()

    assets = args.symbols

    end_date = datetime.today()
    start_date = end_date - timedelta(weeks=args.weeks)

    data = yf.download(assets, start=start_date, end=end_date)

    if args.output in ["text", "all"]:
        print_price_difference(assets, data)

    if args.output in ["graph", "all"]:
        plot_stock_prices(assets, data)

    if args.output == "raw":
        print_raw_data(assets, data)

if __name__ == "__main__":
    main()