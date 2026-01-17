from hmmlearn import hmm
import numpy as np

def get_regime_model(n_components=3):
    """
    Returns a Gaussian HMM model for regime detection.
    """
    model = hmm.GaussianHMM(
        n_components=n_components, 
        covariance_type="full", 
        n_iter=100, 
        random_state=42
    )
    return model

def map_regimes(df, prediction_column='Regime'):
    """
    Maps HMM hidden states (0,1,2) to logical labels (-1, 0, 1)
    based on average returns.
    """
    # Calculate average return for each state
    regime_means = [df[df[prediction_column] == i]['Close'].pct_change().mean() for i in range(3)]
    
    # Sort: Lowest return = Downtrend (-1), Middle = Sideways (0), Highest = Uptrend (1)
    sorted_indices = np.argsort(regime_means)
    
    mapping = {
        sorted_indices[0]: -1,  # Downtrend
        sorted_indices[1]: 0,   # Sideways
        sorted_indices[2]: 1    # Uptrend
    }
    
    return df[prediction_column].map(mapping)