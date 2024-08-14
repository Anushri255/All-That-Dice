class AllThatDice:
    def __init__(self):
        pass

    def run(self):
        print("Welcome to All-That-Dice!")
        print()
        main = MainMenu()
        main.menu()
  

class MainMenu:
    def __init__(self):
        pass

    def menu(self):
        print("What would you like to do?")
        print(" (r) register a new player")
        print(" (s) show the leader board")
        print(" (p) play a game")
        print(" (q) quit")
        userCommandChoice = input(">")
        
        if userCommandChoice == "r":
            userName = input("What is the name of the new player?")
            player = Player() 
            player.addPlayer(userName)
        
        elif userCommandChoice =="s":
            pass

        elif userCommandChoice == "p":

            invalid = True
        
            while invalid != False:
                print("Which game would you like to play?")
                print(" (o) Odd-or-Even")
                print(" (m) Maxi")
                print(" (b) Bunco")
                userGameChoice = input("> ")

                userGameChoice = userGameChoice.lower()
                print(userGameChoice)

                if userGameChoice == "o":
                    invalid = False
                    oddEven = OddOrEven()
                    oddEven.setUpPlayers()

                elif userGameChoice == "m":
                    if Player.totalPlayers < 3:
                        print("Not enough players to play Maxi")
                        print()
                   
                    else:
                        invalid = False                  
                        maxi = Maxi()
                        maxi.setUpPlayers()
          
                
                elif userGameChoice == "b":
                    if Player.totalPlayers < 2:
                        print("Not enough players to play Bunco.")
                    
                    else:
                        invalid = False
                        bunco = Bunco()
                        bunco.setUpPlayers()
                
                else:
                    print("Invalid Choice")


        elif userCommandChoice == "q":
            quit()
    