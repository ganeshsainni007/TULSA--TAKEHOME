import duckdb
from config import DB_PATH

con = duckdb.connect(str(DB_PATH))

tables = [
    "dim_occupation",
    "dim_skill",
    "dim_knowledge",
    "fact_skill_rating",
    "fact_knowledge_rating"
]

for table in tables:
    count = con.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0]
    print(f"{table}: {count} rows")

print("\nSample data from fact_skill_rating:")
print(con.execute("SELECT * FROM fact_skill_rating LIMIT 5").fetchdf())