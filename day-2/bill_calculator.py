print("Welcome to the tip calculator\n");
total_bill = input("What was the total bill? $\n");
tip = input("How much tip would you like to give? 10, 12 or 15? \n");
people = input("How many people to split the bill? \n");
value = (float(total_bill) + int(tip)) / int(people);
print(f"each person should pay: ${round(value,2)}");