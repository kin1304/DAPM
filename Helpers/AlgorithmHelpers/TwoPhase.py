from base64 import encode

import pandas as pd
import numpy as np
class TwoPhase:
    def __init__(self, data, threshold=30):
        if isinstance(data, dict):
            self.data = data
        else:
            try:
                self.data = dict(data)
            except (TypeError, ValueError):
                raise ValueError("Data không thể chuyển đổi thành từ điển.")
        self.threshold = threshold

    def fit(self):
        pass

    def run(self):
        pass
