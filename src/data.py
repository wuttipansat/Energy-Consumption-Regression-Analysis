from __future__ import annotations

import pandas as pd
import numpy as np
from pathlib import Path

def load_data(csv_path: str | Path,
              target_column: str = "target"
) -> pd.DataFrame:
    """Load data from a CSV file."""
    
    csv_path = Path(csv_path)

    if not csv_path.exists():
        raise FileNotFoundError(f"CSV file not found: {csv_path}")
    
    data = pd.read_csv(csv_path)

    if target_column not in data.columns:
        raise ValueError(f"CSV must contain target column: {target_column}")
    
    if not data[target_column].dtype == float or int:
        raise TypeError(f"Target column must be float or integer: {target_column}")
    
    if target_column != "target":
        data = data.rename(columns={target_column: "target"})

    
    return clean_data(df)

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    
    if "Timestamp" in df.columns:
        data['Timestamp'] = pd.to_datetime(data['Timestamp'])
        data = data.sort_values("Timestamp").reset_index(drop=True)
