"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

sales = float(input("Enter sales: $"))

# Not a good way to do it: vvv

# if sales < 1000:
#     print(int(10/100 * sales))
# elif sales > 1000:
#     print(int(15/100 * sales))
# elif sales == 1000:
#     print(int(15/100 * sales))

if sales < 1000:
    bonus = sales * 0.1
else:
    bonus = sales * 0.15
print("Bonus is $", bonus, sep=' ')

# Loop
sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales < 1000:
        bonus = sales * 0.1
    else:
        bonus = sales * 0.15
    print("Bonus is $", bonus, sep=' ')
    sales = float(input("Enter sales: $"))