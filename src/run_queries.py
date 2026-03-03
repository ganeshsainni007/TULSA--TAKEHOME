import duckdb
from config import DB_PATH
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
QUERY_PATH = BASE_DIR / "sql" / "queries.sql"

con = duckdb.connect(str(DB_PATH))

with open(QUERY_PATH, "r") as f:
    queries = f.read().strip().split(";")

for query in queries:
    query = query.strip()
    if query:
        print("QUERY RESULT")
        print(con.execute(query).fetchdf())