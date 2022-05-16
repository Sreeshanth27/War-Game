import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')


#dictionary for ranks
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}


#Creating a class for card
class Card():
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    def __str__(self):
        return self.rank + " of " + self.suit


 #Creating a class for deck
class Deck:
    
    def __init__(self):
        
        self.all_cards = []
        
        for suit in suits:
            for rank in ranks:
                created_card = Card(suit,rank)
                self.all_cards.append(created_card)
                
    def shuffle(self):
        random.shuffle(self.all_cards)
        
    def return_one(self):
        return self.all_cards.pop()


#Creating a player class
class Player:
    
    def __init__(self,name):
        self.name = name
        self.all_cards = []
        
    def remove_one(self):
        return self.all_cards.pop(0)
    
    def add_cards(self,new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)
        
    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards'


#Game Setup
p1 = input('ENTER THE NAME OF FIRST PLAYER: ')
p2 = input('ENTER THE NAME OF SECOND PLAYER: ')

player_one = Player(p1)
player_two = Player(p2)

new_deck = Deck()
new_deck.shuffle()

for i in range(26):
    player_one.add_cards(new_deck.return_one())
    player_two.add_cards(new_deck.return_one())

game_on = True

round_num = 0

while(game_on == True):
    round_num += 1
    
    print(f'Round {round_num}')
    print(f'{player_one.name} has {len(player_one.all_cards)} cards')
    print(f'{player_two.name} has {len(player_two.all_cards)} cards')
    
    if len(player_one.all_cards) == 0:
        print(f'{player_one.name} is out of cards! {player_two.name} WINS!')
        game_on = False
        break
        
    if len(player_two.all_cards) == 0:
        print(f'{player_two.name} is out of cards! {player_one.name} wins')
        game_on = False
        break
     
    #Starting a new round
    player_one_cards = []
    player_one_cards.append(player_one.remove_one())
    
    player_two_cards = []
    player_two_cards.append(player_two.remove_one())
    
    #while at war
    
    war = True
    
    while war:
        
        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            war = False
            
        elif player_two_cards[-1].value > player_one_cards[-1].value:
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)
            war = False
            
        else:
            print('War!')
            print('IN THE WAR:')
            print(f'{player_one.name} has {len(player_one.all_cards)} cards')
            print(f'{player_two.name} has {len(player_two.all_cards)} cards')
            
            if(len(player_one.all_cards) < 3):
                print(f'{player_one.name} RUNS OUT OF CARDS')
                print(f'{player_two.name} WINS!')
                game_on = False
                break
                
            if(len(player_two.all_cards) < 3):
                print(f'{player_two.name} RUNS OUT OF CARDS')
                print(f'{player_one.name} WINS!')
                gane_on = False
                break
                
            else:
                for i in range(3):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())