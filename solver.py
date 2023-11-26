from pprint import pprint
import requests
import os
import string
import subprocess, sys
from formater import *


black = ''
black_list = []
yellow = '.....'
yellow_list= []
green = '.....'
green_list = []
color = []
MAX_TRYS = 6
ACCEPTABLE_COLORS = {'B','Y','G'}


for _ in range(MAX_TRYS):

    # Imput a 5 letter guess and color-code the letters
    
    while True:
        guess = input("input a 5 letter word: ").upper()
        if len(guess) == 5 and guess.isalpha():
            break
    for i in range(len(guess)):
        while True:
            print("Enter G for green, Y for yellow or B for black or gray")
            color = input(f"color for {guess[i]} ").upper()
            if color not in ACCEPTABLE_COLORS:
                print("Entry must be either upper or lower 'G' , 'B' or 'Y'")
            if color in ACCEPTABLE_COLORS:
                break
        if color == 'B': # Enter a 'b' for dark gray or black letters
            black_list.append((guess[i], i)) # List of tuples
        elif color == 'Y': # Enter a 'y' for yellow letters
            yellow_list.append((guess[i], i)) # List of tuples
        elif color == 'G': # Enter a 'g' for green letters
            green_list.append((guess[i], i)) # List of tuples
        else:
            print("color must be 'B', 'Y' or 'G'")
            break

    green = format_green(green_list)

    yellow = format_yellow(yellow_list)

    black = format_black(black_list)

    perl_string = green.lower() + yellow.lower() + black.lower() + ' and print'
    with open('match.pl', 'w') as file:
        file.write('#!/usr/bin/perl -wnl\n')
        file.write('#\n')
        file.write(perl_string)
    file.close()

#    perl_script = subprocess.Popen(["./match.pl","solutions.txt"])
    perl_script_output = subprocess.check_output(["./match.pl","solutions.txt"])
    decoded_output = perl_script_output.decode("utf-8").replace('\n', ' ')
    print()
    print(decoded_output)
    print()
