import random
from select import select
from tkinter import Menu
from turtle import begin_fill, pos

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
    

class Games:
    def __init__(self):
        self.strength =0
        self.originalDiceValue = 0 
        self.newDiceValue = 0 
        self.playerName = ""

    def setUpPlayers(self):
        pass
    
    def beginGame(self):
        pass

    def throwDice(self):
        pass
    

class leaderboard:
    pass

    def sortPlayersList(self):
        pass
    
    def displayLeaderboard(self):
        pass

    
class Mulitplayers(Games):
    def __init__(self):
        self.numberOfPlayers = 0 
        self.playersInGame = {} 
        self.bidAmount = 0 
        self.totalBid = 0
        self.playerPoints = {}
        self.playerWins = {}

    def setUpPlayers(self):
        pass

    
class Bunco(Mulitplayers):
    pass

    def gameSummary(self):
        pass

    def setUpPlayers(self):
        print("Let's play the game of Bunco!")
        print("How many players (2-4) ? ")
        totalPlayers = int(input(" >"))
        count = 0
        position = 1 

        while count < totalPlayers:
            validPlayer = False

            while validPlayer != True:
                print("What is the name of player #",position,"?")
                playerName = input(">")

                if playerName in Player.playersList:

                    if playerName in self.playersInGame:
                        print("Player already registered")
                        
                    else:
                        print("How many chips would you bid", playerName, "(1-70)?")
                        chips = int(input(">"))

                        while chips < 1 or chips > 70:
                            print("Invalid number of chips.")
                            print("How many chips would you bid", playerName, "(1-70)?")
                            chips = int(input(">"))

                        self.playersInGame[playerName] = chips
                        validPlayer = True
                
                else:
                    print("There is no player named",playerName)

                
            count += 1
            position +=1

        # TESTING PURPOSES ONLY
        print(self.playersInGame)
        self.beginGame()

    def beginGame(self):
        
        roundNumber = 1 

        round = Round()

        for i in range(6):
            print("Round", roundNumber)
            round.playRound(self.playersInGame,roundNumber,self.playerPoints,self.playerWins)
            roundNumber +=1

class OddOrEven(Games):
    def __init__(self):
        self.userGuess = 0
        super().__init__()

    def beginGame(self):

        invalid = True
        dice = Dice()

        print("Hey",self.playerName,"Odd (O) or Even (E) ?")
        self.userGuess = input("> ")
        
        self.userGuess = self.userGuess.upper()

        self.originalDiceValue = dice.rollDice()

        print(self.originalDiceValue)
        
        self.newDiceValue = dice.diceStrength(self.originalDiceValue)

        print("new dice value", self.newDiceValue)

        # TESTING PURPOSES ONLY
        print("New value",self.newDiceValue)

        # Fix up spacing issues
        if self.newDiceValue % 2 == 0 and self.userGuess == "E":
            print("Congratulations,",self.playerName,"! you win")
        
        elif self.newDiceValue % 2 != 0 and self.userGuess == "O":
            print("Congratulations,",self.playerName,"! you win")
        
        else:
            print("Sorry,",self.playerName,"you lose!")
                
            
    def setUpPlayers(self):
        print("Odd or Even")
        print("What is your player name?")
        self.playerName = input(">")
        print(self.playerName)

        if self.playerName in Player.playersList:
            print("You can play ")
            self.beginGame()
        
        else:
            print("No player found")

    
class Maxi(Mulitplayers):
    def __init__(self):
        super().__init__()


    def beginGame(self):
        pass

    
class Dice:

    bunco = False

    def __init__(self):
        self.originalDiceValue = 0 
        self.strength = 0
        self.invalid = True 

    def rollDice(self):
        self.originalDiceValue = random.randint(1,6)
        return self.originalDiceValue

    def diceStrength(self,diceValue):

        if Dice.bunco == False:
            print("How strong will you throw (0-5) ?")
            self.strength = int(input("> "))
            
        while self.invalid == True:

            if self.strength > 5 or self.strength <0:
                print("Invalid Choice")
                print("How strong will you throw (0-5) ?")
                self.strength = int(input("> "))

            else:

                self.newDiceValue = self.originalDiceValue + self.strength
            
                if self.newDiceValue > 6:
                    self.newDiceValue = self.newDiceValue - 6 
                
                self.invalid = False

        return self.newDiceValue


    
class Player:
    playersList = [[]]
    totalPlayers = 0 

    def __init__(self):
        self.chips = 100

    def addPlayer(self, userName):
        
        # Check if name is already taken
        if userName not in Player.playersList:

        # Add player to the list
            Player.playersList.append(userName)
            Player.playersList.append(self.chips)
            Player.totalPlayers += 1
            print("Welcome", userName)
            

        else:
            print("Sorry, the name is already taken.")

        # For testing purposes only
        print(Player.playersList)
        print(Player.totalPlayers)
        m = MainMenu()
        m.menu()
        
        
    def getPlayersList(self):
        return Player.playersList

    def setPlayersList(self):
        pass

    
class Round:
    pass

    def playRound(self,playersInGame,roundNumber, playerPoints, playerWins):

        continueTurn = True

        for key in playersInGame:
            
            roundPoints = 0  
        
            while continueTurn != False:

                points = 0 
                print("Working",key)
                print("It's", key,"'s turn." )
                
                d1 = Dice()
                d2 = Dice()
                d3 = Dice()

                d1Value = d1.rollDice()
                d2Value = d2.rollDice()
                d3Value = d3.rollDice()

                d1NewVal = d1.diceStrength(d1Value)
                Dice.bunco = True
                d2NewVal = d2.diceStrength(d2Value)
                d3NewVal = d3.diceStrength(d3Value)
                Dice.bunco = False

                print(d1NewVal)
                print(d2NewVal)
                print(d3NewVal)
                
                if d1Value == d2NewVal == d3NewVal:
                    if d1Value == roundNumber:
                        points+=21
                        continueTurn = False
                    
                    else:
                        points+=5
                        
                else:

                    if d1NewVal == roundNumber:
                        points +=1                    

                    if d2NewVal == roundNumber:
                        points+=1
                    
                    if d3NewVal == roundNumber:
                        points+=1
                    
                    else:
                        continueTurn = False

                roundPoints+=points
                print(points)
                print(roundPoints)
            
            playerPoints[key] = roundPoints
            continueTurn = True
            print(playerPoints)

atd = AllThatDice()
atd.run()