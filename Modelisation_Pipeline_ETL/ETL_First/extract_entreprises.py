import pandas as pd

def extract_entreprises():
    df = pd.read_csv("dataset_final_kit2.csv")

    entreprises = df[[
        "siren",
        "nom",
        "adresse",
        "tranche_effectif",
        "nom_commune",
        "code_naf"
    ]].drop_duplicates(subset=["siren"])

    # génération simple code_insee (matching simplifié)
    communes = df[["nom_commune"]].drop_duplicates().reset_index(drop=True)
    communes["code_insee"] = communes.index + 38000

    entreprises = entreprises.merge(communes, on="nom_commune", how="left")

    return entreprises