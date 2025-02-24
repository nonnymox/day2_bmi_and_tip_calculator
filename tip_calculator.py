print("Welcome to the tip calculator")
bill = float(input("What was the total bill? "))
tip_percent= int(input("How much tip  would you like to give? 10, 12, or 15 ")) / 100
split = int(input("How many people should split the bill? "))


tip = tip_percent * bill
total_bill = bill + tip
bill_per_person = total_bill/split
print(f"Each person should pay {bill_per_person}")


