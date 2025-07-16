# Ứng dụng Trực quan hóa và Khai phá Tập mục Tiện ích cao (High-Utility Itemsets/Sequences)

## Giới thiệu

Đồ án này xây dựng một ứng dụng trực quan hóa dữ liệu, hỗ trợ khai phá các tập mục tiện ích cao (High-Utility Itemsets - HUI) và chuỗi tiện ích cao (High-Utility Sequential - HUS) từ các tập dữ liệu giao dịch. Ứng dụng cho phép người dùng tải lên dữ liệu, lựa chọn thuật toán khai phá, điều chỉnh ngưỡng tiện ích, xem kết quả và trực quan hóa bằng biểu đồ.

## Tính năng chính

- **Tải dữ liệu**: Hỗ trợ định dạng TXT, CSV, Excel.
- **Tiền xử lý & nhóm dữ liệu**: Tự động nhóm dữ liệu theo giao dịch hoặc người dùng.
- **Chọn bài toán & thuật toán**:
  - High-Utility Itemsets: Two-Phase, HUI-Miner, (EFIM - đang phát triển)
  - High-Utility Sequential: USpan, (HUS-Span, PrefixSpan - đang phát triển)
- **Điều chỉnh ngưỡng tiện ích**: Nhập giá trị min utility để lọc tập mục/chuỗi có tiện ích cao.
- **Hiển thị kết quả**: Danh sách tập mục tiện ích cao, tần suất, giá trị tiện ích.
- **Trực quan hóa**: Biểu đồ scatter thể hiện mối quan hệ giữa tần suất và tiện ích.
- **Xuất kết quả**: Hỗ trợ xuất ra CSV hoặc Excel.

## Cách sử dụng

1. **Chạy ứng dụng**:
   ```bash
   streamlit run home.py
   ```
2. **Tải dữ liệu**: Chọn file TXT/CSV/Excel, cấu hình header và ký tự phân tách nếu cần.
3. **Chọn nhóm bài toán**: HUI hoặc HUS.
4. **Chọn thuật toán**: Two-Phase, HUI-Miner, USpan,...
5. **Nhập ngưỡng tiện ích**: Điều chỉnh giá trị min utility.
6. **Xem kết quả**: Kết quả sẽ hiển thị trên giao diện cùng biểu đồ trực quan.
7. **Xuất kết quả**: Chọn định dạng và tải về.

## Cấu trúc thư mục

- `home.py`: Giao diện chính Streamlit.
- `Helpers/`: Chứa các module xử lý thuật toán, tiền xử lý, vẽ biểu đồ.
  - `AlgorithmHelpers/`: Thuật toán khai phá HUI/HUS.
  - `LoadFileHelpers/`: Tiền xử lý và nhóm dữ liệu.
  - `PlotHelpers.py`: Vẽ biểu đồ.
- `dataset/`: Chứa các file dữ liệu mẫu.
- `requirements.txt`: Thư viện cần thiết.

## Thuật toán hỗ trợ

- **Two-Phase**: Khai phá tập mục tiện ích cao dựa trên TWU.
- **HUI-Miner**: Khai phá tập mục tiện ích cao không sinh ứng viên.
- **USpan**: Khai phá chuỗi tiện ích cao.

## Yêu cầu cài đặt

- Python >= 3.8
- Cài đặt thư viện:
  ```bash
  pip install -r requirements.txt
  ```

## Đóng góp

Mọi ý kiến đóng góp hoặc báo lỗi xin gửi về nhóm phát triển. 