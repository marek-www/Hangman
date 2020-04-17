# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 22:06:55 2020

@author: Marek
"""
import string, random

flag_win = False

def counter():
    
    while True:
        counter = input('How many mistakes?\n')
        try:
            cnt = int(counter)
            break
        except:
            print('Not a number')
            continue
    return cnt

def check_letter(key):
    
    global mistakes
    letter_list = string.ascii_lowercase
    
    while True:
        letter = input('\nChoose letter:\n')
        if letter in letter_list:
            break
        else:
            print('Not a letter')
            continue
        
    if letter in key:
        print('Correct!')     
    else:
        print('Wrong!')
        mistakes -= 1
        
    return letter
    
def show_letter(key, guess, answer):
    
    global flag_win
    for index, let in enumerate(key):
        if let == guess:
            answer[index] = guess
            key[index] = '*'

    for let_2 in answer:
        print(let_2, end = '')
    
    if key == list(len(key) * '*'):
        flag_win = True
 
def random_word():

    with open ('Hangman_wordlist.txt', 'r') as file:
        wordlist = file.read().split(', ')
    
    word = random.choice(wordlist)
    return word   
    
def game():
    
    key_list = list(random_word())
    ans = list(len(key_list) * '*')
    print(f'Your word has {len(key_list)} letters')
    
    while mistakes > 0:
        guessed_letter = check_letter(key_list)
        print(f'Attempts remaining: {mistakes}')    
        show_letter(key_list, guessed_letter, ans)
        if flag_win:
            print('\nCongratulations! You won!')
            break
        if not flag_win and mistakes == 0:
            print('\nYou loose!')

mistakes = counter()        
game()






