import numpy as np
import streamlit as st
from collections import defaultdict

import Helpers.AlgorithmHelpers.read_dict as rd
import Helpers.AlgorithmHelpers.rename as rn

def ndarray_to_nested_list(array):
    if isinstance(array, np.ndarray):
        return [ndarray_to_nested_list(subarray) for subarray in array]
    else:
        return array

class USpan:
    def __init__(self, data:dict, min_threshold):
        self.data = data
        self.min_threshold = min_threshold
        self.max_length = 4 #độ dài chuỗi tối đa
        self.names, self.utilities = rd.read(self.data)
        self.names = ndarray_to_nested_list(data['name'])
        self.names = [
            [[int(value) for value in group] for group in row]
            for row in self.names
        ]
        self.utilities = ndarray_to_nested_list(data['utilities'])
        self.utilities = [
            [[int(value) for value in group] for group in row]
            for row in self.utilities
        ]
        #st.write(type(self.names[0][0]))
        self.transactions = []
        for names, utilities in zip(self.names, self.utilities):
            merged_row = []
            for name_group, utility_group in zip(names, utilities):
                merged_group = list(zip(name_group, utility_group))
                merged_row.append(merged_group)
            self.transactions.append(merged_row + [[]])
        self.transactions = [
            [[(int(x.strip()) if isinstance(x, str) else x, int(y.strip()) if isinstance(y, str) else y) for x, y in group] for group in row]
            for row in self.transactions ]

    def generate_sequences_with_weights(self, items, combined_dict):
        def backtrack(current_sequence, current_weight, index):
            # Kiểm tra độ dài của sequence hiện tại, nếu quá 4 thì dừng
            if len(current_sequence) > self.max_length:
                return

            # Tạo tuple của sequence để dùng làm key trong từ điển
            sequence_tuple = tuple(current_sequence)

            # Cập nhật trọng số và support trong từ điển kết hợp
            if sequence_tuple in combined_dict:
                combined_dict[sequence_tuple] = (combined_dict[sequence_tuple][0] + current_weight,
                                                 combined_dict[sequence_tuple][1])
            else:
                combined_dict[sequence_tuple] = (current_weight, 0)

            # Chỉ tăng mức độ support nếu đây là lần đầu tiên gặp sequence này trong transaction
            if sequence_tuple not in support_dict_in_transaction:
                combined_dict[sequence_tuple] = (combined_dict[sequence_tuple][0], combined_dict[sequence_tuple][1] + 1)
                support_dict_in_transaction.add(sequence_tuple)

            # Duyệt qua các phần tử từ vị trí hiện tại
            for i in range(index, len(items)):
                item = items[i]
                if isinstance(item, list):
                    # Nếu phần tử là một danh sách, thêm từng phần tử vào sequence
                    for elem, weight in item:
                        backtrack(current_sequence + [elem], current_weight + weight, i + 1)
                    # Thêm cả danh sách vào sequence nếu có nhiều hơn 1 phần tử
                    if len(item) > 1:
                        combined_elements = tuple(elem for elem, _ in item)
                        combined_weight = sum(weight for _, weight in item)
                        backtrack(current_sequence + [combined_elements], current_weight + combined_weight, i + 1)
                else:
                    # Nếu phần tử là một phần tử đơn lẻ, thêm nó vào sequence
                    elem, weight = item
                    backtrack(current_sequence + [elem], current_weight + weight, i + 1)

        # Bắt đầu backtracking từ sequence rỗng
        support_dict_in_transaction = set()
        backtrack([], 0, 0)

    def process_all_transactions(self, list_items):
        # Tạo từ điển kết hợp với giá trị là tuple (trọng số, số lần xuất hiện)
        combined_dict = defaultdict(lambda: (0, 0))

        for idx, items in enumerate(list_items):
            # Tạo tập hợp tạm thời để đảm bảo mỗi chuỗi chỉ được tính 1 lần cho mỗi transaction
            support_dict_in_transaction = set()
            self.generate_sequences_with_weights(items, combined_dict)
        return combined_dict

    def uspan(self, threshold):
        combined_dict = self.process_all_transactions(self.transactions)
        total_transactions = len(self.transactions)

        filtered_dict = {key: (value[0], (value[1] / total_transactions)) for key, value in
                         combined_dict.items() if value[0] >= threshold}
        result_set = [[key, value[1], value[0]] for key, value in filtered_dict.items()]
        print(result_set)
        return result_set

    def run(self, threshold):
        high_utility_sequence_sets = self.uspan(threshold)
        return rn.read_data2(high_utility_sequence_sets)