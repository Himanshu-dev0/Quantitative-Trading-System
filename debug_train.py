
import sys
import os
import pandas as pd
import numpy as np
import traceback

# Add src to path
sys.path.append(os.path.abspath('src'))

try:
    print("Importing xgboost...")
    from ml_models import get_xgb_gatekeeper
    print("XGBoost imported.")
except ImportError as e:
    print(f"Failed to import xgboost or ml_models: {e}")
    sys.exit(1)

try:
    print("Loading data...")
    data_path = "results/baseline_results.csv"
    if not os.path.exists(data_path):
        print(f"Error: {data_path} not found.")
        sys.exit(1)
        
    df = pd.read_csv(data_path, index_col=0, parse_dates=True)
    print(f"Data loaded. Shape: {df.shape}")

    if 'Market_Ret' in df.columns and 'Market_Returns' not in df.columns:
        df.rename(columns={'Market_Ret': 'Market_Returns'}, inplace=True)

    print("Engineering features...")
    df['Target'] = (df['Market_Returns'].shift(-1) > 0).astype(int)
    features = ['Delta_CE', 'Delta_PE', 'Gamma', 'Vega', 'PCR_OI', 'Regime', 'Avg_IV']
    
    # Check if features exist
    missing_features = [f for f in features if f not in df.columns]
    if missing_features:
        print(f"Warning: Missing features: {missing_features}")
        # Proceeding might be dangerous if critical features are missing, but let's try with 0
    
    X = df[features].fillna(0)
    y = df['Target']
    
    print("Splitting data...")
    split = int(len(df) * 0.7)
    X_train, X_test = X.iloc[:split], X.iloc[split:]
    y_train, y_test = y.iloc[:split], y.iloc[split:]
    
    print("Training model...")
    model = get_xgb_gatekeeper()
    model.fit(X_train, y_train)
    print("Model trained.")
    
    print("Saving results...")
    df['ML_Prob'] = model.predict_proba(X)[:, 1]
    df['ML_Signal'] = np.where((df['Signal'] != 0) & (df['ML_Prob'] > 0.5), df['Signal'], 0)
    df['ML_Strategy_Returns'] = df['ML_Signal'].shift(1) * df['Market_Returns']
    
    output_path = "results/ml_results_debug.csv"
    df.to_csv(output_path)
    print(f"Results saved to {output_path}")

except Exception:
    print("An error occurred:")
    traceback.print_exc()
    sys.exit(1)
