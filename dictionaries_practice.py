# ==========================================
# БАЗА ДАНИХ КОМПАНІЇ (СЛОВНИК)
# Використовується для Практичної №1
# ==========================================

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
print(f"Alice salary: {EMPLOYEE_DB['tech']['alice']['salary']}")

EMPLOYEE_DB['sales']['diana']['salary']=3500
del EMPLOYEE_DB['tech']['charlie']
print(EMPLOYEE_DB)


total_salary=0
number=0
for i in EMPLOYEE_DB:
    for j in EMPLOYEE_DB[i]:
        total_salary+=(EMPLOYEE_DB[i][j]["salary"])
        number+=1
print(f"Average salary: {total_salary/number:.2f}")


total=0
amount=0
for dep_name,people in EMPLOYEE_DB.items():
    for name, person_data in people.items():
        total+=person_data["salary"]
        amount+=1
print(f"Average salary: {total/amount:.2f}")




user_profile = {"username": "cinema_fan", "is_premium": True, "discount": 15}
user_profile["phone"]="+380991234567"
user_profile["is_premium"]=False
user_profile.pop("discount")
print(user_profile)



grades = {"Alice": 95, "Bob": 80, "Charlie": 75, "Diana": 90}
value_grades=grades.values()
average=sum(value_grades)/len(value_grades)
print(f"Average: {average:.2f}")