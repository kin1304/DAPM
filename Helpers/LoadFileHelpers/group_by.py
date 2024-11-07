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
                grouped_data = (
                    data.groupby(['user', 'transaction'])
                    .apply(lambda x: {
                        "names": np.array(x['name']),
                        "utilities": np.array(x['utilities'])
                    })
                    .unstack(level=0)
                    .to_dict()
                )

                for user, transactions in grouped_data.items():
                    user_transactions = {transaction: details for transaction, details in transactions.items() if
                                         pd.notnull(details)}
                    merged_data[user] = user_transactions

        return merged_data
    return {}


def main(data: pd.DataFrame, problem: str) -> dict:
    data = group_by(data, problem)
    # st.dataframe(dataframe, width=1400, height=300)
    return data
