
import pandas as pd
import numpy as np
import mibian

def calculate_greeks(row, interest_rate=6.5, days_to_expiry=5):
    """
    Calculates Option Greeks using mibian.
    """
    try:
        underlying = float(row.get("Close", 0))
        strike = float(row.get("ATM_Strike", 0))
        
        iv_call = float(row.get("IV_CE", 0)) * 100
        iv_put = float(row.get("IV_PE", 0)) * 100
        
        # Call option Greeks
        call = mibian.BS([underlying, strike, interest_rate, days_to_expiry], volatility=iv_call)
        
        # Put option Greeks
        put = mibian.BS([underlying, strike, interest_rate, days_to_expiry], volatility=iv_put)
        
        return pd.Series({
            "Delta_CE": call.callDelta,
            "Gamma": call.gamma,
            "Theta_CE": call.callTheta,
            "Vega": call.vega,
            "Delta_PE": put.putDelta,
            "Theta_PE": put.putTheta
        })
    except Exception:
        return pd.Series({
            "Delta_CE": np.nan, "Gamma": np.nan, "Theta_CE": np.nan, 
            "Vega": np.nan, "Delta_PE": np.nan, "Theta_PE": np.nan
        })

def add_derived_features(df):
    """
    Adds derived features like IV Spread, PCR, etc.
    """
    df["Avg_IV"] = (df["IV_CE"] + df["IV_PE"]) / 2
    df["IV_Spread"] = df["IV_CE"] - df["IV_PE"]
    
    if "OI_CE" in df.columns and "OI_PE" in df.columns:
        df["PCR_OI"] = df["OI_PE"] / df["OI_CE"].replace(0, np.nan)
        
    if "Close_fut" in df.columns:
        df["Futures_Basis"] = (df["Close_fut"] - df["Close"]) / df["Close"]
        
    return df
