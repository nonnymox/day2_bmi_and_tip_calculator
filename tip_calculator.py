# print("Welcome to the tip calculator")
# bill = float(input("What was the total bill? "))
# tip_percent= int(input("How much tip  would you like to give? 10, 12, or 15 ")) / 100
# split = int(input("How many people should split the bill? "))


# tip = tip_percent * bill
# total_bill = bill + tip
# bill_per_person = total_bill/split
# print(f"Each person should pay {bill_per_person}")


# Checking for wrong input and eliminating errors
print("Welcome to the tip calculator")

try: # Runs the code only if the bill is a number
    bill = float(input("What was the total bill? "))
    tip_percent = int(input("How much tip would you like to give? 10, 12, or 15? ")) / 100
    
    while tip_percent not in [0.1, 0.12, 0.15]:  # Ensures valid tip input of 10  12 or 15
        print("Please enter 10, 12, or 15.")
        tip_percent = int(input("How much tip would you like to give? 10, 12, or 15? ")) / 100

    split = int(input("How many people should split the bill? "))
    
    tip = tip_percent * bill
    total_bill = bill + tip
    bill_per_person = total_bill / split
    
    print(f"Each person should pay: ${bill_per_person:.2f}") # Approximates the bill to 2 decimal
    
except ValueError:
    print("Please enter a valid number.")
