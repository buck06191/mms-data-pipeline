import numpy as np


def load_row_data(data_path: str) -> np.ndarray:
    data = np.loadtxt(data_path, delimiter=",", skiprows=1)
    return data
