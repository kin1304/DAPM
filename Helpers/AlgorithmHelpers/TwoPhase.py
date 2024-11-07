from base64 import encode

import pandas as pd
import numpy as np
<<<<<<< Updated upstream
import itertools
from collections import defaultdict
=======
import re
>>>>>>> Stashed changes

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
<<<<<<< Updated upstream
        self.items, self.utilities = self.fit()

    def fit(self):
        """
        Transforms the dataframe by encoding items, computing utilities, and grouping transactions.
        """
        # 1. Encode items as natural numbers

        if self.df is None:
            raise ValueError("The input dataframe is None.")
        if not isinstance(self.df, pd.DataFrame):
            raise TypeError("The input is not a pandas DataFrame.")
        self.df = self.df.copy()

        # Calculate utilities for each item
        self.df['utility'] = self.df['quantities'] * self.df['unit_price']

        # Group by transaction to create lists of items and utilities for each transaction
        grouped_data = self.df.groupby('transaction').agg({
            'items': list,
            'utility': list
        }).reset_index()

        # Rename columns to match user’s request
        grouped_data = grouped_data.rename(columns={'items': 'items', 'utility': 'utilities'})
        items = grouped_data['items']
        utilities = grouped_data['utilities']
        return items, utilities

    def run(self):
        print(self.items)
        print(self.utilities)
=======
        self.dict = {}

    def run(self):
        print(self.data[:5])
>>>>>>> Stashed changes
