print('''
              _                 __                 
      __.--**"""**--...__..--**""""*-.            
    .'                                `-.         
  .'                         _           \        
 /                         .'        .    \   _._ 
:                         :          :`*.  :-'.' ;
;    `                    ;          `.) \   /.-' 
:     `                             ; ' -*   ;    
       :.    \           :       :  :        :    
 ;     ; `.   `.         ;     ` |  '             
 |         `.            `. -*"*\; /        :     
 |    :     /`-.           `.    \/`.'  _    `.   
 :    ;    :    `*-.__.-*""":`.   \ ;  'o` `. /   
       ;   ;                ;  \   ;:       ;:   ,/
  |  | |                       /`  | ,      `*-*'/ 
  `  : :  :                /  /    | : .    ._.-'  
   \  \ ,  \              :   `.   :  \ \   .'     
    :  *:   ;             :    |`*-'   `*+-*       
    `**-*`""               *---*
''')


print("Welcome to Treasure Island.")
print("your mission is to find the treasure.")
print("you're at the cross road. Where do you want to go?")
direction =input('    "Left" or "Right"? \n')
if direction.lower() == "right":
    print("Game Over!")
else:
    print("A lake is in front of you and a boat is coming, what do you do?") 
    action = input('    "Swim" or "Wait"? \n')
    if(action.lower() == "swim"):
        print("        Game Over       ")
    else:
        print("You have crossed the lake and faced with three doors. which door you will choose?")
        door = input('     "Red", "Blue" or "Yellow? \n')
        if(door.lower() == "red" or door.lower() == "blue"):
            print("        Game Over          ");
        else:
            print("      You Win!        ");