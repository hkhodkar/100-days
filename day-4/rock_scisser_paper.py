import random;
user_choose = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissor? ");

computer_choose = random.randint(0,2);

list = ["""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
"""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""",
"""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""]

print(f"You choose {list[int(user_choose)]} \n")
print(f"The computer choose {list[int(computer_choose)]} \n")

if int(user_choose)==computer_choose:
    print("Draw! Both of you had a same choice! \n")
elif int(user_choose) > computer_choose:
    print("Congratulations You are the winner! \n")
else:
    print("Oops, The computer is the Winner! \n")
