SELECT
    o.title,
    AVG(f.importance_score) AS avg_importance
FROM fact_skill_rating f
JOIN dim_occupation o
    ON f.occupation_code = o.occupation_code
GROUP BY o.title
ORDER BY avg_importance DESC
LIMIT 10;


SELECT
    s.skill_name,
    AVG(f.importance_score) AS avg_importance
FROM fact_skill_rating f
JOIN dim_skill s
    ON f.skill_id = s.skill_id
GROUP BY s.skill_name
ORDER BY avg_importance DESC
LIMIT 10;


SELECT
    o.title,
    AVG(f.level_score) AS avg_knowledge_level
FROM fact_knowledge_rating f
JOIN dim_occupation o
    ON f.occupation_code = o.occupation_code
GROUP BY o.title
ORDER BY avg_knowledge_level DESC
LIMIT 10;