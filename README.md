# NIFTY 50 Quantitative Strategy Pipeline

An automated trading research pipeline using HMM Regime Detection and XGBoost for NIFTY 50 intraday data.

## Repository Structure
- **/notebooks**: 01 to 07 sequential research notebooks.
- **/src**: Modular code for Greeks (mibian) and ML models.
- **/data**: Storage for 5-minute interval OHLCV and Greeks.
- **/results**: Performance summaries and trade logs.

## Execution
To run the entire pipeline at once, ensure you have the dependencies installed and run:
`python run_all.py`

## Methodology
1. **Greeks**: Calculated using the Black-Scholes model via `mibian`.
2. **Regimes**: Gaussian Hidden Markov Model (HMM) identifies market states.
3. **ML Filter**: XGBoost model filters high-probability trade signals.