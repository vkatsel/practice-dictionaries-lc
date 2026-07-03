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

print(EMPLOYEE_DB["tech"]["alice"]["salary"])
tech_average=sum(employee["salary"] for employee in EMPLOYEE_DB["tech"].values())/len(EMPLOYEE_DB["tech"])
sales_average=sum(employee["salary"] for employee in EMPLOYEE_DB["sales"].values())/len(EMPLOYEE_DB["sales"])
hr_average=sum(employee["salary"] for employee in EMPLOYEE_DB["hr"].values())/len(EMPLOYEE_DB["hr"])
print(f"Tech average: {tech_average}. Sales average: {sales_average}. HR average: {hr_average}")