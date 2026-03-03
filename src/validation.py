import duckdb
from config import DB_PATH

con = duckdb.connect(str(DB_PATH))

print("\nDATA VALIDATION CHECKS\n")

null_occ = con.execute("""
    SELECT COUNT(*) FROM dim_occupation
    WHERE occupation_code IS NULL
""").fetchone()[0]

dup_skill = con.execute("""
    SELECT COUNT(*) FROM (
        SELECT occupation_code, skill_id, COUNT(*)
        FROM fact_skill_rating
        GROUP BY occupation_code, skill_id
        HAVING COUNT(*) > 1
    )
""").fetchone()[0]

orphan_skill = con.execute("""
    SELECT COUNT(*)
    FROM fact_skill_rating f
    LEFT JOIN dim_occupation d
        ON f.occupation_code = d.occupation_code
    WHERE d.occupation_code IS NULL
""").fetchone()[0]

invalid_scores = con.execute("""
    SELECT COUNT(*)
    FROM fact_skill_rating
    WHERE importance_score < 0 OR importance_score > 5
""").fetchone()[0]

print(f"Null occupation_code: {null_occ}")
print(f"Duplicate skill keys: {dup_skill}")
print(f"Orphan occupation references: {orphan_skill}")
print(f"Invalid importance scores: {invalid_scores}")

print("\nValidation completed.\n")