# ==========================================
# БАЗА ДАНИХ КОМПАНІЇ (СЛОВНИК)
# Використовується для Практичної №1
# ==========================================
import email

EMPLOYEE_DB = {
    "tech": {
        "alice": {"role": "Data Scientist", "salary": 4500, "status": "active"},
        "bob": {"role": "Backend Engineer", "salary": 3800, "status": "active"},
        "charlie": {"role": "DevOps", "salary": 4000, "status": "on_leave"}
    },
    "sales": {
        "diana": {"role": "Sales Manager", "salary": 3000, "status": "active"},
        "eve": {"role": "Account Executive", "salary": 3200, "status": "active"}
    },
    "hr": {
        "frank": {"role": "HR Specialist", "salary": 2500, "status": "active"}
    }
}

# Ваш код для завдань нижче:
# Live Coding 3: Міні-БД компанії

print(f"Alice salary: {EMPLOYEE_DB['tech']['alice']['salary']}")
# 1
EMPLOYEE_DB['sales']['diana']['salary']=3500
print(f"Diana new salary: {EMPLOYEE_DB['sales']['diana']['salary']}")
# 2
del EMPLOYEE_DB['tech']['charlie']
print(EMPLOYEE_DB['tech'])
# 3
sum=0
count=0
for department in EMPLOYEE_DB:
    for employee in EMPLOYEE_DB[department]:
        salary=int(EMPLOYEE_DB[department][employee]["salary"])
        sum+=salary
        count+=1
# for department, employee in EMPLOYEE_DB.items():
#   for name, data in employee.items():
#       sum += data['salary']
#       count+=1
avr=sum/count
print(f"Average salary: {avr:.2f}")



