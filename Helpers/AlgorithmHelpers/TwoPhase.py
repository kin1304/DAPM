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
        self.fit()

    def fit(self):
        first_three = dict(list(self.data.items())[:3])
        print(first_three)

    def run(self):
        pass

