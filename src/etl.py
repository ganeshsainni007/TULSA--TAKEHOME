import duckdb
import pandas as pd
from config import DATA_PATH, DB_PATH, SCHEMA_PATH, WAREHOUSE_PATH

WAREHOUSE_PATH.mkdir(parents=True, exist_ok=True)

con = duckdb.connect(str(DB_PATH))

with open(SCHEMA_PATH, "r") as f:
    con.execute(f.read())

occupation_df = pd.read_csv(DATA_PATH / "Occupation Data.txt", sep="\t")

occupation_df = occupation_df.rename(columns={
    "O*NET-SOC Code": "occupation_code",
    "Title": "title",
    "Description": "description"
})

con.execute("DELETE FROM dim_occupation")
con.register("occupation_df", occupation_df)
con.execute("INSERT INTO dim_occupation SELECT * FROM occupation_df")

skills_df = pd.read_csv(DATA_PATH / "Skills.txt", sep="\t")

skills_df = skills_df.rename(columns={
    "O*NET-SOC Code": "occupation_code",
    "Element ID": "skill_id",
    "Element Name": "skill_name",
    "Scale ID": "scale_id",
    "Data Value": "data_value"
})

dim_skill_df = skills_df[["skill_id", "skill_name"]].drop_duplicates()

con.execute("DELETE FROM dim_skill")
con.register("dim_skill_df", dim_skill_df)
con.execute("INSERT INTO dim_skill SELECT * FROM dim_skill_df")

skills_pivot = skills_df.pivot_table(
    index=["occupation_code", "skill_id"],
    columns="scale_id",
    values="data_value"
).reset_index()

skills_pivot = skills_pivot.rename(columns={
    "IM": "importance_score",
    "LV": "level_score"
})

con.execute("DELETE FROM fact_skill_rating")
con.register("skills_pivot", skills_pivot)
con.execute("""
    INSERT INTO fact_skill_rating
    SELECT occupation_code, skill_id, importance_score, level_score
    FROM skills_pivot
""")

knowledge_df = pd.read_csv(DATA_PATH / "Knowledge.txt", sep="\t")

knowledge_df = knowledge_df.rename(columns={
    "O*NET-SOC Code": "occupation_code",
    "Element ID": "knowledge_id",
    "Element Name": "knowledge_name",
    "Scale ID": "scale_id",
    "Data Value": "data_value"
})

dim_knowledge_df = knowledge_df[["knowledge_id", "knowledge_name"]].drop_duplicates()

con.execute("DELETE FROM dim_knowledge")
con.register("dim_knowledge_df", dim_knowledge_df)
con.execute("INSERT INTO dim_knowledge SELECT * FROM dim_knowledge_df")

knowledge_pivot = knowledge_df.pivot_table(
    index=["occupation_code", "knowledge_id"],
    columns="scale_id",
    values="data_value"
).reset_index()

knowledge_pivot = knowledge_pivot.rename(columns={
    "IM": "importance_score",
    "LV": "level_score"
})

con.execute("DELETE FROM fact_knowledge_rating")
con.register("knowledge_pivot", knowledge_pivot)
con.execute("""
    INSERT INTO fact_knowledge_rating
    SELECT occupation_code, knowledge_id, importance_score, level_score
    FROM knowledge_pivot
""")

print("ETL completed successfully.")