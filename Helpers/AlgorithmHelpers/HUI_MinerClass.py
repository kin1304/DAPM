import Helpers.AlgorithmHelpers.read_dict as rd
import Helpers.AlgorithmHelpers.rename as rn


def find_subitem(itemset: list) -> list:
    subitems = [[[itemset[0]]]]
    for index in range(1, len(itemset)):
        subitem = subitems[index - 1].copy()
        subitem.append([itemset[index]])
        for item in subitems[index - 1]:
            if len(item) <= 3:
                i = item.copy()
                i.append(itemset[index])
                subitem.append(i)
        subitems.append(subitem)
    return subitems


def calculate_utilities(trans: dict, subitems) -> float:
    total_utilities = 0.0
    for item in subitems:
        total_utilities += trans[item]
    return total_utilities


def make_dict(names: list, util: list) -> dict:
    dictionary = {}
    for i in range(len(names)):
        dictionary[names[i]] = float(util[i])
    return dictionary


class HUI_Miner:
    def __init__(self, transactions, min_threshold):
        # transactions: dataframe các giao dịch(Transaction).
        # utilities: dictionary lưu utility của từng item.(ví dụ: {"A": 5, "B": 3})
        # threshold: ngưỡng tối thiểu để một itemset được coi là HUI.
        self.transactions = transactions
        self.min_threshold = min_threshold
        self.names, self.utilities = rd.read(transactions)
        self.first_version = self.filter_candidates(min_threshold)

    def find_candidate(self) -> dict:
        dict_candidates = {}
        for index in range(len(self.names)):
            trans = make_dict(list(self.names[index]), list(self.utilities[index]))
            all_subitems = find_subitem(list(self.names[index]))
            for subitems in all_subitems[-1]:
                subitems_sorted = sorted(subitems)
                string = ""
                for item in subitems_sorted:
                    string += str(item) + " "
                total_utilities = calculate_utilities(trans, subitems_sorted)
                dict_candidates[string] = dict_candidates.get(string, 0) + total_utilities
        return dict_candidates

    def filter_candidates(self, threshold) -> list:
        dict_candidates = self.find_candidate()
        candidates = []
        for idx, (key, value) in enumerate(dict_candidates.items()):
            if value == " ":
                pass
            elif float(value) >= threshold:
                candidates.append([key, value])
        return candidates

    def run(self, threshold) -> list:
        candidates = []
        for fv in self.first_version:
            if fv[1] >= threshold:
                data = rn.read_data(fv[0])
                candidates.append(data + [fv[1]])
        return candidates
