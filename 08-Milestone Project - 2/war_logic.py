from war import Card, Deck, Player


def main():
    # Create two players
    player1 = Player('Mariette')
    player2 = Player('Kit')
    # Create and shuffle deck
    deck = Deck()
    deck.shuffle()
    # Split deck between players
    for i in range(26):
        player1.add_cards(deck.deal_one())
        player2.add_cards(deck.deal_one())

    round = 1
    while len(player1.hand) > 5 and len(player2.hand)> 5:
        print(f'Round {round}')
        round +=1

        # Players each draw a card
        player1_general = player1.draw_card()
        #print(f'{player1.name} played {player1_general}')
        player2_general = player2.draw_card()
        #print(f'{player2.name} played {player2_general}')
        pool = [player1_general, player1_general]
        # compare cards
        if player1_general.value > player2_general.value:
            player1.add_cards(pool)
        elif player2_general.value > player1_general.value:
            player2.add_cards(pool)
        else:
            print('War!')
            war = True
            while war:
                for i in range(5):
                    pool.append(player1.draw_card())
                    pool.append(player2.draw_card())

                player1_general = player1.draw_card()
                player2_general = player2.draw_card()

                pool.extend([player1_general, player2_general])

                if player1_general.value > player2_general.value:
                    player1.add_cards(pool)
                    war = False
                elif player2_general.value > player1_general.value:
                    player2.add_cards(pool)
                    war = False
                else:
                    continue
    else:
        if len(player1.hand)<= 5:
            print(f'{player2.name} wins!')
        else:
            print(f'{player1.name} wins!')

# each player draws a card
# compare cards
        # if winner, winner adds cards to bottom of deck
        # if war, each player draws army of 3  and sends general to fight


if __name__ == '__main__':
    main()