import backtrader as bt
import pandas as pd

from strategies.moving_average_rsi import (
    MovingAverageRSIStrategy
)

from walk_forward.walk_forward_analysis import (
    average_wfa_score
)

from robustness.robustness_score import (
    robustness_score
)

# BACKTRADER ENGINE


cerebro = bt.Cerebro()

cerebro.addstrategy(
    MovingAverageRSIStrategy
)


# LOAD DATA


df = pd.read_csv(
    "data/AAPL.csv",
    parse_dates=['Date'],
    index_col='Date'
)

# Flatten columns
if isinstance(df.columns, pd.MultiIndex):

    df.columns = (
        df.columns.get_level_values(0)
    )

# Required columns
df = df[
    ['Open', 'High', 'Low', 'Close', 'Volume']
]

# Convert numeric
df = df.apply(pd.to_numeric)

# DATA FEED


data = bt.feeds.PandasData(
    dataname=df
)

cerebro.adddata(data)

# PORTFOLIO SETTINGS


starting_cash = 100000

cerebro.broker.setcash(
    starting_cash
)

cerebro.broker.setcommission(
    commission=0.001
)

cerebro.broker.set_slippage_perc(
    0.001
)


# ANALYZERS


cerebro.addanalyzer(
    bt.analyzers.DrawDown,
    _name='drawdown'
)


# RUN BACKTEST


results = cerebro.run()

strategy = results[0]


# FINAL VALUE


final_value = (
    cerebro.broker.getvalue()
)


# RETURN %


total_return = (
    (
        final_value - starting_cash
    ) / starting_cash
) * 100

# DRAWDOWN


drawdown = (
    strategy.analyzers
    .drawdown
    .get_analysis()
)

max_drawdown = (
    drawdown.max.drawdown
)


# RESULTS SUMMARY


print("\n")

print("## Results Summary")

print(
    "| Metric                       | Value        |"
)

print(
    "|------------------------------|-------------|"
)

print(
    f"| Stock Symbol                 | AAPL        |"
)

print(
    f"| Backtest Period              | 2018–2025   |"
)

print(
    f"| Starting Capital             | "
    f"${starting_cash:,.0f}    |"
)

print(
    f"| Percentage Return on Capital | "
    f"{total_return:.2f}%      |"
)

print(
    f"| Maximum Drawdown             | "
    f"{max_drawdown:.2f}%       |"
)

print(
    f"| Walk-Forward Analysis Score  | "
    f"{average_wfa_score:.2f}        |"
)

print(
    f"| Robustness Score             | "
    f"{robustness_score:.2f} (> 75) |"
)

# PLOT


if __name__ == "__main__":

    cerebro.plot(
        style='candlestick'
    )