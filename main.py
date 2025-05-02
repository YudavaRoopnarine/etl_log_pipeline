from scripts.extract import read_logs
from scripts.transform import clean_text
from scripts.load import insert_logs
from config.db_config import DB_HOST, DB_NAME, DB_USER, DB_PASSWORD, DB_PORT


def run_etl_pipeline():
    # Step 1: Extract data from raw log files
    raw_logs = read_logs()

    # Step 2: Transform the extracted logs (cleaning & processing)
    transformed_logs = clean_text(raw_logs)

    # Step 3: Load the transformed logs into PostgreSQL
    insert_logs(transformed_logs)


if __name__ == "__main__":
    run_etl_pipeline()

