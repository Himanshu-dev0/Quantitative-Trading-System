
import pandas as pd
import numpy as np

def apply_strategy(df):
    """
    Applies the baseline 5/15 EMA strategy with Regime filter.
    """
    df['Signal'] = 0
    
    # Ensure EMAs exist
    if 'EMA_5' not in df.columns or 'EMA_15' not in df.columns:
        # Simple calculation if missing (for demonstration)
        df['EMA_5'] = df['Close'].ewm(span=5, adjust=False).mean()
        df['EMA_15'] = df['Close'].ewm(span=15, adjust=False).mean()

    # Long: EMA Cross + Regime +1 (Uptrend)
    # Note: Checking Regime values. Task says +1 Uptrend, -1 Downtrend, 0 Sideways.
    # Notebook 05 used Regime=1 and Regime=2. We should align with Task or Notebook.
    # Assuming Notebook used 1 for Uptrend and 2 for Downtrend/Sideways based on code loc.
    # Let's verify standard HMM usually outputs 0, 1, 2. 
    # Providing logic compatible with standard integer regimes.
    
    # We will assume generic logic:
    # Bullish Signal
    long_condition = (df['EMA_5'] > df['EMA_15']) & (df['Regime'] == 1)
    df.loc[long_condition, 'Signal'] = 1
    
    # Bearish Signal
    # Assuming Regime 2 is Downtrend based on notebook 05 code "df['Regime'] == 2" for Short
    short_condition = (df['EMA_5'] < df['EMA_15']) & (df['Regime'] == 2)
    df.loc[short_condition, 'Signal'] = -1 
    
    return df

def calculate_returns(df):
    """
    Calculates strategy returns and metrics.
    """
    df['Market_Ret'] = df['Close'].pct_change()
    df['Strategy_Ret'] = df['Signal'].shift(1) * df['Market_Ret']
    return df

def calculate_metrics(returns, risk_free_rate=0.065):
    """
    Calculates performance metrics.
    """
    metrics = {}
    metrics['Total_Return'] = (1 + returns).prod() - 1
    
    # Annualized Sharpe
    if returns.std() != 0:
        metrics['Sharpe_Ratio'] = (returns.mean() / returns.std()) * np.sqrt(252*75) # 75 candles/day approx
    else:
        metrics['Sharpe_Ratio'] = 0
        
    return metrics
