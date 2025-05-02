import psycopg2
from psycopg2 import sql
from datetime import datetime


def insert_logs(logs):
    try:
        connection = psycopg2.connect(
            dbname="log_processing",
            user="postgres",
            password="Smackthat25!",
            host="localhost",
            port="5432"
        )
        cursor = connection.cursor()
        print("Connection successful!")

        print(f"Number of log entries received: {len(logs)}")

        for entry in logs:
            timestamp_raw = entry.get("timestamp")
            log_level = entry.get("log_level")
            message = entry.get("message")

            try:
                # Ensure timestamp is valid and converted to datetime
                if not timestamp_raw or str(timestamp_raw).lower() == "nan":
                    print("Skipping entry due to invalid timestamp:", entry)
                    continue

                # If already a datetime object, use it; otherwise, parse it
                if isinstance(timestamp_raw, datetime):
                    timestamp = timestamp_raw
                else:
                    timestamp = datetime.fromisoformat(str(timestamp_raw))

                sql = "INSERT INTO logs (timestamp, log_level, message) VALUES (%s, %s, %s)"
                val = (timestamp, log_level, message)
                cursor.execute(sql, val)

            except Exception as inner_e:
                print("Skipping bad log entry:", entry)
                print("Reason:", inner_e)
                continue

            # Show each log being inserted
            print(f"Inserting: {timestamp} | {log_level} | {message}")

        # Commit after all insertions
        connection.commit()
        print("Logs inserted successfully!")


    except Exception as e:
        import traceback
        print("Error inserting logs!")
        print("Details:", e)
        traceback.print_exc()


    finally:
        cursor.close()
        connection.close()
        print("Connection closed.")
