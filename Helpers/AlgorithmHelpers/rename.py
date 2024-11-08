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
    print(d['1'])
    return names
