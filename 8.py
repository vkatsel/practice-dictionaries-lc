grades = {"Alice": 95, "Bob": 80, "Charlie": 75, "Diana": 90}
total=0
for key,value in grades.items():
    total+=value
mean=total/len(grades)
print(mean)