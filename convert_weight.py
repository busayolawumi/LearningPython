def convert_weight():
    weight = float(input("Enter the weight: "))
    unit = input("Enter the unit (K for kilograms, L for pounds): ")

    if unit.upper() == "K":
        pounds = weight * 2.20462
        print(f"The weight in pounds: {pounds:.2f}")
    elif unit.upper() == "L":
        kilograms = weight * 0.453592
        print(f"The weight in kilograms: {kilograms:.2f}")
    else:
        print("Invalid unit. Please specify K for kilograms or L for pounds.")

convert_weight()