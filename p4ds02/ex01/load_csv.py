import pandas as pd

def load(path: str) -> pd.DataFrame:
    """Load a Dataframe"""
    try:
        data  = pd.read_csv(path)
        print(f"Loading dataset of dimensions {data.shape}")
        return data
    except Exception as error:
        print("Error: ", error)