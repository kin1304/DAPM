import pandas as pd
import streamlit as st


def load_file_excel() -> pd.DataFrame:
    st.header("Tải file excel lên ở đây")
    uploaded_file = st.file_uploader("", type=["xlsx", "xls"])
    if uploaded_file is not None:
        header = st.checkbox("Dữ lệu có header")
        if header:
            df = pd.read_excel(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file, header=None)
        st.write("Xem trước dữ liệu:")
        st.dataframe(df.head())
        return df


def load_file_csv_txt() -> pd.DataFrame:
    st.header("Tải file txt lên ở đây")
    uploaded_file = st.file_uploader("", type=["txt", "csv"])
    if uploaded_file is not None:
        try:
            header = st.checkbox("Dữ lệu có header")
            choose_delimiter = st.radio("Chọn dấu ngăn cách giữa các cột",
                                        ('Khoảng trắng', ',', '.', '|', '_', ';', ':', 'Tab', 'Khác'),
                                        horizontal=True)
            if choose_delimiter == 'Khoảng trắng':
                choose_delimiter = ' '
            elif choose_delimiter == 'Tab':
                choose_delimiter = '\t'
            elif choose_delimiter == 'Khác':
                choose_delimiter = st.text_input('xin hãy nhập ký tự ngăn cách giữa các côt')
                if choose_delimiter == '':
                    choose_delimiter = ' '
            if choose_delimiter == 'Khác':
                choose_delimiter = ' '
            if not header:
                df = pd.read_csv(uploaded_file, delimiter=choose_delimiter, header=None)
            else:
                df = pd.read_csv(uploaded_file, delimiter=choose_delimiter)
            st.write("Xem trước dữ liệu:")
            st.dataframe(df, width=1400, height=300)
            df_after = fill_column(df)
            st.write("Dữ liệu sau khi chọn cột:")
            st.dataframe(df_after, width=1400, height=300)
            return df_after
        except pd.errors.ParserError as e:
            st.markdown("<span style='color:red'>Chọn dấu ngăn không phù hợp</span>", unsafe_allow_html=True)
            return pd.DataFrame({})


def fill_column(dataframe: pd.DataFrame) -> pd.DataFrame:
    try:
        data = pd.DataFrame()
        data['name'] = dataframe['name']
        data['utilities'] = dataframe['quantity'] * dataframe['price']
        data['user'] = dataframe['user']
        data['transaction'] = dataframe['transaction']
        return data
    except Exception as e:
        print(e)
        return pd.DataFrame({})

