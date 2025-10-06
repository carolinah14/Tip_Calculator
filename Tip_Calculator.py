print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $"))
tip_amount = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
tip_amount /= 100
number_of_people = int(input("How many people to split the bill? "))
payment_per_person = (total_bill * tip_amount + total_bill) / number_of_people
print(f"Each person should pay: ${payment_per_person: .2f}")
input("\nPress ENTER to exit the program")

