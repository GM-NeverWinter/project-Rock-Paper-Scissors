"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""
# By [GM]NeverWinter  

import random

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def __init__(self):
        self.my_move = moves
        self.their_move = random.choice(moves)

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move


# Human
class humanPlayer(Player):
    def move(self):
        choice = input("Show your move (rock/paper/scissors): ")
        while choice.lower() not in moves:
            print("Invalid move...")
            choice = input("Show your move (rock/paper/scissors): ")
        return choice.lower()


# A player that always plays 'rock'
class rockPlayer(Player):
    def move(self):
        return "rock"


# A player that chooses its moves randomly.
class randomPlayer(Player):
    def move(self):
        return random.choice(moves)


# A player that remembers and imitates
# what the human player did in the previous round.
class reflectPlayer(Player):
    def move(self):
        return self.their_move


# A player that cycles through the three moves
class cyclePlayer(Player):
    def move(self):
        if self.my_move == moves[0]:
            return moves[1]
        elif self.my_move == moves[1]:
            return moves[2]
        else:
            return moves[0]


class Game:

    def beats(self, one, two):
        return ((one == 'rock' and two == 'scissors') or
                (one == 'scissors' and two == 'paper') or
                (one == 'paper' and two == 'rock'))

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1_score = 0
        self.p2_score = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()

        print(f"Player 1: {move1}  || Player 2: {move2}")

        # Condition
        if move1 == move2:
            print("Tie !!")
        elif self.beats(move1, move2):
            self.p1_score += 1
            print("Player 1 wins!")
        else:
            self.p2_score += 1
            print("Player 2 wins!")

        # Print result
        print(f"Score: {self.p1_score} - {self.p2_score} \n")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        # Start
        print("Game start!")

        # define round
        rounds = input("How many round you want to play: ")
        while not rounds.isnumeric():
            print("Invalid input...")
            rounds = input("How many round you want to play: ")

        # Looping game
        for round in range(int(rounds)):
            print(f"Round {round + 1}:")
            # Round play
            self.play_round()

        # Final Score
        print(f"Final Score: {self.p1_score} - {self.p2_score}")
        if self.p1_score > self.p2_score:
            print("Player 1 wins!")
        elif self.p1_score < self.p2_score:
            print("Player 2 wins! ")
        else:
            print("Wow! Ties !!")
        # Ending
        print("Game over!")


if __name__ == '__main__':
    human = humanPlayer()
    # Bot select
    bot_list = [randomPlayer(), reflectPlayer(),
                rockPlayer(), cyclePlayer()]

    game = Game(human, random.choice(bot_list))
    game.play_game()
