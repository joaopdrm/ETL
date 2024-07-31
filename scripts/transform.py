import pandas as pd

def transform_data():
    df = pd.read_csv("../data/raw/data.csv")
    df['age'] = df['age'] + 1  # Exemplo de transformação
    df.to_csv("../data/processed/transformed_data.csv", index=False)
    return df