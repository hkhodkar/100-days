
true_chars = ["t","r","u","e"]
love_chars = ["l","o","v","e"]
def calculate_love_score(name1, name2):
    apeended_name = name1 + name2;
    true_score = 0;
    love_score = 0;
    for letter in apeended_name:
        if letter.lower() in true_chars:
            true_score = true_score+1;
        if letter.lower() in love_chars:
            love_score +=1;
    print(f"{true_score}{love_score}")    

calculate_love_score("Angela Yu","Jack Bauer")    