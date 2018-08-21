try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

# 1) A ValueError will occur when the numerator and/or denominator are invalid.
# 2) A ZeroDivisionError will occur when then denominator is 0.
# 3) No because it is impossible to divide by zero.