import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import io

st.title('Ứng dụng Trực quan hóa Dữ liệu')

# Bước 1: Tải lên tệp TXT
uploaded_file = st.file_uploader("Chọn tệp TXT để tải lên", type="txt")

if uploaded_file is not None:
    # Giả sử tệp TXT có định dạng giống CSV với dấu phân cách là tab hoặc dấu phẩy
    # Bạn có thể điều chỉnh tham số 'delimiter' phù hợp
    df = pd.read_csv(uploaded_file, delimiter='\t')  # Hoặc delimiter=',' nếu cần

    st.write("Xem trước dữ liệu:")
    st.dataframe(df.head())

    # Bổ sung combobox để chọn nhóm bài toán
    problem_group = st.selectbox('Chọn nhóm bài toán', ['High-Utilities Itemsets', 'High-Utilities Sequential'])

    # Bổ sung combobox để chọn thuật toán tương ứng với nhóm bài toán đã chọn
    if problem_group == 'High-Utilities Itemsets':
        selected_algorithm = st.selectbox('Chọn một thuật toán để chạy', ['Two-Phase', 'HUI-Miner', 'EFIM'])
    elif problem_group == 'High-Utilities Sequential':
        selected_algorithm = st.selectbox('Chọn một thuật toán để chạy', ['USpan', 'HUS-Span', 'PrefixSpan'])

    st.write(f'Nhóm bài toán đã chọn: {problem_group}')
    st.write(f'Thuật toán đã chọn: {selected_algorithm}')

    # Bước 2: Chọn các thuật toán cần chạy
    if selected_algorithm == 'Two-Phase':
        algorithm_instance = TwoPhase() 
    elif selected_algorithm == 'HUI-Miner':
        algorithm_instance = HUIMiner()
    elif selected_algorithm == 'EFIM':
        algorithm_instance = EFIM()
    elif selected_algorithm == 'USpan':
        algorithm_instance = USpan()
    elif selected_algorithm == 'HUS-Span':
        algorithm_instance = HUSSpan()
    elif selected_algorithm == 'PrefixSpan':
        algorithm_instance = PrefixSpan()

    # Bước 3: Vẽ biểu đồ scatter
    fig, ax = plt.subplots()
    ax.scatter(df[x_column], df[y_column])
    ax.set_xlabel(x_column)
    ax.set_ylabel(y_column)
    ax.set_title(f'Biểu đồ Scatter của {y_column} so với {x_column}')
    st.pyplot(fig)

    # Bước 4: Xuất kết quả
    output_format = st.radio("Chọn định dạng xuất", ('CSV', 'Excel'))

    if output_format == 'CSV':
        csv = df.to_csv(index=False)
        st.download_button(
            label="Tải xuống dữ liệu dưới dạng CSV",
            data=csv,
            file_name='ket_qua.csv',
            mime='text/csv',
        )
    else:
        towrite = io.BytesIO()
        df.to_excel(towrite, index=False, engine='openpyxl')
        towrite.seek(0)
        st.download_button(
            label="Tải xuống dữ liệu dưới dạng Excel",
            data=towrite,
            file_name='ket_qua.xlsx',
            mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
