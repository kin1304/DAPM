import pandas as pd
import streamlit as st


def load_file_excel():
    st.header("Tải file excel lên ở đây")
    uploaded_file = st.file_uploader("", type=["xlsx", "xls"])
    if uploaded_file is not None:
        df = pd.read_excel(uploaded_file)
        st.write("Xem trước dữ liệu:")
        st.dataframe(df.head())
        return uploaded_file


def load_file_txt():
    st.header("Tải file txt lên ở đây")
    uploaded_file = st.file_uploader("", type="txt")
    if uploaded_file is not None:
        choose_delimiter = st.radio("Chọn dấu ngăn cách giữa các cột", ('Khoảng trắng', ',', '.', '-', '|', '_', ';', ':', 'Tab'), horizontal=True)
        if choose_delimiter == 'Khoảng trắng':
            choose_delimiter = ' '
        elif choose_delimiter == 'Tab':
            choose_delimiter = '\t'
        df = pd.read_csv(uploaded_file, delimiter= choose_delimiter)
        st.write("Xem trước dữ liệu:")
        st.dataframe(df.head())
        return uploaded_file
