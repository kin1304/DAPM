from typing import Any
import numpy as np
import pandas as pd
from numpy import ndarray, dtype


def read(data: dict) -> tuple[ndarray[Any, dtype[Any]], ndarray[Any, dtype[Any]]]:
    names = []
    utilities = []
    for key, value in data.items():
        df = pd.DataFrame(value)
        df["utilities"] = df["utilities"].astype(float)
        df = df.groupby("names", as_index=False).sum()
        names.append(df["names"].values)
        utilities.append(df["utilities"].values)
    # Chuyển đổi thành các mảng đa chiều (số transaction x số name trong mỗi transaction)
    names_array = np.array(names, dtype=object)
    utilities_array = np.array(utilities, dtype=object)
    return names_array, utilities_array
