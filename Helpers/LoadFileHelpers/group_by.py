import pandas as pd
import numpy as np


def group_by(data: pd.DataFrame, problem: str) -> dict:
    if not pd.DataFrame(data).empty:
        data = pd.DataFrame(data)
        merged_data = {}
        columns = list(data.columns)
        if 'user' not in columns and 'transaction' not in columns:
            pass
        else:
            if problem == 'HUI':
                grouped_encoded_names = data.groupby('transaction')['name'].apply(lambda x: np.array(x)).to_dict()
                grouped_utilities = data.groupby('transaction')['utilities'].apply(lambda x: np.array(x)).to_dict()
                merged_data = {
                    transaction_id: {
                        "names": grouped_encoded_names[transaction_id],
                        "utilities": grouped_utilities[transaction_id]
                    }
                    for transaction_id in grouped_encoded_names.keys()
                }

            else:  #problem == 'HUS'
                grouped_data = data.groupby('user').agg({
                    'name': list,
                    'utilities': list,
                    'transaction': list
                }).reset_index()

                # Function to group each row by 'transaction' so that 'name' and 'utilities' entries with the same 'transaction' are combined into lists
                def group_by_transaction(row):
                    # Create a dictionary where the keys are unique transactions and values are lists for names and utilities
                    grouped = {}
                    for name, utility, transaction in zip(row['name'], row['utilities'], row['transaction']):
                        if transaction not in grouped:
                            grouped[transaction] = {'name': [], 'utilities': []}
                        grouped[transaction]['name'].append(name)
                        grouped[transaction]['utilities'].append(utility)

                    # Extract the grouped names and utilities as lists and also the transaction keys as a list
                    transactions = list(grouped.keys())
                    names = [grouped[t]['name'] for t in transactions]
                    utilities = [grouped[t]['utilities'] for t in transactions]

                    return pd.Series([names, utilities, transactions])

                # Apply the grouping function to each row in the DataFrame
                grouped_data[['name', 'utilities', 'transaction']] = grouped_data.apply(group_by_transaction, axis=1)

                # Drop the 'transaction' and 'user' columns as requested
                merged_data = grouped_data.drop(columns=['transaction', 'user'])
        return merged_data
    return {}


def main(data: pd.DataFrame, problem: str) -> dict:
    data = group_by(data, problem)
    # st.dataframe(dataframe, width=1400, height=300)
    return data
