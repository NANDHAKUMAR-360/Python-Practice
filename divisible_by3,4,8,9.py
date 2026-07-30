a = int(input("Enter a number: "))
if a % 3 == 0:
    print("Divisible by 3")
elif a % 4 == 0:
    print("Divisible by 4")
elif a % 8 == 0:
    print("Divisible by 8")
elif a % 9 == 0:
    print("Divisible by 9")
else:
    print("Not divisible by 3, 4, 8, or 9")