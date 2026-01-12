import kagglehub

# Download latest version
path = kagglehub.dataset_download("sobhanmoosavi/us-accidents")

print("Path to dataset files:", path)

from pathlib import Path
import pandas as pd
def load_dataset():
    dataset_dir = Path(
        kagglehub.dataset_download("sobhanmoosavi/us-accidents")
    )
    csv = next(dataset_dir.glob("*.csv"))
    return pd.read_csv(csv, nrows=5)
data = load_dataset()
print(data.head())
print(data.dtypes)