import itertools
from collections import defaultdict
import pandas as pd

class TwoPhase:
    def __init__(self, uploaded_file):
        """
        Khởi tạo lớp TwoPhase và xử lý file được truyền vào.
        
        Parameters:
        uploaded_file (UploadedFile): File được truyền từ giao diện Streamlit.
        """
        self.transactions = []
        self.min_utility = 30  # Có thể thay đổi giá trị này theo nhu cầu
        self._load_data(uploaded_file)

    def _load_data(self, uploaded_file):
        """
        Hàm nội bộ để tải dữ liệu từ file truyền vào.
        
        Parameters:
        uploaded_file (UploadedFile): File được truyền từ giao diện Streamlit.
        """
        try:
            # Đọc dữ liệu từ file
            lines = uploaded_file.getvalue().decode("utf-8").splitlines()
            for line in lines:
                parts = line.strip().split(':')
                items = list(map(int, parts[0].split()))
                total_utility = int(parts[1])
                utilities = list(map(int, parts[2].split()))
                self.transactions.append((items, total_utility, utilities))
            print("Dữ liệu đã được tải thành công.")
        except Exception as e:
            print(f"Lỗi khi đọc dữ liệu từ file: {e}")

    def calculate_twu(self):
        """
        Tính toán TWU - Trọng số Tiện ích Giao Dịch cho các mục.
        """
        item_twu = defaultdict(int)
        for items, total_utility, _ in self.transactions:
            for item in items:
                item_twu[item] += total_utility
        return item_twu

    def generate_candidates(self, itemsets, length):
        """
        Tạo các tập ứng viên có kích thước lớn hơn.
        
        Parameters:
        itemsets (list): Danh sách các mục.
        length (int): Kích thước của tập ứng viên.
        
        Returns:
        list: Danh sách các tập ứng viên.
        """
        return list(itertools.combinations(itemsets, length))

    def calculate_utility(self, itemset):
        """
        Tính toán tiện ích cho các tập con có kích thước lớn hơn 1.
        
        Parameters:
        itemset (tuple): Tập hợp các mục.
        
        Returns:
        tuple: (support, utility) của tập hợp.
        """
        utility = 0
        support_count = 0
        for items, _, utilities in self.transactions:
            if set(itemset).issubset(set(items)):
                support_count += 1
                for item in itemset:
                    utility += utilities[items.index(item)]
        support = support_count / len(self.transactions)
        return support, utility

    def filter_candidates(self, candidates):
        """
        Lọc các ứng viên có ultility < minUtility.
        
        Parameters:
        candidates (list): Danh sách các tập ứng viên.
        
        Returns:
        list: Danh sách các tập mẫu tiện ích cao.
        """
        high_utility_itemsets = []
        for itemset in candidates:
            support, utility = self.calculate_utility(itemset)
            if utility >= self.min_utility:
                high_utility_itemsets.append((itemset, support, utility))
        return high_utility_itemsets

    def twophase(self):
        """
        Thuật toán two-phase để tìm các tập mẫu tiện ích cao.
        
        Returns:
        list: Danh sách các tập mẫu tiện ích cao.
        """
        item_twu = self.calculate_twu()
        initial_candidates = [item for item in item_twu if item_twu[item] >= self.min_utility]

        high_utility_itemsets = []

        # Tạo các tập ứng viên với kích thước là 1
        k = 1
        current_candidates = [(item,) for item in initial_candidates]

        # Tạo sinh các tập ứng viên với kích thước lớn dần
        while current_candidates:
            high_utility_itemsets.extend(self.filter_candidates(current_candidates))
            k += 1
            current_candidates = self.generate_candidates(initial_candidates, k)

        return high_utility_itemsets

    def write_high_utility_itemsets(self, high_utility_itemsets, output_file_path):
        """
        Ghi các tập mẫu tiện ích cao vào file kết quả.
        
        Parameters:
        high_utility_itemsets (list): Danh sách các tập mẫu tiện ích cao.
        output_file_path (str): Đường dẫn file kết quả.
        """
        with open(output_file_path, 'w') as file:
            for itemset, support, utility in high_utility_itemsets:
                itemset_str = ' '.join(map(str, itemset))
                file.write(f"{itemset_str} #SUP: {support:.1f} #UTIL: {utility}\n")

    def run(self):
        """
        Chạy thuật toán Two-Phase và in ra kết quả.
        """
        if self.transactions:
            high_utility_itemsets = self.twophase()
            # Hiển thị kết quả
            for itemset, support, utility in high_utility_itemsets:
                itemset_str = ' '.join(map(str, itemset))
                print(f"{itemset_str} #SUP: {support:.1f} #UTIL: {utility}")
        else:
            print("Dữ liệu chưa được tải thành công. Không thể chạy thuật toán.")
