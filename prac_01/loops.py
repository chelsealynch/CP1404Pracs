for i in range(1, 21, 2):
    print(i, end=' ')
print()

for i in range(0, 100, 10):
    print(i, end=' ')
print()

for i in range(1, 20, -1):
    print(i, end=' ')
print()

make_stars = input("Enter a number: ")
if make_stars != 0:
    print('*' * int(make_stars))

make_more_stars = int(input("Enter a number: "))
for i in range(make_more_stars):
    print('*', end=' ')
print()

for i in range(make_more_stars):
    print('*' * (i + 1), end=' ')
    print()

# unfinished