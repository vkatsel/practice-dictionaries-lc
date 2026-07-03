menu = {"Latte": 60, "Americano": 40}
print(f"Americano: {menu["Americano"]}")
menu["Latte"]=70
menu["Flat White"]=65
print(f"Updated menu: {menu}")
print(f"Cappuccino: {menu.get("Cappuccino","Undefined")}")