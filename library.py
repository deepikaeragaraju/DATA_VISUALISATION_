# ------------------------------------------
# Library File for Data Visualization Project
# ------------------------------------------

# Importing required Python libraries

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Optional: Style settings for better visualizations
sns.set_style("whitegrid")

def load_sample_data():
    """
    Returns a simple sample dataset used in examples.
    """
    data = {
        "month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
        "sales": [150, 180, 220, 210, 260, 300],
        "profit": [20, 25, 30, 28, 35, 40]
    }
    return pd.DataFrame(data)

# Optional Test Execution
if __name__ == "__main__":
    df = load_sample_data()
    print("Sample Data Loaded Successfully:")
    print(df)
