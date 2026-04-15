import pandas as pd

def extract_secteurs():
    df = pd.read_csv("dataset_final_kit2.csv")

    secteurs = df[["code_naf", "libelle_naf"]].drop_duplicates()

    return secteurs