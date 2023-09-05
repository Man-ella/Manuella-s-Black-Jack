import random

suits = ['♠','♣','♦','♥'] 

class Card(object):  
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        
    def __str__(self):
        return '(suit: {}, rank: {})'.format(self.suit,self.rank)

class CardCollection(object): 

    def __init__(self):
        self.cards = []

    def add_card(self, card): 
        self.cards.append(card)

    def draw_card(self): 
        select = self.cards.pop(random.randint(0, len(self.cards)-1))   
        return select  

    def make_deck(self):
            deck = []
            suits = ['♠','♣','♦','♥']
            ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
            for suit in suits:
                for rank in ranks:
                    deck.append(Card(suit,rank))
            shuffled = random.sample(deck, len(deck))
            self.cards = shuffled

    def value(self):
        all_cards = self.cards
        all_ranks = []
        added = []
        total = 0
        record = 0
        for card in all_cards:
            all_ranks.append(card.rank)
        for element in all_ranks:
            added.append(element)
            
            if type(element)==int: 
                total += element
                if total > 21 and added.count('A')==1 and record ==0:
                    total -=10
                    record +=1
                  
            elif element in ['J','Q','K']:
                total += 10
                if total > 21 and added.count('A')==1 and record ==0:
                    total -=10
                    record +=1
            elif element == 'A':
                total += 11
                if total > 21 and 'A' in added:
                    total -=10 
                    record += 1
        return total
                

    def __str__(self):
        full_deck = []
        for card in self.cards:
            full_deck.append(str(card))
        return '{}'.format(full_deck)

def main():
    print("<<<<Starting>>>>")
    deck = CardCollection()
    deck.make_deck() # initialize a fresh deck 

    player_hand = CardCollection()
    status_player = True
    while status_player:
       drawn_player = deck.draw_card()
       player_hand.add_card(drawn_player)
       print(f"You drew {drawn_player}")
       player_current_value = player_hand.value()
       print(f"your sum: {player_current_value}")
       if player_current_value == 21:
           print("player wins")
           break
       elif player_current_value > 21:
           print("player loses")
           break
       else:
           x = 1
           while x:
               choice = input("Want another card? yes or no: ")
               if choice == "yes":
                   status_player = True
                   x = 0
               elif choice == "no":
                   status_player = False
                   x = 0
               else:
                   print("Invalid input. Please choose yes or no!")
                   x = 1       
    else:
        dealer_hand = CardCollection()
        status_dealer = True
        while status_dealer:
            drawn_dealer = deck.draw_card()
            dealer_hand.add_card(drawn_dealer)
            print(f"I drew {drawn_dealer}")
            dealer_current_value = dealer_hand.value()
            print(f"my sum: {dealer_current_value}")
            if dealer_current_value == 21:
                print("dealer wins")
                break
            elif dealer_current_value > 21:
                print("player wins")
                break
            elif dealer_current_value >= 17 and dealer_current_value < 21:
                if player_current_value == dealer_current_value:
                    print("game is a push")
                elif player_current_value > dealer_current_value:
                    print("player wins")
                elif player_current_value < dealer_current_value:
                    print("dealer wins")
                break

if __name__ == "__main__":
    main()
    