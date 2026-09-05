import os
import csv
import psycopg2
from psycopg2 import sql
from dotenv import load_dotenv
load_dotenv()

if 'port' not in os.environ:
    os.environ['port'] = '5432'

# ============================================================
# CONFIGURATION
# ============================================================

DB_CONFIG = {
    "host": os.environ['host'],
    "port": int(os.environ['port']),
    "database": os.environ['database'],
    "user": os.environ['user'],
    "password": os.environ['password'],
}

CSV_DIR = "data"


# ============================================================
# DATABASE CONNECTION
# ============================================================

conn = psycopg2.connect(**DB_CONFIG)
conn.autocommit = False

cursor = conn.cursor()

print("Connected to PostgreSQL")