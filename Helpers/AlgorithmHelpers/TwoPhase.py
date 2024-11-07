import numpy as np
import streamlit as st
import itertools
from collections import defaultdict

import Helpers.AlgorithmHelpers.read_dict as rd

class TwoPhase:
    def __init__(self, data:dict, threshold=30):
        self.threshold = threshold
        self.data = data
        self.names, self.utilities = rd.read(self.data)
        self.sum_utilities = np.array([np.sum(transaction_utilities) for transaction_utilities in self.utilities])
        self.transactions = []
        for na, sum_util, util in zip(self.names, self.sum_utilities, self.utilities):
            self.transactions.append((na, sum_util, util))

    # Tính toán TWU (Trọng số Tiện ích Giao Dịch)
    def calculate_twu(self, transactions):
        item_twu = defaultdict(int)
        for items, total_utility, _ in transactions:
            for item in items:
                item_twu[item] += total_utility
        return item_twu

    # Tạo các tập ứng viên từ các tập có kích thước nhỏ hơn
    def generate_candidates(self, itemsets, length):
        return list(itertools.combinations(itemsets, length))

    # Tính toán tiện ích cho các tập con có kích thước lớn hơn 1
    def calculate_utility(self, itemset, transactions):
        utility = 0
        support_count = 0
        for items, _, utilities in transactions:
            if set(itemset).issubset(set(items)):
                support_count += 1
                for item in itemset:
                    item_index = np.where(items == item)[0]
                    if len(item_index) > 0:  # Nếu tìm thấy chỉ số
                        utility += utilities[item_index[0]]
        support = support_count / len(self.transactions)
        return support, utility

    # Lọc các ứng viên có tiện ích >= minUtility
    def filter_candidates(self, candidates, min_utility, transactions):
        high_utility_itemsets = []
        for itemset in candidates:
            support, utility = self.calculate_utility(itemset, transactions)
            if utility >= min_utility:
                high_utility_itemsets.append((itemset, support, utility))
        return high_utility_itemsets

    # Chạy thuật toán Two-Phase
    def run(self):
        # Tính TWU cho mỗi item và lọc các item ban đầu
        item_twu = self.calculate_twu(self.transactions)
        initial_candidates = [item for item in item_twu if item_twu[item] >= self.threshold]

        high_utility_itemsets = []

        # Bắt đầu với các tập ứng viên có kích thước là 1
        k = 1
        current_candidates = [(item,) for item in initial_candidates]

        # Tạo các tập ứng viên có kích thước lớn dần
        while current_candidates:
            high_utility_itemsets.extend(self.filter_candidates(current_candidates, self.threshold, self.transactions))
            k += 1
            if k <= 4:
                current_candidates = self.generate_candidates(initial_candidates, k)

        return high_utility_itemsets

