import duckdb
import glob
import os
from itertools import combinations

conn=duckdb.connect()
csv_files = glob.glob("Data/*.csv")
all_profiles = {}
for file_path in csv_files:
    file_name=os.path.basename(file_path)
    customer_schema=conn.execute(f"DESCRIBE SELECT * FROM '{file_path}' ").fetchdf()
    column_name=customer_schema["column_name"].to_list()
    profile_lines=[]
    for col in column_name:
        total,non_null,distinct=conn.execute(f"""SELECT COUNT(*), count("{col}"),count(DISTINCT "{col}") from '{file_path}'""").fetchone()
        profile_lines.append(f"{col}:{total} rows,{distinct} distinct,{total-non_null} nulls")


    profile_text= " ".join(profile_lines)
    all_profiles[file_name] = profile_text
    # print(file_name, "->", profile_text)
    # print(list(all_profiles.keys()))

def overlap_ratio(path_a, col_a, path_b, col_b):
    result = conn.execute(f"""
        WITH a AS (SELECT DISTINCT CAST("{col_a}" AS VARCHAR) AS val FROM '{path_a}' WHERE "{col_a}" IS NOT NULL),
             b AS (SELECT DISTINCT CAST("{col_b}" AS VARCHAR) AS val FROM '{path_b}' WHERE "{col_b}" IS NOT NULL)
        SELECT COUNT(*) FILTER (WHERE b.val IS NOT NULL) AS matched,
               (SELECT COUNT(*) FROM a) AS total_a
        FROM a LEFT JOIN b ON a.val = b.val
    """).fetchone()
    matched, total_a = result
    return matched / total_a if total_a else 0





table_columns = {}
for file_path in csv_files:
    cols = conn.execute(f"DESCRIBE SELECT * FROM '{file_path}'").fetchdf()["column_name"].tolist()
    table_columns[file_path] = cols

candidates = []
for path_a, path_b in combinations(csv_files, 2):
    for col_a in table_columns[path_a]:
        for col_b in table_columns[path_b]:
            ratio = overlap_ratio(path_a, col_a, path_b, col_b)
            if ratio > 0.8:
                candidates.append((
                    os.path.basename(path_a), col_a,
                    os.path.basename(path_b), col_b,
                    round(ratio, 3)
                ))

for c in candidates:
    print(c)