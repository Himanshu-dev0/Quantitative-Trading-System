import pandas as pd
from xgboost import XGBClassifier

def get_xgb_gatekeeper():
    """
    Returns a configured XGBoost model for trade filtering.
    """
    model = XGBClassifier(
        n_estimators=100,
        learning_rate=0.1,
        max_depth=5,
        random_state=42,
        eval_metric='logloss',
    )
    return model

def get_lstm_model(input_shape):
    """
    Returns a compiled LSTM model for time-series prediction.
    input_shape: (time_steps, features)
    """
    try:
        from tensorflow.keras.models import Sequential
        from tensorflow.keras.layers import LSTM, Dense, Dropout
        from tensorflow.keras.optimizers import Adam
    except ImportError:
        print("Tensorflow not found. Please install it.")
        return None

    model = Sequential()
    # First LSTM layer
    model.add(LSTM(50, return_sequences=True, input_shape=input_shape))
    model.add(Dropout(0.2))
    
    # Second LSTM layer
    model.add(LSTM(50, return_sequences=False))
    model.add(Dropout(0.2))
    
    # Output layer (Binary classification: Up/Down)
    model.add(Dense(1, activation='sigmoid'))
    
    model.compile(optimizer=Adam(learning_rate=0.001), loss='binary_crossentropy', metrics=['accuracy'])
    return model