gross_salaries = [15000, 22000, 18500, 31000]
net_salaries =[salary - (salary*0.2) for salary in gross_salaries]
print(net_salaries)