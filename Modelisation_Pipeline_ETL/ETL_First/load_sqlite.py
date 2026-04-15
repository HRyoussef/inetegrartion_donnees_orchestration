import sqlite3
def load_data(communes, secteurs, entreprises):
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()

    # RESET PROPRE
    cur.execute("DROP TABLE IF EXISTS communes")
    cur.execute("DROP TABLE IF EXISTS secteurs")
    cur.execute("DROP TABLE IF EXISTS entreprises")

    # CREATE TABLES
    cur.execute("""
    CREATE TABLE communes (
        code_insee INTEGER PRIMARY KEY,
        nom_commune TEXT,
        code_postal TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE secteurs (
        code_naf TEXT PRIMARY KEY,
        libelle_naf TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE entreprises (
        siren TEXT PRIMARY KEY,
        nom TEXT,
        adresse TEXT,
        tranche_effectif TEXT,
        nom_commune TEXT,
        code_insee INTEGER,
        code_naf TEXT
    )
    """)

    # ALIGN DATAFRAMES
    communes = communes[["code_insee", "nom_commune", "code_postal"]]
    secteurs = secteurs[["code_naf", "libelle_naf"]]
    entreprises = entreprises[[
        "siren", "nom", "adresse",
        "tranche_effectif", "nom_commune",
        "code_insee", "code_naf"
    ]]

    # INSERT
    communes.to_sql("communes", conn, if_exists="append", index=False)
    secteurs.to_sql("secteurs", conn, if_exists="append", index=False)
    entreprises.to_sql("entreprises", conn, if_exists="append", index=False)

    conn.commit()
    conn.close()