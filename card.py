# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 23:02:22 2020

@author:    Parna
"""
import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}
class Card:
    def __init__(self,suit,rank):
        self.rank=rank
        self.suit=suit
        self.value=values[rank]
    def __str__(self):
        return self.rank+" of "+self.suit
    
"""    
two_hearts=Card("hearts",'Three')

four_hearts=Card("hearts",'Four')
eg=four_hearts.value >two_hearts.value
print(eg)
"""

class Deck:
    def __init__(self):
        self.all_cards=[]
        for suit in suits:
            for rank in ranks:
                 created_card=Card(suit,rank)
                 self.all_cards.append(created_card)
    def shuffle(self):
        random.shuffle(self.all_cards)
    def deal_one(self):
        return self.all_cards.pop()
"""             
new_deck=Deck()

bottom_card=new_deck.all_cards[-1]
print(bottom_card)

for card_object in new_deck.all_cards:
    print(card_object)
new_deck.shuffle()
bottom_card=new_deck.all_cards[-1]
print("\n",bottom_card)  
    """
"""
new_deck=Deck()
new_deck.shuffle()
mycard=new_deck.deal_one()  
print(mycard)  
print(len(new_deck.all_cards))
"""

class Player:
    
    def __init__(self,name):
        self.name = name
        # A new player has no cards
        self.all_cards = [] 
        
    def remove_one(self):
       
        return self.all_cards.pop(0)
    
    def add_cards(self,new_cards):
        #add multiple cards
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        
        else:
            self.all_cards.append(new_cards)
    
    
    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'
"""
new_player=Player("parna")
#print(new_player)
new_player.add_cards(mycard)
print(new_player)
new_player.add_cards([mycard,mycard,mycard])
print(new_player)
print(new_player.all_cards[0])
new_player.remove_one()
print(new_player)
"""

#GAME_SETUP

player_one=Player("one")
player_two=Player("two")

new_deck=Deck()
new_deck.shuffle()

#split the deck between two players
for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

game_on=True
#while game_on
 
round_num=0#counter
while game_on:
    round_num+=1
    print(f"Round {round_num}")
    
     # Check to see if a player is out of cards:
    if len(player_one.all_cards) == 0:
        print("Player One out of cards! Game Over")
        print("Player Two Wins!")
        game_on = False
        break
        
    if len(player_two.all_cards) == 0:
        print("Player Two out of cards! Game Over")
        print("Player One Wins!")
        game_on = False
        break
#START NEW ROUND
    player_one_cards=[]#current cards in play
    player_one_cards.append(player_one.remove_one())
        
    player_two_cards=[]#current cards in play
    player_two_cards.append(player_two.remove_one())

#while at_war
    at_war = True

    while at_war:


        if player_one_cards[-1].value > player_two_cards[-1].value:

            # Player One gets the cards
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            
            
            # No Longer at war, time for next round
            at_war = False
        
        elif player_one_cards[-1].value < player_two_cards[-1].value:

            # Player Two gets the cards
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)
            
            # No Longer at "war" , time for next round
            at_war = False

        else:
            print('WAR!')
            # This occurs when the cards are equal.
            # We'll grab another card each and continue the current war.
            
            # First check to see if player has enough cards
            
            # Check to see if a player is out of cards:
            if len(player_one.all_cards) < 5:
                print("Player One unable to play war! Game Over at War")
                print("Player Two Wins! Player One Loses!")
                game_on = False
                break

            elif len(player_two.all_cards) < 5:
                print("Player Two unable to play war! Game Over at War")
                print("Player One Wins! Player One Loses!")
                game_on = False
                break
            # Otherwise, we're still at war, so we'll add the next cards
            else:
                for num in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())







 