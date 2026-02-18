print("Bill splitter calculator")
bill = int(input("Enter total bill amount: "))
ppl_num = int(input("Enter number of people to split the bill between: "))
tip_prec = int(input("Enter tip precentage: "))

Tip_Prec = ((tip_prec / 100) + 1)

print("Each person has to pay:")
print((Tip_Prec * bill) / ppl_num)