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
        use_label_encoder=False
    )
    return model