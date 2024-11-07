import numpy as np

def read(data: dict):
    # Tạo mảng răng cưa với các số nguyên cho names và số thực cho utilities
    all_names = [np.array(transaction["names"], dtype=int) for transaction in data.values()]
    all_utilities = [np.array(transaction["utilities"], dtype=float) for transaction in data.values()]

    # Chuyển đổi thành các mảng răng cưa (số transaction x số name trong mỗi transaction)
    names_array = np.array(all_names, dtype=object)
    utilities_array = np.array(all_utilities, dtype=object)

    return names_array, utilities_array