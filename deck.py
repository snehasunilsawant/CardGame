import random
#All Classes
class Card():
    def __init__(self,suitsName,cardName,cardValue):
        self.suitsName=suitsName
        self.cardName=cardName        
        self.cardValue=cardValue

class Deck():
    def __init__(self,deckList):
        self.deckList=deckList
        for i in suits:
            for j in range(0,13):
                deck_card=Card(i,cardName[j],j+1)                
                tupple=(deck_card.suitsName,deck_card.cardName,deck_card.cardValue) 
                deckList.append(tupple)                         
        random.shuffle(deckList)

    def draw(self):        
        print self.deckList[len(self.deckList)-1][1] + " of " + self.deckList[len(self.deckList)-1][0]
        numberOfCard = self.deckList[len(self.deckList)-1][2]
        del self.deckList[-1:]
        return numberOfCard
        

class Player():
    def __init__(self,first_name,last_name,power):
        self.first_name=first_name
        self.last_name=last_name
        self.power=power

    def addScore(self,score):
        score = score + 1
        return score

class Game():
    def __init__(self,id,player1_totalScore,player2_totalScore):
        self.id=id
        self.player1_totalScore=player1_totalScore
        self.player2_totalScore=player2_totalScore
        
    def rules(self,player1CardValue,player2CardValue):
        if(player1CardValue > player2CardValue):
            print "== " + player_1.last_name + " got score =="
            self.player1_totalScore = player_1.addScore(self.player1_totalScore)

        elif(player2CardValue > player1CardValue):
            print "== " + player_2.last_name + " got score =="
            self.player2_totalScore = player_2.addScore(self.player2_totalScore)
            
        else:
            print "== both got score =="
            self.player1_totalScore = player_1.addScore(self.player1_totalScore)
            self.player2_totalScore = player_2.addScore(self.player2_totalScore)

    
    def gameOver(self,player1TotalScore,player2TotalScore):
        if(player1TotalScore > player2TotalScore):
            print  (player_1.last_name + " Wins game " + str(game_1.id)).upper()
        elif(player2TotalScore > player1TotalScore):
            print ((player_2.last_name + " Wins game " + str(game_1.id))).upper()
        else:
            print ("Both Wins. It was a draw").upper()   



# Declaration of objects , lists and variables 
suits=["Diamonds","Hearts","clubs","Spade"]
cardName=["Ace","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack","Queen","King"]
player_1=Player('Sneha','Super Woman','winner')
player_2=Player('Andrew','dojo warrior','winner')  

#Logic
game_1 = Game(1,0,0)
deck=Deck([])
for i in range(0,26):
    p1=deck.draw()
    p2=deck.draw()
    game_1.rules(p1,p2)
print player_1.last_name + " total Score : ",game_1.player1_totalScore
print player_2.last_name + " total Score : ",game_1.player2_totalScore
game_1.gameOver(game_1.player1_totalScore,game_1.player2_totalScore)
print "GAME OVER"


     



