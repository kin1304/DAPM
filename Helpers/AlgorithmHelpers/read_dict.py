import numpy as np

def read(data:dict):
    all_names = [transaction["names"] for transaction in data.values()]
    all_utilities = [transaction["utilities"] for transaction in data.values()]

    # Chuyển đổi thành các mảng đa chiều (số transaction x số name trong mỗi transaction)
    names_array = np.array(all_names, dtype=object)
    utilities_array = np.array(all_utilities, dtype=object)

    return names_array, utilities_array