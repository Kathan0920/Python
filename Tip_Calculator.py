#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60


print("Welcome to the Tip calculator.")
total_bill = input("What was the total bill (Rs) ")
tip_percentage = input("What percentage tip would you like to give? 10, 12, or 15? ")
total_person = input("Among how many persons you want to share bill? ")

tip = float(total_bill) * (float(tip_percentage) / 100)
bill_with_tip = float(total_bill) + float(tip)
each_to_pay = bill_with_tip / float(total_person)

print(f"Each person shoud pay {round(each_to_pay,2)}")
