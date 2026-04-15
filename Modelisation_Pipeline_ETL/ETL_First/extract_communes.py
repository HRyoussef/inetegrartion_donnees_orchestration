import pandas as pd

def extract_communes():
    df = pd.read_csv("dataset_final_kit2.csv")

    communes = df[["nom_commune", "cp_entreprise"]].drop_duplicates()

    communes = communes.rename(columns={
        "cp_entreprise": "code_postal"
    })

    communes = communes.reset_index(drop=True)
    communes["code_insee"] = communes.index + 38000

    return communes