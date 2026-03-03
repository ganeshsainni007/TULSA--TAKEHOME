from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_PATH = BASE_DIR / "data" / "raw" / "onet"
WAREHOUSE_PATH = BASE_DIR / "data" / "warehouse"
DB_PATH = WAREHOUSE_PATH / "workforce.duckdb"

SCHEMA_PATH = BASE_DIR / "sql" / "schema.sql"