# tip calculator

print("welcome to tip calculator")
bill =float(input("what is your total bill ?"))
tip =int(input("how much tip you want to give ? 10,12,15"))
people =int(input("how many people to split the bill?"))
bill_with_tip=(bill*tip)/100+bill
print(bill_with_tip)
