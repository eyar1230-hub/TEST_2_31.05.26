from db import run_update_query, run_query_select

#1. answer
answer = run_query_select("""
SELECT * 
FROM world_cups
WHERE winner like 'Brazil'

""")
for i in answer:
    print(i)
print('')
print('-' * 240)
print('')
# 2.answer1
run_update_query("UPDATE world_cups SET host_country = ? where year = ?", ('East Asia', 2002))
result1 = run_query_select("SELECT * FROM world_cups WHERE year = 2002")
for row in result1:
    print(row)

