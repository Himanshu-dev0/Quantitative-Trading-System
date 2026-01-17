# NIFTY 50 Quantitative Strategy Pipeline

An automated trading research pipeline using HMM Regime Detection and XGBoost for NIFTY 50 intraday data.

## Project Structure

*   **/data**: Contains raw and processed CSV data files (`nifty_spot`, `futures`, `options`, `merged`).
*   **/notebooks**: Sequential Jupyter notebooks for research:
    *   `01_data_acquisition.ipynb`: Fetches market data.
    *   `02_data_cleaning.ipynb`: Cleans and pre-processes data.
    *   `03_regime_detection.ipynb`: HMM model training.
    *   `04_feature_engineering.ipynb`: Calculates Greeks and indicators.
    *   `05_baseline_strategy.ipynb`: EMA crossover strategy.
    *   `06_ml_models.ipynb`: XGBoost/LSTM model training.
    *   `07_outlier_analysis.ipynb`: Analysis of outlier trades.
*   **/src**: Python source modules:
    *   `data_utils.py`: Data fetching and saving utilities.
    *   `features.py`: Feature engineering calculations.
    *   `backtest.py`: Strategy logic and performance metrics.
    *   `ml_models.py`: Machine learning model definitions.
    *   `regime.py`: HMM regime detection logic.
    *   `greeks.py`: Option Greeks calculation helper.
*   **/models**: Saved trained models (e.g., `xgb_gatekeeper.json`).
*   **/results**: Backtest CSVs and performance reports.
*   **/plots**: Generated charts and visualizations.

## Installation Instructions

1.  **Clone the Repository**:
    ```bash
    git clone <repo_url>
    cd "Quantitative Trading System"
    ```

2.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## How to Run

1.  **Run the Full Pipeline**:
    Execute the master script to run all notebooks in order:
    ```bash
    python run_all.py
    ```

2.  **Run Individual Steps**:
    You can also run specific notebooks using Jupyter or VS Code. Start with `01_data_acquisition.ipynb` and proceed sequentially.

## Key Results Summary

*   **Baseline Strategy**: EMA 5/15 Crossover with HMM Regime Filter.
*   **Regime Detection**: Successfully identified 3 market regimes (Uptrend, Downtrend, Sideways) using Gaussian HMM.
*   **ML Enhancement**: XGBoost Classifier filter improved the Sharpe Ratio by filtering out low-probability trades.
*   **Performance**: Detailed metrics available in `results/performance_summary.txt`.

## License
[License Name]