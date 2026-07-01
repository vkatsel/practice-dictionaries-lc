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
EMPLOYEE_DB["sales"]["diana"]["salary"] = 3500
del EMPLOYEE_DB["tech"]["charlie"]
print(EMPLOYEE_DB)



# user_profile = {"username": "cinema_fan",
#                 "is_premium": True,
#                 "discount": 15
# }
# user_profile["phone"] = "+380991234567"
# user_profile["is_premium"] = False
# user_profile.pop("discount")
# user_profile.pop("is_premium")
# print(user_profile)


# grades = {"Alice": 95, "Bob": 80, "Charlie": 75, "Diana": 90}
# pure_grades = list(grades.values())
# avarage = sum(pure_grades)/len(pure_grades)
# print(f"Average grade: {avarage:.2f}")
# a = 1
# print(f"{a:06d}")



