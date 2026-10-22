import random;

print(''' 
    /=======================\\
    | Welcome to Hangman!!! |
    \\=======================/
      
      ''')


HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

word_list = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()

placeholder = ""
chosen_word = random.choice(word_list);
game_over = False;
lives = 0;
correct_letter = [];
print(chosen_word);

for char in range(len(chosen_word)):
        placeholder += "_";
        
while not game_over:
    guess = input("Guess a letter: ")
    display = ""


    correct_letter_count = len(correct_letter);  
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letter.append(letter)
        elif letter in correct_letter:
            display += letter    
        else:
            display += "_"
    print(f"{display} \n")
    
    if guess not in chosen_word:
        lives +=1
        if lives >= 6:
            game_over = True;
            print("you loose.")
        else:
            print(f"****************** {6 - lives} / 6 Lives **************** \n") 
    
    print(HANGMANPICS[lives])   
    if "_" not in display:
        game_over = True;
        print("You win.")
    