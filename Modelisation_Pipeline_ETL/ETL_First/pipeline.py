import logging

from extract_communes import extract_communes
from extract_secteurs import extract_secteurs
from extract_entreprises import extract_entreprises
from load_sqlite import load_data


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("pipeline.log"),
        logging.StreamHandler()
    ]
)

def main():
    logging.info("🚀 PIPELINE START")

    try:
        logging.info(" Extraction communes")
        communes = extract_communes()

        logging.info(" Extraction secteurs")
        secteurs = extract_secteurs()

        logging.info(" Extraction entreprises")
        entreprises = extract_entreprises()

        logging.info(" Loading SQLite")
        load_data(communes, secteurs, entreprises)

        logging.info(" PIPELINE SUCCESS")

    except Exception as e:
        logging.error(f" ERROR: {e}")


if __name__ == "__main__":
    main()