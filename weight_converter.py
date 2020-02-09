#Program for converting weight in kgs to lbs or viceversa

weight= input("Enter weight :")
unit = input ("Pounds(lbs) or Kilograms(kg)")
if unit == "lbs":
   new_weight = float(weight)*0.45
   print(f'You are {new_weight} kgs')
else:
   new_weight = float(weight)/0.45
   print(f'You are {new_weight} lbs')
