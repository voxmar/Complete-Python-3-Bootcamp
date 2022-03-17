# add shebang
import random

# computer dealer + human player (classes)
# human has a hand and a bank roll from which to place bets
# play starts with player having two cards face up, dealer having one face up and one face down
# player wants to be closer to 21 than dealer
# player can hit (receive another card) or stay(stop cards)
# after player goes, dealer goes, closest to 21 wins
# player can keep hitting as long as they like, but if they go over 21 they go bust and the dealer wins and takes the money
# if computer closer to 21 they win, computer can keep hitting until they beat the player or go bust

# face cards all have value 10, aces are either 1 or 11 whichever is preferable

class Card:
    values = {'Ace' : 11, 'King' : 10, 'Queen' : 10, 'Jack' : 10, 'Ten' : 10, 'Nine' : 9, 'Eight' : 8, 'Seven' : 7,
              'Six' : 6, 'Five' : 5, 'Four' : 4, 'Three' : 3, 'Two' : 2 }

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = Card.values[rank]

    def __str__(self):
        return f'{self.rank} of {self.suit}'

class Deck:

    def __init__(self):
        self.cards = []

        for suit in ['Hearts', 'Diamonds', 'Clubs', 'Spades']:
            for rank in Card.values.keys():
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_one(self):
        return self.cards.pop()

class Player:

    def __init__(self, name, starting_balance):
        self.name = name
        self.balance = starting_balance
        self.hand = []

    def __str__(self):
        hand_string = ', '.join([str(card) for card in self.hand])
        return f'{self.name} has £{self.balance} and is holding {hand_string}'

    def bet(self, amount):
        if amount > self.balance:
            print('Insufficient funds, no bet placed')
            return 0
        else:
            self.balance -= amount
            print (f'Bet successfully placed, balance is now: £{self.balance}')
            return amount

    def collect_winnings(self, amount):
        self.balance += amount

    def hit(self, card):
        self.hand.append(card)

    def sort_hand(self):
        """
        Sorting hand using bubble sort to put aces last to give most advantageous use of aces
        """
        for n in range(len(self.hand) - 1, 0, -1):
            for i in range(n):
                if self.hand[i].value > self.hand[i + 1].value:
                    self.hand[i], self.hand[i + 1] = self.hand[i + 1], self.hand[i]


    def evaluate_hand(self):
        hand_value = 0
        self.sort_hand()
        for card in self.hand:
            if 'Ace' in str(card):
                if hand_value < 10:
                    hand_value += 11
                else:
                    hand_value += 1
            else:
                hand_value += card.value
        return hand_value

    def discard_hand(self):
        self.hand = []

class Dealer:
    def __init__(self):
        self.hand = []

    def reveal_one(self):
        return str(self.hand[0])

    def reveal_hand(self):
        return ', '.join([str(card) for card in self.hand])

    def hit(self, card):
        self.hand.append(card)

    def sort_hand(self):
        """ Sorting hand using bubble sort to put aces last to give most advantageous use of aces """
        for n in range(len(self.hand) - 1, 0, -1):
            for i in range(n):
                if self.hand[i].value > self.hand[i + 1].value:
                    self.hand[i], self.hand[i + 1] = self.hand[i + 1], self.hand[i]


    def evaluate_hand(self):
        hand_value = 0
        self.sort_hand()
        for card in self.hand:
            if 'Ace' in str(card):
                if hand_value < 10:
                    hand_value += 11
                else:
                    hand_value += 1
            else:
                hand_value += card.value
        return hand_value

    def discard_hand(self):
        self.hand = []



def player_turn(player, deck):
    global pool
    hand_value = player.evaluate_hand()
    print(f'{player.name}\'s turn started')
    while hand_value < 21:
        print(f'The value of {player.name}\'s hand is {hand_value}')

        move = input(f'What would you like to do, {player.name}? Bet, hit, or stay?')
        while move.lower() not in ['bet', 'hit', 'stay']:
            print('Move must be bet, hit, or stay.')
            move = input('What would you like to do? Bet, hit, or stay?')

        if move == 'bet':
            amount = float(input('How much would you like to bet?'))
            amount = player.bet(amount)
            pool += amount*2
            print (f'Potential winnings are now £{pool}')
        elif move == 'hit':
            card = deck.deal_one()
            player.hit(card)
            print(f'{player.name} received {str(card)}')
            hand_value = player.evaluate_hand()
        elif move == 'stay':
            break
    else:
        print(f'{player.name} reached 21, automatically staying.')
    return hand_value


pool = 0

def main():
    # set up the table
    dealer = Dealer()
    global pool
    pool = 0

    player_name = input('Hello player, what is your name?')
    opening_balance = 0
    while opening_balance == 0:
        try:
            opening_balance = float(input('How much money are you playing with today?'))
        except ValueError:
            print('Money must be a number.')
            continue
    player = Player(name=player_name, starting_balance=opening_balance)

    another_round = True
    while another_round:
        print('Starting a round')
        print(f'Potential winnigs: £{pool}')
        # Play a round
        # Deal cards
        deck = Deck()
        deck.shuffle()

        for i in range(2):
            dealer.hit(deck.deal_one())
            player.hit(deck.deal_one())

        # Reveal cards
        print(f'Dealer is holding {dealer.reveal_one()} and one other card')
        print(player)

        # Player turn
        while True:
            player_total = player_turn(player, deck)
            if player_total > 21 :
                print(f'Player {player.name} went bust, the house wins!')
                break
            else:  # computer turn
                dealer_total = dealer.evaluate_hand()
                print(f'Dealer is holding {dealer.reveal_hand()} worth {dealer_total}')
                while dealer_total <= player_total:
                    dealer.hit(deck.deal_one())
                    dealer_total = dealer.evaluate_hand()
                    print(f'Dealer is now holding {dealer.reveal_hand()} worth {dealer_total}')
                    if dealer_total > 21:
                        print('Dealer went bust, player wins!')
                        player.collect_winnings(pool)
                        print(f'{player.name}\'s balance is now £{player.balance}')
                        pool = 0
                        break
                else:
                    print('Dealer wins!')
                    pool = 0
            break

        player.discard_hand()
        dealer.discard_hand()
        # End of round
        carry_on = input('Another round? (y/n)')
        while carry_on not in ['y', 'n']:
            carry_on = input('Answer must be y or n . Another round?')
        if carry_on == 'y' :
            another_round = True
        elif carry_on == 'n':
            another_round = False
    print(f'Thank you for playing, take this receipt for {player.balance} to the counter to cash out.')


if __name__ == '__main__':
    main()