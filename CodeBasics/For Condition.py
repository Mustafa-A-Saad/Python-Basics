month_list = ["January", "February", "March", "April", "May"]
expense_list = [2340, 2500, 2100, 3100, 2980]
answer = float(input("Enter expense amount: "))

month = -1
for i in range(len(expense_list)):
    if answer == expense_list[i]:
        month = i
        break

if month != -1:
    print(f'You have spent {answer} in {month_list[month]}!')
else:
    print("The number u entered wasn't spent anywhere ")


#-------Star Porject--------#

#for i in range(1,6):
#    print("*"*i)

for i in range(6):
    s = ""
    for j in range(i):
        s ="*"*i
    print(s)

# Another Way
"""
num = int(input("enter a input"))
for i in range(num):
    s=""
    for j in range(i+1):
        s+="*"
    print(s)
"""
