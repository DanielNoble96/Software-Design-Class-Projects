#  File: Poker.py

#  Description: This program simulates a basic game of poker involving 2-6 players.
#               It deals a hand of five cards randomly to each player and then
#               determines a winner based on the hands of each.

#  Student's Name: Daniel A. Noble Hernandez

#  Student's UT EID: dan833

#  Course Name: CS 313E

#  Unique Number: 51345

#  Date Created: 22nd September 2018

#  Date Last Modified: 28th September 2018

import random

class Card (object):
    RANKS = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)

    SUITS = ('C', 'D', 'H', 'S')

    # constructor
    def __init__ (self, rank = 12, suit = 'S'):
        if (rank in Card.RANKS):
            self.rank = rank
        else:
            self.rank = 12

        if (suit in Card.SUITS):
            self.suit = suit
        else:
            self.suit = 'S'

    # string representation of a Card object
    def __str__ (self):
        if (self.rank == 14):
            rank = 'A'
        elif (self.rank == 13):
            rank = 'K'
        elif (self.rank == 12):
            rank = 'Q'
        elif (self.rank == 11):
            rank = 'J'
        else:
            rank = str(self.rank)

        return (rank + self.suit)

    # equality tests
    def __eq__ (self, other):
        return self.rank == other.rank

    def __ne__ (self, other):
        return self.rank != other.RANKS

    def __lt__ (self, other):
        return self.rank < other.rank

    def __le__ (self, other):
        return self.rank <= other.rank

    def __gt__ (self, other):
        return self.rank > other.rank

    def __ge__ (self, other):
        return self.rank >= other.rank


class Deck (object):
    # constructor
    def __init__ (self, n = 1):
        self.deck = []
        for i in range(n):
            for suit in Card.SUITS:
                for rank in Card.RANKS:
                    card = Card(rank, suit)
                    self.deck.append(card)

    # shuffle the deck
    def shuffle (self):
        random.shuffle(self.deck)

    # deal all the hands
    def deal (self):
        if (len(self.deck) == 0):
            return None
        else:
            return self.deck.pop(0)


class Poker (object):
    # constructor
    def __init__ (self, num_players = 2, num_cards = 5):
        self.deck = Deck()
        self.deck.shuffle()
        self.all_hands = []
        self.num_players = num_players
        self.numCards_in_Hand = num_cards

        # deal all the hands
        for i in range(num_players):
            hand = []
            for j in range(self.numCards_in_Hand):
                hand.append(self.deck.deal())
            self.all_hands.append(hand)

    # simulates the play of the game
    def play (self, is_royal, is_straight_flush, is_four_kind, is_full_house, is_flush, is_straight, is_three_kind, is_two_pair, is_one_pair, is_high_card):
        # sort the hands of each player and print
        for i in range(len(self.all_hands)):
            sorted_hand = sorted(self.all_hands[i], reverse = False)
            self.all_hands[i] = sorted_hand
            hand_str = ''
            for card in sorted_hand:
                hand_str = hand_str + str(card) + ' '
            print('Player ' + str(i + 1) + ' : ' + hand_str)

        # determine the type of each hand and print
        points_hand = []    # create a list to store points for each hand
        print()

        for i in range(self.num_players):
            if is_royal(self.all_hands[i]):
                points = is_royal(self.all_hands[i])
                points_hand.append(points)
                print('Player ' + str(i + 1) + ': Royal')
                continue

            elif is_straight_flush(self.all_hands[i]):
                points = is_straight_flush(self.all_hands[i])
                points_hand.append(points)
                print('Player ' + str(i + 1) + ': Straight flush')
                continue

            elif is_four_kind(self.all_hands[i]):
                points = is_four_kind(self.all_hands[i])
                points_hand.append(points)
                print('Player ' + str(i + 1) + ': Four of a kind')
                continue

            elif is_full_house(self.all_hands[i]):
                points = is_full_house(self.all_hands[i])
                points_hand.append(points)
                print('Player ' + str(i + 1) + ': Full house')
                continue

            elif is_flush(self.all_hands[i]):
                points = is_flush(self.all_hands[i])
                points_hand.append(points)
                print('Player ' + str(i + 1) + ': Flush')
                continue

            elif is_straight(self.all_hands[i]):
                points = is_straight(self.all_hands[i])
                points_hand.append(points)
                print('Player ' + str(i + 1) + ': Straight')
                continue

            elif is_three_kind(self.all_hands[i]):
                points = is_three_kind(self.all_hands[i])
                points_hand.append(points)
                print('Player ' + str(i + 1) + ': Three of a kind')
                continue

            elif is_two_pair(self.all_hands[i]):
                points = is_two_pair(self.all_hands[i])
                points_hand.append(points)
                print('Player ' + str(i + 1) + ': Two pair')
                continue

            elif is_one_pair(self.all_hands[i]):
                points = is_one_pair(self.all_hands[i])
                points_hand.append(points)
                print('Player ' + str(i + 1) + ': One pair')
                continue

            elif is_high_card(self.all_hands[i]):
                points = is_high_card(self.all_hands[i])
                points_hand.append(points)
                print('Player ' + str(i + 1) + ': High card')




        print(points_hand)
        # determine the winner and print
        print()
        max_index = 0
        max_value = max(points_hand)
        for i in range(len(points_hand)):
            if points_hand[i] == max_value:
                max_index = i + 1

        winner = 'Player ' + str(max_index)
        print(winner + ' wins.')


    # determine if a hand is a royal flush
    # takes as argument a list of 5 Card objects
    # returns a number (points) for that hand
    def is_royal (self, hand):
        same_suit = True
        # check that all five are of the same suit
        for i in range(len(hand) - 1):
            same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)

        if (not same_suit):
            return 0

        rank_order = True
        # check that the cards are valued 10 through Ace
        for i in range(len(hand)):
            rank_order = rank_order and (hand[4 - i].rank == 14 - i)

        if (not rank_order):
            return 0

        # calculate points
        hands_total = 0
        for i in range(len(hand)):
            hands_total += hand[4 - i].rank * 15 ** (4 - i)
        points = hands_total + 10 * 15 ** 5

        return points

    # determine if a hand is a straight flush
    #takes as argument a list of 5 Card objects
    # returns a number (points) for that hand
    def is_straight_flush (self, hand):
        same_suit = True
        for i in range(len(hand) - 1):
            same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)

        if (not same_suit):
            return 0

        # check if there are five cards in consecutive order
        rank_order = True
        for i in range(len(hand) - 1):
            rank_order = rank_order and ((1 + hand[i].rank) == hand[i + 1].rank)

        if (not rank_order):
            return 0

        # calculate points
        hands_total = 0
        for i in range(len(hand)):
            hands_total += hand[4 - i].rank * 15 ** (4 - i)
        points = hands_total + 9 * 15 ** 5

        return points


    # dtermine if a hand is a four of a is_four_kind
    # takes as argument a list of 5 Card objects
    # returns a number (points) for that hand
    def is_four_kind (self, hand):
        # increment a counter each time that two cards are equal
        four_equal_count = 1
        for i in range(len(hand) - 1):
            if (hand[i].rank == hand[i + 1].rank):
                four_equal_count += 1

        if (four_equal_count != 4):
            return 0

        # determine where the four of a kind appears in the list
        # calculate points accordingly
        if (hand[0] != hand[1]):
            hands_total = 0
            for i in range(len(hand)):
                hands_total += hand[4 - i].rank * 15 ** (4 - i)
            points = hands_total + 8 * 15 ** 5

        else:
            hands_total = 0
            for i in range(len(hand)):
                hands_total += hand[i].rank * 15 ** (4 - i)
            points = hands_total + 8 * 15 ** 5

        return points



    # determine if a hand is one pair
    # takes as argument a list of 5 card objects
    # returns a number (points) for that hand
    def is_full_house(self, hand):
        three_equal = False
        two_equal = False
        hands_total = 0

        # check if first two are equal and of same suit
        if ((hand[0].rank == hand[1].rank) and (hand[0].suit == hand[1].suit)):
            two_equal = True

            # check if last three are equal and of same suit
            if ((hand[2].rank == hand[3].rank) and (hand[3].rank == hand[4].rank)):
                if((hand[2].suit == hand[3].suit) and (hand[3].suit == hand[4].suit)):
                   three_equal = True


        # if not check if first three are equal and of same suit
        if ((hand[0].rank == hand[1].rank) and (hand[1].rank == hand[2].rank)):
            if ((hand[0].suit == hand[1].suit) and (hand[1].suit == hand[2].suit)):
                three_equal = True

            # reset two equal count
            two_equal = False

            # check if last two are equal and of same suit
            if ((hand[3].rank == hand[4].rank) and (hand[3].suit == hand[4].suit)):
                two_equal = True


        if (not (three_equal and two_equal)):
            return 0

        # determine where in the list the three pair is to calculate the points
        if (hand[0].rank == hand[1].rank and hand[1].rank == hand[2].rank):
            points = 7 * 15 ** 5 + hand[0].rank * 15 ** 4 + hand[1].rank * 15 ** 3
            points += hand[2].rank * 15 ** 2 + hand[3].rank * 15 + hand[4].rank

        else:
            points = 7 * 15 ** 5 + hand[4].rank * 15 ** 4 + hand[3].rank * 15 ** 3
            points += hand[2].rank * 15 ** 2 + hand[1].rank * 15 + hand[0].rank

        return points



    # determine if a hand is one pair
    # takes as argument a list of 5 card objects
    # returns a number (points) for that hand
    def is_flush(self, hand):
        same_suit = True

        # check that all five are of the same suit
        for i in range(len(hand) - 1):
            same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)

        if (not same_suit):
            return 0

        # calculate points
        hands_total = 0
        for i in range(len(hand)):
            hands_total += hand[4 - i].rank * 15 ** (4 - i)
        points = hands_total + 6 * 15 ** 5

        return points



    # determine if a hand is one pair
    # takes as argument a list of 5 card objects
    # returns a number (points) for that hand
    def is_straight(self, hand):
        rank_order = True

        # check that all five cards have consecutive values
        for i in range(len(hand) - 1):
            rank_order = rank_order and ((1 + hand[i].rank) == hand[i + 1].rank)

        if (not rank_order):
            return 0

        # calculate points
        hands_total = 0
        for i in range(len(hand)):
            hands_total += hand[4 - i].rank * 15 ** (4 - i)
        points = hands_total + 5 * 15 ** 5

        return points



    # determine if a hand is one pair
    # takes as argument a list of 5 card objects
    # returns a number (points) for that hand
    def is_three_kind(self, hand):
        three_equal = False
        for i in range(len(hand) - 1):
            # ensure that elements are in range of the list
            if (i <= 2):
                if (hand[i].rank == hand[i + 1].rank and hand[i + 1].rank == hand[i + 2].rank):
                    three_equal = True

        if (not three_equal):
            return 0

        # determine where in the list the three of a kind are
        # calculate points value accordingly
        if (hand[0].rank == hand[1].rank):
            points = 4 * 15 ** 5 + hand[0].rank * 15 ** 4 + hand[1].rank * 15 ** 3
            points += hand[2].rank * 15 ** 2 + hand[3].rank * 15 + hand[4].rank

        elif (hand[3].rank == hand[4].rank):
            points = 4 * 15 ** 5 + hand[4].rank * 15 ** 4 + hand[3].rank * 15 ** 3
            points += hand[2].rank * 15 ** 2 + hand[1].rank * 15 + hand[0].rank

        else:
            points = 4 * 15 ** 5 + hand[1].rank * 15 ** 4 + hand[2].rank * 15 ** 3
            points += hand[3].rank * 15 ** 2 + hand[0].rank * 15 + hand[4].rank

        return points



    # determine if a hand is one pair
    # takes as argument a list of 5 card objects
    # returns a number (points) for that hand
    def is_two_pair (self, hand):
        pair_count = 0
        points = 0
        for i in range(len(hand) - 1):
            if (hand[i].rank == hand[i + 1].rank):
                pair_count += 1
                # calculate points value depending upon pair locations
                if (i == 0 or i == 1):
                    points = hand[i].rank * 15 ** 2 + hand[i + 1].rank * 15

                elif (i == 2 or i == 3):
                    points += hand[i].rank * 15 ** 4 + hand[i + 1].rank * 15 ** 3

            # identify location of non-paired element
            elif (i == 0 and hand[i].rank != hand[i + 1].rank):
                idx = 0
            elif (i == 2 and hand[i - 1].rank != hand[i].rank and hand[i].rank != hand[i + 1].rank):
                idx = 2
            elif (i == 3 and hand[i].rank != hand[i + 1].rank):
                idx = 4

        if (pair_count != 2):
            return 0

        # calculate rest of points due to lone element two pair
        points += hand[idx].rank + 3 * 15 ** 5

        return points

    # determine if a hand is one pair
    # takes as argument a list of 5 card objects
    # returns a number (points) for that hand
    def is_one_pair (self, hand):
        one_pair = False

        for i in range(len(hand) - 1):
            if (hand[i].rank == hand[i + 1].rank):
                one_pair = True
                if (i != 0):
                    # move pair to front of the list
                    hold = hand[0].rank
                    hand[0].rank = hand[i].rank
                    hand[i].rank = hold

                    hold = hand[1].rank
                    hand[1].rank = hand[i + 1].rank
                    hand[i + 1].rank = hold

                    # sort last three elements of the list
                    if hand[2].rank > hand[3].rank:
                        hold = hand[2].rank
                        hand[2].rank = hand[3].rank
                        hand[3].rank = hold

                    if hand[3].rank > hand[4].rank:
                        hold = hand[3].rank
                        hand[3].rank = hand[4].rank
                        hand[4].rank = hold
                break

        if (one_pair == False):
            return 0

        points = 2 * 15 ** 5 + hand[0].rank * 15 ** 4 + hand[1].rank * 15 ** 3
        points += hand[2].rank * 15 ** 2 + hand[3].rank * 15 + hand[4].rank

        return points



    # determine if a hand is one pair
    # takes as argument a list of 5 card objects
    # returns a number (points) for that hand
    def is_high_card (self, hand):
        high_card = hand[4].rank
        hands_total = 0
        for i in range(len(hand)):
            hands_total += hand[4 - i].rank * 15 ** (4 - i)
        points = hands_total + 1 * 15 ** 5

        return points



def main():
    # prompt the user to enter the number of players
    num_players = int(input('Enter the number of players: '))
    while ((num_players < 2) or (num_players > 6)):
       num_players = int(input('Enter the number of players: '))

    # create the Poker object
    game = Poker(num_players)

    # play the game - Poker
    game.play(game.is_royal, game.is_straight_flush, game.is_four_kind, game.is_full_house, game.is_flush, game.is_straight, game.is_three_kind, game.is_two_pair, game.is_one_pair, game.is_high_card)


# do not remove this line above main()
if __name__ == '__main__':
    main()
