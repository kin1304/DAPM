class HUI_Miner:
    def __init__(self, transactions, threshold):
        # transactions: dataframe các giao dịch(Transaction).
        # utilities: dictionary lưu utility của từng item.(ví dụ: {"A": 5, "B": 3})
        # threshold: ngưỡng tối thiểu để một itemset được coi là HUI.
        self.transactions = transactions
        self.threshold = threshold

    def candidate(self) -> list:
        initial_candidate = [trans for trans in self.transactions if trans.total_utilities >= self.threshold]
        return initial_candidate



