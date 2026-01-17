import os
import subprocess
import sys

# List of notebooks in the exact order they must run
notebooks = [
    "notebooks/01_data_acquisition.ipynb",
    "notebooks/02_data_cleaning.ipynb",
    "notebooks/03_regime_detection.ipynb",
    "notebooks/04_feature_engineering.ipynb",
    "notebooks/05_baseline_strategy.ipynb",
    "notebooks/06_ml_models.ipynb",
    "notebooks/07_outlier_analysis.ipynb",
    "notebooks/08_lstm_strategy.ipynb"
    
]

def run_notebook(path):
    print(f"--- Running {path} ---")
    
    # We bypass the 'jupyter' command and call nbconvert directly as a module
    # This avoids the "command not found" error on Windows
    command = [
        sys.executable, "-m", "nbconvert", 
        "--to", "notebook", 
        "--execute", 
        "--inplace", 
        path
    ]
    
    result = subprocess.run(
        command, 
        capture_output=True, 
        text=True, 
        shell=True 
    )
    
    if result.returncode == 0:
        print(f"✅ Success: {path}")
    else:
        print(f"❌ Error in {path}:")
        # If it fails, we want to see the exact error inside the notebook
        error_msg = result.stderr if result.stderr else result.stdout
        print(error_msg)
        return False
    return True

if __name__ == "__main__":
    # Check if we are in the right folder
    if not os.path.exists("notebooks"):
        print("Error: 'notebooks' folder not found. Run this from the project root.")
    else:
        for nb in notebooks:
            if not run_notebook(nb):
                print("\n🛑 Pipeline stopped due to an error.")
                sys.exit(1)

        print("\n🎉 All notebooks executed! Check the /results and /plots folders.")