#  to calculate bmi of a person 
#   BMI = ( WEIGHT\HEIGHT^2)

height =float(input("enter your height in m : "))
weight = float(input("enter your weight in kg : "))
bmi=(float(weight)/(height)**2)
format_bmi="{:.2f}".format(bmi)
print(format_bmi)
