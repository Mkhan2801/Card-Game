from random import shuffle

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}
black_jack_values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}


class Card:
    def __init__(self, suit, rank):
        self.suit  = suit
        self.rank = rank
        self.value = values[rank]
        self.b_j_value = black_jack_values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit
    
class Deck:
    def __init__(self):
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                created_card = Card(suit,rank)
                self.all_cards.append(created_card)
        
        shuffle(self.all_cards)

    def __str__(self):
        deck_comp = ''  # start with an empty string
        for card in self.all_cards:
            deck_comp += '\n '+card.__str__() # add each Card object's print string
        return 'The deck has:' + deck_comp
    
    def shuffle(self):
        shuffle(self.all_cards)

    def  deal_one(self):
        if len(self.all_cards)>0:
            return self.all_cards.pop()
        else:
            return "Dealer have no card!"
        

class Player:
    def __init__(self,name):
        self.name = name
        self.all_cards = []

    def __str__(self):
        return f'{self.name} has {len(self.all_cards)} cards.'
    
    def add_card(self,new_card):
        if type(new_card) == type([]):
            self.all_cards.extend(new_card)
        else:
            self.all_cards.append(new_card)

    def remove_card(self):
        if len(self.all_cards)>0:
            return self.all_cards.pop(0)
        else:
            return f'{self.name} has no cards.'
        
    def cards(self):
        deck_comp = ''  # start with an empty string
        for card in self.all_cards:
            deck_comp += '\n '+card.__str__()  # add each Card object's print string
        return 'The '+ self.name +' has:' + deck_comp
    
    def sum(self):
        subtotal = 0  # start with an empty string
        for card in self.all_cards:
            subtotal += card.b_j_value # add each Card object's print string
        return  subtotal

    
def game():
    print('Enter 1 for Card war Enter 2 for Black jack')
    input_num = int(input('Chose the game you want to play: '))
    if input_num == 1:
        card_war()
    elif input_num == 2:
        blackjack()
    else:
        print('Wrong input!!!')
        game() 

def card_war():
    print('Play Card War')
    new_Deck = Deck()
    no = 0
    while  not no in range(1,3):
        no = int(input('Enter no of player (only enter 1 or 2) :'))
        if not no in range(1,3):
            print('Plese enter valid no.')
        
    if no==1:
        P1 = make_player(1)
        cpu = make_player('cpu')
        print(P1)
        print(cpu)
    elif no==2:
        P1 = make_player(1)
        P2 = make_player(2)
        print(P1)
        print(P2)
        
    


def make_player(no):
    if no=='cpu':
        return Player('Cpu')
    name = input(f'Chose Player_{no} Name: ')
    
    if not name:
        return Player(f'player_{no}')
    else:
        return Player(name)



def blackjack():
    print('Play Black jack')
    new_Deck = Deck()
    drow_new = True
    no = 0
    while  not no in range(1,5):
        no = int(input('Enter no of player (only enter 1 to 4) :'))
        if not no in range(1,5):
            print('Plese enter valid no.')
    
    players =[]
    while no>0:
        print(no)
        player = make_player(no)
        players.append(player)
        no=no-1

    
    
    table = Player('Table')
    table.drow= False
    table.add_card(new_Deck.deal_one())
    table.add_card(new_Deck.deal_one())
    print(f'Table has {table.all_cards[0]} face up and a card face down')


    for player in players:
        player.add_card(new_Deck.deal_one())
        player.drow = False

    while drow_new:
        temp =  False
        for player in players:
            if not player.drow:
                drow_new_card(player,new_Deck)
                temp = True
        
        drow_new = temp
  
    print(table.cards())
    print(f'Sum of Table is {table.sum()}')
    while table.sum()<17:
        table.add_card(new_Deck.deal_one())
        print(table.cards())
    table_dif = 21-table.sum()
    

    for play in players:
        print('wwin test')
        state_chack(play)
        if play.sum()>21:
            print(f'Sum of {play.name} is {play.sum()}')
            print(f'{play.name}, You are busted')

        elif play.sum()<22:
            dif = 21-play.sum()
            print(dif,table_dif)    
            if dif > table_dif:
                print(f'Sum of {play.name} is {play.sum()} and sum of Table is {21-table_dif}')
                print(f'In game {play.name} VS Table. Table wins')

            else:
                print(f'Sum of {play.name} is {play.sum()} and sum of Table is {21-table_dif}')
                print(f'In game {play.name} VS Table. {play.name} wins')

        else:
            print(f'In game {play.name} VS Table. Table wins')

    

            


    
     
def drow_new_card(play,deck):

    print(play.cards())
    print(f'Sum of {play.name} is {play.sum()}')
    drow = input(f'{play.name} do you want to drow a new card(y/n):')
    if drow == 'y' or drow =='Y':
        play.add_card(deck.deal_one())
        
    elif drow == 'n' or drow =='N':
        play.drow = True
    else:
        print('Enter valid input!!')
        drow_new_card(play,deck)

    state_chack(play)

def state_chack(player_name):
    if player_name.sum() < 21 and player_name.drow:
        return print(player_name.cards() +'/n '+ f'Sum of {player_name.name} is {player_name.sum()}')

    if player_name.sum() == 21:
            print(f'{player_name.name}, You got a Black jack')
            player_name.drow = True
            return print(player_name.cards() +'/n '+ f'Sum of {player_name.name} is {player_name.sum()}')
        
    if player_name.sum() > 21:
            print(f'{player_name.name}, You are busted')
            player_name.drow = True
            return print(player_name.cards() +'/n '+ f'Sum of {player_name.name} is {player_name.sum()}')




blackjack()

