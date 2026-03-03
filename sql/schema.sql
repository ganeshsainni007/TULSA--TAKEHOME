CREATE TABLE IF NOT EXISTS dim_occupation (
    occupation_code TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT
);

CREATE TABLE IF NOT EXISTS dim_skill (
    skill_id TEXT PRIMARY KEY,
    skill_name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS dim_knowledge (
    knowledge_id TEXT PRIMARY KEY,
    knowledge_name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS fact_skill_rating (
    occupation_code TEXT NOT NULL,
    skill_id TEXT NOT NULL,
    importance_score FLOAT,
    level_score FLOAT,
    PRIMARY KEY (occupation_code, skill_id),
    FOREIGN KEY (occupation_code) REFERENCES dim_occupation(occupation_code),
    FOREIGN KEY (skill_id) REFERENCES dim_skill(skill_id)
);

CREATE TABLE IF NOT EXISTS fact_knowledge_rating (
    occupation_code TEXT NOT NULL,
    knowledge_id TEXT NOT NULL,
    importance_score FLOAT,
    level_score FLOAT,
    PRIMARY KEY (occupation_code, knowledge_id),
    FOREIGN KEY (occupation_code) REFERENCES dim_occupation(occupation_code),
    FOREIGN KEY (knowledge_id) REFERENCES dim_knowledge(knowledge_id)
);