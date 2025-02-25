def calculate_bmi(height, weight):
    bmi = weight/height**2
    if  bmi < 18.5:
        print("Underweight")
    elif bmi < 25:
        print("Normal weight")
    else:
        print("Overweight")

    return bmi

print(calculate_bmi(1.65,84))