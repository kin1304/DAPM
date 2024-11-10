import pandas as pd


def read_data(subitems: str) -> list:
    df = pd.read_csv("dict.csv")
    d = df.to_dict()
    array = subitems.split(" ")
    names = []
    for a in array:
        if a == "":
            pass
        else:
            names.append(d[a][0])
    return names

def read_data2(itemsets):
    df = pd.read_csv("dict.csv")
    name_mapping = df.iloc[0].to_dict()

    converted_output_list = [
        [[name_mapping.get(str(element), str(element)) if isinstance(element, int) else tuple(
            name_mapping.get(str(sub_element), str(sub_element)) for sub_element in element) for element in key],
         support, utility]
        for key, support, utility in itemsets
    ]
    return converted_output_list