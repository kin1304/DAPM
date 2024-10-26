import pandas as pd
import numpy as np

class TwoPhase:
    def __init__(self, df, threshold=30):
        self.df = pd.DataFrame(data=df)
        self.threshold = threshold
        self.grouped_data = self.fit()

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

        # Remove the unnamed index column as it is not needed
        #self.df = self.df.drop(columns=['Unnamed: 0'])

        # Calculate utilities for each item
        self.df['utility'] = self.df['quantities'] * self.df['unit_price']

        # Group by transaction to create lists of items and utilities for each transaction
        grouped_data = self.df.groupby('transaction').agg({
            'items': list,
            'utility': list
        }).reset_index()

        # Rename columns to match user’s request
        grouped_data = grouped_data.rename(columns={'items': 'items', 'utility': 'utilities'})

        return grouped_data

    def run(self):
        print(self.grouped_data[:5])