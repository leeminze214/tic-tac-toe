import pygame
import time
import user
import bot
import random


class bk_end_board:
    def __init__(self):
        self.turns = 0

        self.board = [[" ", " ", " "]
            , [" ", " ", " "]
            , [" ", " ", " "]]
        self.symbols = {"one": False, "two": False, "three": False, "four": False, "five": False, "six": False,
                        "seven": False, "eight": False, "nine": False}

    def taken_or_not(self, row, col):
        if self.board[row][col] == ' ':
            return "empty"

    def fill(self, row, col, sym):
        self.board[row][col] = sym

    def update_status_sym(self, key):
        self.symbols[key] = True

    def full_board(self):
        for i in range(3):
            for a in range(3):
                if self.board[i][a] == " ":
                    return False
                return True

    def random_first(self):
        half = random.choice([1, 2])
        if half == 1:
            user.Bob.first_turn = True
        else:
            bot.Bot.first_turn = True

    # switches turns with booleans
    def Turns(self):
        if user.Bob.first_turn:
            if self.turns % 2 == 0:
                self.swch_to_user()
            else:
                self.swch_to_bot()
        else:
            if self.turns % 2 == 0:
                self.swch_to_bot()
            else:
                self.swch_to_user()


    def swch_to_user(self):
        bot.robot.turn = False
        user.Bob.turn = True

    def swch_to_bot(self):
        bot.robot.turn = True
        user.Bob.turn = False


'''             
        elif bot.robot.first_turn:
            if self.turns % 2 == 0:
                self.swch_to_bot()
            else:
                self.swch_to_user()
'''

# def check_result(self):


Board = bk_end_board()
