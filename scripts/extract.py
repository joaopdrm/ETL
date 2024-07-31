import pandas as pd

def extract_data():
    # Simula a extração dos dados

    data = {
        "name": ["John", "Jane", "Doe"],
        "age": [30, 25, 35],
        "city": ["New York", "Los Angeles", "Chicago"]     
    }

    df = pd.DataFrame(data)
    df.to_csv("../data/raw/data.csv",index=False)
    return df