import mibian
import pandas as pd
import numpy as np

def calculate_greeks(row, interest_rate=6.5, days_to_expiry=5):
    """
    Calculates Option Greeks for a single row of data.
    """
    try:
        underlying = float(row['Close'])
        strike = float(row['ATM_Strike'])
        
        # Calculate Call Greeks
        c = mibian.BS([underlying, strike, interest_rate, days_to_expiry], volatility=row['IV_CE']*100)
        
        # Calculate Put Greeks
        p = mibian.BS([underlying, strike, interest_rate, days_to_expiry], volatility=row['IV_PE']*100)
        
        return pd.Series({
            'Delta_CE': c.callDelta,
            'Delta_PE': p.putDelta,
            'Gamma': c.gamma,
            'Vega': c.vega,
            'Theta_CE': c.callTheta,
            'Theta_PE': p.putTheta
        })
    except Exception as e:
        return pd.Series({
            'Delta_CE': 0, 'Delta_PE': 0, 
            'Gamma': 0, 'Vega': 0, 
            'Theta_CE': 0, 'Theta_PE': 0
        })