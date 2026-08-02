a=int(input("Amount: "))
b=int(input("Age: "))
if a>=25000 or b<=25:
    loan=int(input("Loan amount: "))
    if (loan>=50000):
        print("Maximum loan amount is 50000")
    else:
        print("You are eligible for loan")
else:
    print("Not eligible for loan")