
from statistics import median_grouped

import pandas as pd
import streamlit as st
import numpy as np


def group_by(data: pd.DataFrame, problem=""):
    df = pd.DataFrame({})
    if not pd.DataFrame(data).empty:
        data = pd.DataFrame(data)

        columns = list(data.columns)
        if 'user' not in columns and 'transaction' not in columns:
            pass
        else:
            # mã hóa name
            data['name_encoded'] = data['name'].astype('category').cat.codes
            name_mapping = dict(enumerate(data['name'].astype('category').cat.categories))
            # từ điển lưu trữ
            name_mapping_dict = {v: k for k, v in name_mapping.items()}
            # st.dataframe(data,  width=1400, height=300)

            merged_data = {}
            if (problem == 'HUI'):

                grouped_encoded_names = data.groupby('transaction')['name_encoded'].apply(lambda x: np.array(x)).to_dict()
                grouped_utilities = data.groupby('transaction')['utilities'].apply(lambda x: np.array(x)).to_dict()

                merged_data = {
                    transaction_id: {
                        "encoded_names": grouped_encoded_names[transaction_id],
                        "utilities": grouped_utilities[transaction_id]
                    }
                    for transaction_id in grouped_encoded_names.keys()
                }

            else: #problem == 'HUS'
                grouped_data = (
                    data.groupby(['user', 'transaction'])
                    .apply(lambda x: {
                        "encoded_names": np.array(x['name_encoded']),
                        "utilities": np.array(x['utilities'])
                    })
                    .unstack(level=0)
                    .to_dict()
                )

                for user, transactions in grouped_data.items():
                    user_transactions = {transaction: details for transaction, details in transactions.items() if
                                         pd.notnull(details)}
                    merged_data[user] = user_transactions

        return merged_data, name_mapping_dict

    return pd.DataFrame({})


def main(data: pd.DataFrame, problem="") -> pd.DataFrame:
    dataframe, items_dict = group_by(data, problem)
    # st.dataframe(dataframe, width=1400, height=300)
    return dataframe, items_dict

