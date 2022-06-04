# tip calculator for restro 

print("welcome to the tip calculator ")
bill = float(input("what is your total bill ?"))
tip = int(input("what per tip would uou like to give ? 10,12,15 "))
person = int(input("how many person to split the bill?"))

bill_with_tip = (bill*tip)/100+bill   #total bill
bill_per_person = bill_with_tip/person
print(bill_per_person)