import pandas as pd
import streamlit as st


def group_by(data: pd.DataFrame) -> pd.DataFrame:
    df = pd.DataFrame({})
    if not pd.DataFrame(data).empty:
        columns = list(data.columns)
        if 'user' not in columns and 'transaction' not in columns:
            pass
        else:
            user_flag = False
            transaction_flag = False
            st.write("Bạn có muốn group by sản phẩm theo: ")
            if 'user' in columns:
                user_flag = st.checkbox('user')
            if 'transaction' in columns:
                transaction_flag = st.checkbox('transaction')
            if user_flag and transaction_flag:
                df = pd.DataFrame(data.groupby(by=['transaction', 'user'], as_index=False).sum())
                df['user'] = df['user'].astype(int)
                df['transaction'] = df['transaction'].astype(int)
                return df
            elif user_flag:
                df = pd.DataFrame(data.groupby(by='user', as_index=False).sum())
                df["user"] = df["user"].astype(int)
                return df
            elif transaction_flag:
                df = pd.DataFrame(data.groupby(by='transaction', as_index=False).sum())
                df["transaction"] = df["transaction"].astype(int)
                return df
    return pd.DataFrame({})


def main(data: pd.DataFrame) -> pd.DataFrame:
    dataframe = group_by(data)
    st.dataframe(dataframe, width=1400, height=300)
    return dataframe
