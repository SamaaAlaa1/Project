
# Purpose: Subtract a Square is a game It is played by two
#people with a pile of coins (or other tokens) between them. The players take turns removing
#coins from the pile, always removing a non-zero square number of coins (1, 4, 9, 16, ...).
#The player who removes the last coin wins.
from random import randint
def is_square_number(player_move):
    # check if the number of the palyer's move is a square number
    if (player_move != 0 and (player_move ** 0.5) % 1 == 0):
        return True
    
    else:
        return False
    
#Welcome message and Explain the rules of the game 
print('''
                  =======WELCOME=======
              ======Sbtract a Square======
          In this game there is a pile of coins
          each player can remove a square number of coins 
          the player who takes the last coin wins
            Enjoy:)
      ''')

while(True):
    
    #Get the number of coins to start the game with
    coins_choice = input('''
                         Do you want to choose the number of coins or
                         do you want a random number?
                         1 => Enter the number of coins
                         2 => Random number 
                         ''')
    
    if(coins_choice == '1'):
        while True:
            #Get the number of coins and check if it's Valid
            try:
                n_coins = input("Enter The Number of coins you want to start the game with:")
                n_coins = int(n_coins)
                
                #check if it's positive number
                if n_coins <= 0:
                    print("ERROR:Please enter a positive number")
                    continue
                
                #check if it's not a square number
                if is_square_number(n_coins):
                    print("You can't Enter a square number!\nTry again")
                    continue
                break
            #Reject string and float
            except ValueError:
                print("ERROR:Please enter an integer")

    elif(coins_choice == '2'):
        #Get random number of coins to start the game with
        while(True):
            n_coins = randint(100,500)
            
            #check if it's not a square number
            if(not is_square_number(n_coins)):
                break
            
    print(f"The number of coins is {n_coins}")
    
    #Game playing
    while (n_coins > 0):
        #Get Player1's move and check if it's Valid
        while True:
            try:
              player1_move = int(input("player1's move\nEnter your move:"))
              
              #check if it's positive number
              if player1_move > 0:
                  break
              else:
                  print("ERROR: Please enter a positive square number")
                  
            #Reject string and float  
            except ValueError:
              print("ERROR: Please enter an integer square number")
        
        #check if it's a square number
        if not is_square_number(player1_move):
           print("Please insert a square number!")
           continue
       
         
        if player1_move > n_coins:
           print("ERROR: Invalid Number!")
           continue
    
        n_coins -= player1_move
        
        #Check for a winner
        if (n_coins <= 0):
            print("Player 1 is a winner")
            break
        
        #Update status
        print(f"Now we have '{n_coins}' coins")
    
        while True:
            #Get Player2's move and check if it's Valid
            try:
              player2_move = int(input("player2's move\nEnter your move:"))
              
              #check if it's positive number
              if player2_move > 0:
                  break
              else:
                  print("ERROR: Please enter a positive square number")
                  
            #Reject string and float
            except ValueError:
              print("ERROR: Please enter an integer square number")
              
        #check if it's a square number      
        if not is_square_number(player2_move):
           print("Please insert a square number!")
           continue
       
        #check that the player's input is in range
        if player2_move > n_coins:
           print("ERROR: Invalid Number!")
           continue
       
        n_coins -= player2_move
        
        #Check for a winner
        if (n_coins <= 0):
            print("Player 2 is a winner")
            break
        
        #Update status
        print(f"Now we have '{n_coins}' coins")
        
    #End of the game or Play again
    print('''
              1 => Play Again
              2 => Exit
              ''')
    
    #End ot the game : Ask the player to play again or Exit game
    while True:
        game = input("Enter 1 to play again or 2 to Exit: ")
        if game == '2':
            break
        elif game == '1':
            break
        else:
            print("Error: Invalid choice!! Please enter either 1 or 2.")
    if(game == '1'):
        continue
    else:
        break
