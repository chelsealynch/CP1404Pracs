number_of_items = input("Number of items: ")
item_price_1 = input("Price of item: ")
item_price_2 = input("Price of item: ")
item_price_3 = input("Price of item: ")
total = int(item_price_1 + item_price_2 + item_price_3)

print("Total price for " + int(number_of_items) + " items is $" + int(total))

# total = 0
# number = int(input("Number of items: "))
# while number < 0:
#     print("Invalid number of items!")
#     number = int(input("Number of items: "))
# for i in range(number):
#     price = float(input("Price of item: "))
#     total += price
#
# if total > 100:
#     total *= 0.9
#
# print("Total price for {} items is ${:.2f}".format(number, total))