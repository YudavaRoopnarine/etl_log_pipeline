import pandas as pd
from datetime import datetime
import re


def parsing_timestamps(timestamp_string, format_string):
    try:
        return datetime.strptime(timestamp_string, format_string)
    except ValueError:
        return None


def clean_text(text):
    try:
        df = pd.DataFrame(text)  # Works if text is a list of dictionaries
    except ValueError:
        print("Invalid data format!")


    # Standardize column names for CSVs
    if 'first_name' in df.columns and 'last_name' in df.columns:
        df['name'] = df['first_name'].str.strip() + " " + df['last_name'].str.strip()
    elif 'name' in df.columns:
        df['name'] = df['name'].str.strip()

    # Clean name to lowercase
    if 'name' in df.columns:
        df['name'] = df['name'].str.lower()

    # Clean phone numbers
    if 'phone' in df.columns:
        df['phone'] = df['phone'].str.replace(r'\D', '', regex=True)

    # Simplify email to domain only
    if 'email' in df.columns:
        df['email_domain'] = df['email'].apply(lambda x: x.split('@')[1] if isinstance(x, str) and '@' in x else None)

    # Clean IP address
    if 'ip_address' in df.columns:
        df['ip_address'] = df['ip_address'].str.strip()

    # Drop first_name and last_name if merged
    df = df.drop(columns=[col for col in ['first_name', 'last_name'] if col in df.columns])

    return df.to_dict(orient="records")
