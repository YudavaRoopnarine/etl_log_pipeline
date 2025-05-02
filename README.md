etl_log_pipeline/
│── data/                # Directory for storing raw and processed logs
    ├── webserver_logs.txt     # Raw web server logs
    ├── application_logs.csv   # Logs from an application
    ├── error_logs.json        # JSON-formatted error logs
│── logs/                # Directory for storing pipeline execution logs
    ├──    # Log file for ETL execution
│── scripts/             # Contains ETL scripts
│   │── extract.py       # Extracts raw log data
│   │── transform.py     # Cleans & processes data
│   │── load.py          # Loads transformed data into PostgreSQL
│── config/              
│   │── db_config.py     # Database connection settings
│   │── pipeline_config.py  # Configuration settings for the pipeline
│── main.py              # Entry point to run the ETL pipeline
│── requirements.txt     # Dependencies (libraries required)
│── README.md            # Project documentation
│── .env                 # Stores environment variables (e.g., DB credentials)
│── Dockerfile (optional)  # For containerization
│── airflow/ (optional)  # If using Apache Airflow for automation

what is venv activate doing ?
Isolates Dependencies
Instead of installing packages globally, Python uses the venv folder for package management.
Prevents conflicts between different projects using different package versions.

Modifies Environment Variables
It updates the PATH variable so that Python and pip run from the virtual environment instead of the system-wide installation.


cd C:\Users\yudav\PycharmProjects\etl_log_pipeline

venv\Scripts\activate

 install the necessary Python packages:
 pip install psycopg2 pandas python-dotenv logging

After installation, check if the libraries are installed:
pip freeze > requirements.txt

