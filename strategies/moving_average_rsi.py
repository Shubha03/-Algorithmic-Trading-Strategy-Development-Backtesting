import backtrader as bt


class MovingAverageRSIStrategy(bt.Strategy):

    params = (

        # EMA periods
        ('fast_ma', 50),
        ('slow_ma', 200),

        # RSI
        ('rsi_period', 14),

        # Risk management
        ('stop_loss', 0.08),
        ('take_profit', 0.20),

        # Position sizing
        ('risk_per_trade', 0.10),
    )

    def __init__(self):

        # Fast EMA
        self.fast_ma = (
            bt.indicators.ExponentialMovingAverage(
                self.data.close,
                period=self.params.fast_ma
            )
        )

        # Slow EMA
        self.slow_ma = (
            bt.indicators.ExponentialMovingAverage(
                self.data.close,
                period=self.params.slow_ma
            )
        )

        # RSI
        self.rsi = (
            bt.indicators.RSI(
                self.data.close,
                period=self.params.rsi_period
            )
        )

        # ATR
        self.atr = (
            bt.indicators.ATR(
                self.data,
                period=14
            )
        )

        # EMA crossover
        self.crossover = (
            bt.indicators.CrossOver(
                self.fast_ma,
                self.slow_ma
            )
        )

        self.buy_price = None

    def next(self):

        current_price = (
            self.data.close[0]
        )

       
        # ENTRY CONDITIONS
        

        if not self.position:

            bullish_trend = (
                self.fast_ma[0]
                > self.slow_ma[0]
            )

            bullish_crossover = (
                self.crossover > 0
            )

            healthy_rsi = (
                50 < self.rsi[0] < 65
            )

            sufficient_volatility = (
                self.atr[0] > 1
            )

            if (
                bullish_trend
                and bullish_crossover
                and healthy_rsi
                and sufficient_volatility
            ):

                cash_to_use = (
                    self.broker.getcash()
                    * self.params.risk_per_trade
                )

                size = int(
                    cash_to_use
                    / current_price
                )

                if size > 0:

                    self.buy(size=size)

                    self.buy_price = (
                        current_price
                    )


        # EXIT CONDITIONS
  

        else:

            stop_loss_price = (
                self.buy_price
                * (
                    1 - self.params.stop_loss
                )
            )

            take_profit_price = (
                self.buy_price
                * (
                    1 + self.params.take_profit
                )
            )

            bearish_trend = (
                self.fast_ma[0]
                < self.slow_ma[0]
            )

            overbought = (
                self.rsi[0] > 75
            )

            stop_loss_hit = (
                current_price
                < stop_loss_price
            )

            take_profit_hit = (
                current_price
                > take_profit_price
            )

            if (
                bearish_trend
                or overbought
                or stop_loss_hit
                or take_profit_hit
            ):

                self.sell()