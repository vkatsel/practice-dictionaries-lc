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

total_salary = 0
amount_p = 0
for dep_name, people in EMPLOYEE_DB.items():
    for name, data in people.items():
        total_salary += data["salary"]
        amount_p += 1

print(f"average salary: {total_salary/amount_p}")

# print(EMPLOYEE_DB["tech"]["alice"]["salary"])
# Ваш код для завдань нижче:

# user_profile = {"username": "cinema_fan", "is_premium": True, "discount": 15}
#
# user_profile["phone"] = "+380991234567"
# user_profile["is_premium"] = False
# user_profile.pop("discount")
# print(user_profile)
#
#
# print(user_profile.values())

# grades = {"Alice": 95, "Bob": 80, "Charlie": 75, "Diana": 90}
# new_grades = list(grades.values())
# average = sum(new_grades) / len(new_grades)
# print(average)
#
# phone = "991234567"
# print(f"+38{phone:10s}")






