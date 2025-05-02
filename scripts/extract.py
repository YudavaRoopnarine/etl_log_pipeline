import os
import re
import pandas as pd
import json
import logging  # Logging will tell you which file is currently being processed and help you debug issues faster.


def read_logs():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
    extracted_data = []

    for filename in os.listdir("data/"):
        logging.info(f"Processing file: {filename}")
        filepath = os.path.join("data", filename)

        if filename.endswith((".log", ".txt")):
            with open(filepath, "r") as file:
                for line in file:
                    try:
                        parts = re.match(
                            r'(?P<ip>\S+) - - \[(?P<timestamp>[^\]]+)\] '
                            r'"(?P<method>\S+) (?P<path>\S+) (?P<version>[^"]+)" '
                            r'(?P<status>\d{3}) (?P<length>\d+)',
                            line.strip()  # <- This is the line you want to match!
                        )
                        if parts:
                            log_data = parts.groupdict()
                            extracted_data.append(log_data)
                        else:
                            logging.warning(f"No match for line: {line.strip()}")
                    except Exception as e:
                        logging.error(f"Error processing line: {line.strip()} - {e}")

        elif filename.endswith(".csv"):
            df = pd.read_csv(filepath)
            extracted_data.extend(df.to_dict(orient="records"))  # Convert to list of dicts

        elif filename.endswith(".json"):
            with open(filepath, "r") as file:
                json_data = json.load(file)
                if isinstance(json_data, list):  # If JSON is a list of records
                    extracted_data.extend(json_data)
                else:  # If JSON is a single dictionary
                    extracted_data.append(json_data)

    return extracted_data


if __name__ == "__main__":
    logs = read_logs()
    print("Processed logs:")
    print(logs)
