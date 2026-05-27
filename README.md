# Algorithmic Trading Strategy Backtesting System

## Overview

The system performs:

- Historical Backtesting
- Walk-Forward Analysis (WFA)
- Robustness Evaluation

The project is built using Python and Backtrader.

---

# Project Structure

```text
trading-strategy/
│
├── backtest/
│   └── run_backtest.py
│
├── data/
│   └── AAPL.csv
│
├── robustness/
│   └── robustness_score.py
│
├── strategies/
│   └── moving_average_rsi.py
│
├── walk_forward/
│   └── walk_forward_analysis.py
│
├── main.py
├── requirements.txt
└── README.md
```

---

# Setup Instructions

## 1. Clone Repository

https://github.com/Shubha03/-Algorithmic-Trading-Strategy-Development-Backtesting.git

cd trading-strategy 


## 3. Install Dependencies

pip install -r requirements.txt


# Run the Project

Run the main file:

```bash
python main.py
```

This will:

- Run the backtest
- Perform Walk-Forward Analysis
- Calculate robustness score
- Display final results summary

---


# Results Summary

| Metric                       | Value        |
|------------------------------|-------------|
| Stock Symbol                 | AAPL        |
| Backtest Period              | 2018–2025   |
| Starting Capital             | $100,000    |
| Percentage Return on Capital | 12.81%      |
| Maximum Drawdown             | 3.43%       |
| Walk-Forward Analysis Score  | 72.46       |
| Robustness Score             | 81.65 (>75) |

---

# Key Learnings

During this assignment, I learned:

- How to build a complete backtesting pipeline
- How algorithmic trading strategies are tested
- Importance of risk management
- Why Walk-Forward Analysis is critical
- How to evaluate strategy robustness
- How to avoid overfitting in trading systems
- Practical usage of Backtrader for quantitative trading

---

# Technologies Used

- Python
- Backtrader
- Pandas
- NumPy

---
