# Qstar - ml_portfolio_optimization

## Description

This project focuses on using machine learning (ML) models to identify outperforming stocks in a portfolio before they peak, allowing for strategic fund allocation.

This project is supported by QuantX.

## How to Find Outperforming Stock

Predicting profit directly can be challenging, so we explore categorical labels and temporal models (K bars) considering margin balance and short balance. The trend is more important than the actual numbers.

## Raw Data
https://drive.google.com/drive/folders/15cWxpwbFELBw_CJDNdLaaw8W2ydjvuDo?usp=sharing

Using
- data_preprocessing.py script
- 100_label.csv 
- 100_feature_past_6_months_ohlcv.csv
- stock_industry.csv

We can generate the result.csv


We uses result.csv file as the dataset to train and test the machine learning model.

## Features

### Technical Indicators (TA-Lib)

#### Goals:
1. Filter out indicators that make no sense.
2. If an indicator can be divided by moving average (MA), keep it and normalize by MA.

#### Criteria for Selecting Features:
1. Alignment across different stocks.
2. Entropy: Categorical features should have enough information.
3. Stability over different periods (from training to testing set).

### Momentum Indicators
- **Drop**: `'adx'`, `'adxr'`, `'apo'`, `'bop'`, `'cci'`, `'cmo'`, `'dx'`, `'macd'`, `'macd_x'`, `'mfi'`, `'minus_di'`, `'minus_dm'`, `'plus_di'`, `'plus_dm'`, `'ppo'`, `'roc'`, `'rocr'`, `'rocp'`, `'rocr100'`, `'rsi'`, `'trix'`, `'ultosc'`, `'willr'`
- **Keep**: `'aroonup'`, `'aroondown'`, `'aroonosc'`, `'mom'`

### Overlap Studies
- **Drop**: `'dema'`, `'ema'`, `'kama'`, `'ma'`, `'mama'`, `'sma'`, `'t3'`, `'tema'`, `'trima'`, `'wma'`, `'upperband'`, `'lowerband'`, `'ht_trendline'`, `'midpoint'`, `'midprice'`, `'sar'`, `'sarext'`
- **Keep**: `'middleband'`, `'midpoint'`, `'midprice'`

### Volume Indicators
- **Drop**: Usually use the trend, not the absolute value; normalize by volume.

### Volatility Indicators
- **Drop**: TR, ATR
- **Keep**: NATR (normalized), useful for estimating volatility
- **Description**: [NATR Indicator](https://tulipindicators.org/natr)

### Price Transform
- **Drop**: `'avgprice'`, `'medprice'`, `'typprice'`
- **Keep**: `'wclprice'`

### Cycle Indicators=
- **Keep**: HT_DCPHASE (-45 to 315)
- **Drop**: HT_PHASOR (proportional to stock price)
- **Pending**: HT_DCPERIOD, HT_SINE (similar to HT_DCPHASE), HT_TRENDMODE (always returns 1 or 0 instead of -1 as documented)

### Pattern Recognition
- **Drop**: `'cdl3starsinsouth'`, `'cdlabandonedbaby'`, `'cdlconcealbabyswall'`
- **Almost all 0, count(-100) < 50**: `'cdlbreakaway'`, `'cdl2crows'`, `'cdl3blackcrows'`, `'cdleveningdojistar'`
- **Almost all 0, count(100) < 50**: `'cdl3linestrike'`, `'cdl3whitesoldiers'`
- **Pending**: `'cdladvanceblock'`, `'cdldarkcloudcover'`, `'cdleveningstar'`, `'cdlhangingman'`
- **No +100**: `'cdldoji'`, `'cdldragonflydoji'`, `'cdlgravestonedoji'`, `'cdlhammer'`

## Label

#### Profit Statistics (Top 100 Raw Data)
- count: 12019
- mean: 1.081814
- std: 11.182851
- min: -46.226415
- 25%: -4.851116
- 50%: 0.423131
- 75%: 5.688666
- max: 142.248062

### Percentile Thresholds
- PR_50: 0.423131
- PR_60: 2.163202
- PR_70: 4.341017
- PR_80: 7.407407
- PR_90: 13.062045
- PR_97: 24.036847
- PR_99: 36.552946

## Model Training

- **Regression**: Linear Regression, XGBoost, Random Forest

## Portfolio Optimization Method

- **Initial Portfolio**: $10k across 10 stocks, e.g., 0001: $1k, 0002: $1k
- **Regression Models**:
    - Allocate based on expected return and variance, e.g., 0001: expected return 25%, variance 10% → $0.5k

### Allocation Strategy
1. Stocks with > 13% expected return: 20% of the portfolio.
2. Remaining stocks: average allocation.

## Backtesting

Integrate the ML model and allocation strategy into the original quantx trading engine backtest system

## Result

Original Portfolio backtest result:
https://drive.google.com/drive/folders/1_xweElV6_3mubQMCDZTknqTEvIal_9Sr?usp=sharing

RF Portfolio backtest result:
https://drive.google.com/drive/folders/1Dc3x6ArFm35jJHKzIweRk2MsBtecykYm?usp=sharing

## Contribution

The QStar model utilizing machine learning algorithms (Random Forest) to identify outperforming equities and rebalance the fund allocation within the QuantX portfolio, increasing return by 2.32% and lowering drawdown by 3.72%.