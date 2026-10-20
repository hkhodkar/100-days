import string;
import random;
print("Welcome to py Password Generator")


password = [];
numbers_list = [];
letters_list = [];
symbols_list = [];

for char in string.ascii_letters:
    letters_list.append(char);

for num in string.digits:
    numbers_list.append(num)
    
for sym in string.punctuation:
    symbols_list.append(sym);
    
letters_count = input("How many letters would you like in your password? \n")
symbols_count = input("How many symbol would you like? \n")
numbers_count = input("How many number would you like? \n")

for char in range(int(letters_count)):
    password.append(random.choice(letters_list))

for sym in range(int(symbols_count)):
    password.append(random.choice(symbols_list));
    
for num in range(int(numbers_count)):
    password.append(random.choice(numbers_list));    

random.shuffle(password)
print(f"Your new password is: {''.join(password)}")
