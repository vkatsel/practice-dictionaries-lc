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

# Guided Practice: Профіль користувача
user_profile = {"username": "cinema_fan", "is_premium": True, "discount": 15}
user_profile["phone"]="+380991234567"
user_profile["is_premium"]=False
user_profile.pop("discount")
print(user_profile)

# Guided Practice: Аналіз оцінок
grades = {"Alice": 95, "Bob": 80, "Charlie": 75, "Diana": 90}
mas=list(grades.values())
sum=0
for i in mas:
    sum+=i
avg=sum/len(mas)
print(f"{avg:.2f}")
phone = "991234567"
print(f"+38{phone:010s}")