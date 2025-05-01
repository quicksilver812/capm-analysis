# CAPM Analysis Tool

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.6+](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)

A Python implementation of the Capital Asset Pricing Model (CAPM) that calculates beta coefficients and expected returns for stocks relative to a market index.

## Overview

This tool implements the Capital Asset Pricing Model to analyze the relationship between a stock's returns and market returns. It:

1. Downloads historical stock and market index data using Yahoo Finance
2. Calculates monthly returns
3. Computes beta using both covariance method and regression analysis
4. Determines expected returns based on CAPM formula
5. Visualizes the regression line showing the relationship between stock and market returns

## Features

- **Data Retrieval**: Downloads historical stock prices from Yahoo Finance
- **Beta Calculation**: Computes beta using both covariance and regression methods
- **Expected Returns**: Calculates expected returns based on CAPM
- **Visualization**: Plots the CAPM regression line with actual data points
- **Flexible Analysis**: Can be used with any stock and market index available on Yahoo Finance

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/capm-analysis.git
cd capm-analysis

# Install required packages
pip install numpy pandas matplotlib yfinance
```

## Usage

```python
from capm_analysis import CAPM

# Create CAPM instance with stock, market index, and date range
capm = CAPM(['AAPL', '^GSPC'], '2018-01-01', '2023-01-01')

# Initialize and process data
capm.initialise()

# Calculate beta using covariance method
capm.calculate_beta()

# Perform regression analysis and calculate expected returns
capm.regression()
```

### Example

The default example analyzes Bajaj Finance (BAJFINANCE.NS) against the NIFTY 50 index (^NSEI):

```python
capm = CAPM(['BAJFINANCE.NS', '^NSEI'], '2010-01-01', '2017-01-01')
capm.initialise()
capm.calculate_beta()
capm.regression()
```

## Output

The program will:
1. Print the beta calculated using the covariance formula
2. Print the beta calculated using regression analysis
3. Print the expected returns based on CAPM
4. Display a graph showing the CAPM line and actual data points
   
   <img width="650" alt="Image" src="https://github.com/user-attachments/assets/9fba086e-5c0e-4c79-bfd6-f5ba65184d89" />

5. Terminal Output
   ```
   [*********************100%***********************]  1 of 1 completed
   [*********************100%***********************]  1 of 1 completed
   Beta from formula:  1.2525003127613483
   Beta from regression:  1.2525003127613485
   Expected returns:  0.08096586673883803
   ```

## How It Works

### Theory

The Capital Asset Pricing Model (CAPM) is used to:
- Calculate the relationship between systematic risk and expected return for assets
- Determine if a stock is fairly valued relative to its risk
- The formula is: E(R_i) = R_f + β_i(E(R_m) - R_f)
  - E(R_i) is the expected return of the stock
  - R_f is the risk-free rate
  - β_i is the beta of the stock
  - E(R_m) is the expected return of the market

### Key Functions

* `download_data()`: Retrieves historical stock and market index prices
* `initialise()`: Processes data and calculates monthly returns
* `calculate_beta()`: Computes beta using the covariance formula
* `regression()`: Performs regression analysis to determine alpha and beta
* `plot_regressions()`: Visualizes the CAPM regression line with actual data points

## Requirements

- Python 3.6+
- NumPy
- Pandas
- Matplotlib
- yfinance

## Customization

You can customize the analysis by:
- Changing the stock and market index tickers
- Modifying the date range for analysis
- Adjusting the risk-free rate (RISK_FREE_RATE constant)
- Using different return calculation methods (e.g., arithmetic instead of logarithmic)

## Contributing

Contributions are welcome! Potential areas for enhancement include:
- Adding multiple stock analysis capability
- Implementing rolling beta calculations
- Adding confidence intervals for beta estimates
- Creating more comprehensive visualizations (e.g., correlation plots)

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- William Sharpe for developing the Capital Asset Pricing Model
- Yahoo Finance for providing historical stock data
