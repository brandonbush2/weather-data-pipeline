import psycopg2
import os
from dotenv import load_dotenv
from api_request import fetch_data

load_dotenv() #calling .env variables

def connect_to_db():
    print("Connecting to the Postgresql database...")
    try:
        conn = psycopg2.connect(
            host = "localhost",
            port = 5000,
            dbname = os.getenv("POSTGRES_DB"),
            user = os.getenv("POSTGRES_USER"),
            password = os.getenv("POSTGRES_PASSWORD")
        )
        return conn
    except psycopg2.Error as e:
        print(f"Database connection failed {e}")
        raise

connect_to_db()