user_profile = {"username": "cinema_fan", "is_premium": True, "discount": 15}
user_profile["phone"]= +380991234567
user_profile["is_premium"]=False
user_profile.pop("discount")
print(f"Updated user_profile: {user_profile}")
