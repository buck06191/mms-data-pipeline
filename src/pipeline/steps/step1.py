from typing import Optional
from snirf.pysnirf2 import Snirf
from pipeline.utils.data import load_row_data
from pipeline.utils.snirf import open_snirf
import numpy as np


class Step1:
    def __init__(self, data_path: str):
        self.data_path = data_path
        self.data: Optional[np.ndarray] = None

    def run(self) -> Snirf:
        self.data = load_row_data(self.data_path)
        snirf = open_snirf()
        snirf.nirs.appendGroup()
        snirf.nirs[0].data.appendGroup()

        snirf.nirs[0].data[0].dataTimeSeries = self.data

        return snirf
