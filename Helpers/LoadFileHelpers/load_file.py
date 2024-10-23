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
        header = st.checkbox("Dữ lệu có header")
        choose_delimiter = st.radio("Chọn dấu ngăn cách giữa các cột",
                                    ('Khoảng trắng', ',', '.', '-', '|', '_', ';', ':', 'Tab', 'Khác'), horizontal=True)
        if choose_delimiter == 'Khoảng trắng':
            choose_delimiter = ' '
        elif choose_delimiter == 'Tab':
            choose_delimiter = '\t'
        elif choose_delimiter == 'Khác':
            choose_delimiter = st.text_input('xin hãy nhập ký tự ngăn cách giữa các côt')
        if choose_delimiter == 'Khác':
            choose_delimiter = ' '
        if not header:
            df = pd.read_csv(uploaded_file, delimiter=choose_delimiter, header=None)
        else:
            df = pd.read_csv(uploaded_file, delimiter=choose_delimiter)
        col1, col2, col3 = st.columns([1, 2, 1])  # Cột giữa sẽ rộng hơn
        with col1:
            st.write("")  # Cột bên trái để trống
        with col2:
            st.write("Xem trước dữ liệu:")
            st.dataframe(df, width=700, height=300)
        with col3:
            st.write("")  # Cột bên phải để trống
        df_after = fill_column(df)
        col1, col2, col3 = st.columns([1, 2, 1])
        with col1:
            st.write("")  # Cột bên trái để trống
        with col2:
            st.write("Dữ liệu sau khi điền tên cột")
            st.dataframe(df_after, width=700, height=300)
        with col3:
            st.write("")  # Cột bên phải để trống
        return df_after


def fill_column(dataframe: pd.DataFrame) -> pd.DataFrame:
    items = ""
    utilities = ""
    quantities = ""
    unit_price = ""
    total_utilities = ""
    df = pd.DataFrame({})
    if not dataframe.empty:
        columns = [""] + list(dataframe.columns)
        if len(columns) > 0:
            items = st.selectbox("Chọn cột chứa tên của các sản phẩm", columns, placeholder=" ")
            if items == "":
                pass
            else:
                columns.remove(items)
        if len(columns) > 0:
            utilities = st.selectbox("Chen cột chứa hữu ích của sản phẩm", columns, placeholder=" ")
            if utilities == "":
                pass
            else:
                columns.remove(utilities)
        if len(columns):
            total_utilities = st.selectbox("Chọn cột chứa tổng hữu ích của đơn hàng", columns, placeholder=" ")
            if total_utilities == "":
                pass
            else:
                columns.remove(total_utilities)
        if len(columns) > 0:
            quantities = st.selectbox("Chọn cột cứa số lượng của sản phẩm", columns, placeholder=" ")
            if quantities == "":
                pass
            else:
                columns.remove(quantities)
        if len(columns) > 0:
            unit_price = st.selectbox("Chọn cột chứa đơn giá của sản phẩm", columns, placeholder=" ")
        if (items != "" and utilities != "") or (items != "" and quantities != "" and unit_price != ""):
            df["items"] = dataframe[items]
            if utilities != "":
                df["utilities"] = dataframe[utilities]
            if quantities != "":
                df["quantities"] = dataframe[quantities]
            if unit_price != "":
                df["unit_price"] = dataframe[unit_price]
            if total_utilities != "":
                df["total_utilities"] = dataframe[total_utilities]
    return df
