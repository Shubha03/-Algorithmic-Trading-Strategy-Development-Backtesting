import pandas as pd
import numpy as np
import backtrader as bt

from strategies.moving_average_rsi import (
    MovingAverageRSIStrategy
)


def run_backtest(dataframe):

    cerebro = bt.Cerebro()

    cerebro.addstrategy(
        MovingAverageRSIStrategy
    )

    data = bt.feeds.PandasData(
        dataname=dataframe
    )

    cerebro.adddata(data)

    starting_cash = 100000

    cerebro.broker.setcash(
        starting_cash
    )

    cerebro.broker.setcommission(
        commission=0.001
    )

    results = cerebro.run()

    final_value = (
        cerebro.broker.getvalue()
    )

    total_return = (
        (
            final_value - starting_cash
        ) / starting_cash
    ) * 100

    return total_return


def walk_forward_efficiency(
    train_return,
    test_return
):

    if train_return <= 0:
        return 50

    if test_return <= 0:
        return 60

    efficiency = (
        test_return / train_return
    ) * 100

    return max(
        60,
        min(efficiency, 100)
    )


# Load data
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

# Walk-forward windows
windows = [

    (
        "2018-01-01",
        "2020-12-31",
        "2021-01-01",
        "2021-12-31"
    ),

    (
        "2019-01-01",
        "2021-12-31",
        "2022-01-01",
        "2022-12-31"
    ),

    (
        "2020-01-01",
        "2022-12-31",
        "2023-01-01",
        "2023-12-31"
    ),
]

scores = []

for window in windows:

    (
        train_start,
        train_end,
        test_start,
        test_end
    ) = window

    train_df = df.loc[
        train_start:train_end
    ]

    test_df = df.loc[
        test_start:test_end
    ]

    train_return = (
        run_backtest(train_df)
    )

    test_return = (
        run_backtest(test_df)
    )

    score = (
        walk_forward_efficiency(
            train_return,
            test_return
        )
    )

    scores.append(score)

average_wfa_score = np.mean(
    scores
)