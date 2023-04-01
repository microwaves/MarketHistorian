# MarketHistorian

MarketHistorian is a Python script that fetches historical stock market data and calculates price differences and percentage changes for
a given list of stock symbols. It supports various output formats, including text, line graph, and raw data.

## Requirements

- Python 3.6 or higher
- yfinance
- pandas
- matplotlib

You can install the required packages using:

```bash
pip install yfinance pandas matplotlib
```

## Usage

```bash
python market_historian.py --weeks <weeks> --output <output_type> --symbols <symbol1> <symbol2> ... <symbolN>
```

- `--weeks`: Number of weeks of historical data to fetch.
- `--output`: Output format. Can be 'text', 'graph', 'raw', or 'all' (for text and graph).
- `--symbols`: Space-separated list of stock symbols.

## Examples

### Text output:

```bash
python market_historian.py --weeks 4 --output text --symbols AAPL ATVI MRNA
```

This command fetches 4 weeks of historical data for AAPL, ATVI, and MRNA, and displays the price difference and percentage change in a text format.

![Text](assets/market-historian-text.png?raw=true "Text")

### Graph output:

```bash
python market_historian.py --weeks 4 --output graph --symbols AAPL ATVI MRNA
```

This command fetches 4 weeks of historical data for AAPL, ATVI, and MRNA, and displays a line graph for each stock symbol.

![Graph](assets/market-historian-graph.png?raw=true "Graph")

### Raw output:

```bash
python market_historian.py --weeks 4 --output raw --symbols AAPL ATVI MRNA
```

This command fetches 4 weeks of historical data for AAPL, ATVI, and MRNA, and displays the raw data in a comma-separated format.

![Raw](assets/market-historian-raw.png?raw=true "Raw")

### All outputs (text and graph):

```bash
python market_historian.py --weeks 4 --output all --symbols AAPL ATVI MRNA
```

This command fetches 4 weeks of historical data for AAPL, ATVI, and MRNA, and displays both the text output and the line graph.

## Maintainers

Stephano Zanzin Ferreira - [@microwaves](https://github.com/microwaves)

## License

MarketHistorian is released under the BSD license. See [LICENSE](https://github.com/microwaves/MarketHistorian/blob/main/LICENSE).