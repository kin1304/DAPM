import streamlit as st
import pandas as pd


def load_file_csv():
    st.write("Tải file csv lên ở đây")
    uploaded_file = st.file_uploader("Chọn tệp TXT để tải lên", type="txt")
    if uploaded_file is not None:
        # Giả sử tệp TXT có định dạng giống CSV với dấu phân cách là tab hoặc dấu phẩy
        # Bạn có thể điều chỉnh tham số 'delimiter' phù hợp
        df = pd.read_csv(uploaded_file, delimiter='\t')  # Hoặc delimiter=',' nếu cần
        st.write("Xem trước dữ liệu:")
        st.dataframe(df.head())
        return uploaded_file
