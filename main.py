print("Welcome to the Tip Calculator!!")
total = float(input("What was the total bill? $ "))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

total_bill = total + (total * tip / 100)
split = round(total_bill / people, 2)

print(f"Each person should pay : {split}$ !")
