import pandas as pd
import streamlit as st
import time

from Helpers.AlgorithmHelpers.TwoPhase import TwoPhase
from Helpers.LoadFileHelpers import load_file as lf
from Helpers.LoadFileHelpers import group_by as gr
from Helpers.AlgorithmHelpers import TwoPhase, USpan
from Helpers.AlgorithmHelpers import HUI_MinerClass

st.title('Ứng dụng Trực quan hóa Dữ liệu')

problem_group = st.selectbox('Chọn nhóm bài toán', ['High-Utilities Itemsets', 'High-Utilities Sequential'])

# Bổ sung combobox để chọn thuật toán tương ứng với nhóm bài toán đã chọn
selected_algorithm = ""
if problem_group == 'High-Utilities Itemsets':
    selected_algorithm = st.selectbox('Chọn một thuật toán để chạy', ['Two-Phase', 'HUI-Miner', 'EFIM'])
elif problem_group == 'High-Utilities Sequential':
    selected_algorithm = st.selectbox('Chọn một thuật toán để chạy', ['USpan', 'HUS-Span', 'PrefixSpan'])

min_threshold = st.number_input("Nhập giá trị hữu ích bạn muốn khai thác: ", value=1, min_value=1, key="0")

# Bước 1: Tải lên tệp
choose_tof = st.radio("Chọn định dạng file tải lên", ('TXT hoặc CSV', 'Excel'))
data = {}
if choose_tof == 'TXT hoặc CSV':
    data = lf.load_file_csv_txt()
elif choose_tof == 'Excel':
    data = lf.load_file_excel()

if not pd.DataFrame(data).empty:
    if problem_group == 'High-Utilities Itemsets':
        data = gr.main(data, problem='HUI')
    if problem_group == 'High-Utilities Sequential':
        data = gr.main(data, problem='HUS')

st.write("sau khi group_by")
st.dataframe(pd.DataFrame(data).head())


algorithm_instance = HUI_MinerClass.HUI_Miner(data, min_threshold)
# Bước 2: Chọn các thuật toán cần chạy
if selected_algorithm == 'Two-Phase':
    algorithm_instance = TwoPhase.TwoPhase(data, min_threshold)
elif selected_algorithm == 'HUI-Miner':
    algorithm_instance = HUI_MinerClass.HUI_Miner(data, min_threshold)
# elif selected_algorithm == 'EFIM':
#     algorithm_instance = EFIM()
elif selected_algorithm == 'USpan':
    algorithm_instance = USpan.USpan(data, min_threshold)
# elif selected_algorithm == 'HUS-Span':
#     algorithm_instance = HUSSpan()
# elif selected_algorithm == 'PrefixSpan':
#     algorithm_instance = PrefixSpan()

placeholder = st.empty()
threshold = st.number_input("Nhập giá trị hữu ích bạn muốn khai thác: ", value=algorithm_instance.min_threshold, min_value=algorithm_instance.min_threshold, key="1")
high_utility_itemsets = []
if len(high_utility_itemsets) == 0:
    if algorithm_instance:
        placeholder.write("Đang chạy thuật toán...")
        high_utility_itemsets = algorithm_instance.run(threshold)
        time.sleep(5)

if high_utility_itemsets:
    placeholder.write("Kết quả các tập mẫu tiện ích cao:")
    for high_utility_itemset in high_utility_itemsets:
        st.write(high_utility_itemset)
    # for itemset, support, utility in high_utility_itemsets:
    #     itemset_str = ' '.join(map(str, itemset))
    #     st.write(f"{itemset_str} #SUP: {support:.1f} #UTIL: {utility}")
else:
    st.write("Không tìm thấy tập mẫu tiện ích cao nào.")


# Bước 4: Xuất kết quả
output_format = st.radio("Chọn định dạng xuất", ('CSV', 'Excel'))

# if output_format == 'CSV':
#     csv = df.to_csv(index=False)
#     st.download_button(
#         label="Tải xuống dữ liệu dưới dạng CSV",
#         data=csv,
#         file_name='ket_qua.csv',
#         mime='text/csv',
#     )
# else:
#     towrite = io.BytesIO()
#     df.to_excel(towrite, index=False, engine='openpyxl')
#     towrite.seek(0)
#     st.download_button(
#         label="Tải xuống dữ liệu dưới dạng Excel",
#         data=towrite,
#         file_name='ket_qua.xlsx',
#         mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
#     )
