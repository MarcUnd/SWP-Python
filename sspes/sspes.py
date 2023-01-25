import random
import json
import playerHandeling as ph
import requests
from termcolor import colored

rpsls = {'rock': 0, 'spock': 1, 'paper': 2, 'lizard': 3, 'scissors': 4}
list_keys = list(rpsls.keys())
url = 'http://127.0.0.1:5000/'



def getString(my_input):
    for s in list_keys:
        if list_keys[list(rpsls.values()).index(my_input)] == s:
            return list_keys[list(rpsls.values()).index(my_input)]
    return 'not valid'

def checkWinner(comp_choice, player_choice, player_name):
    stats = 0
    difference = (comp_choice - player_choice) % 5
    if(difference == 0):
        stats = 2
        print(colored('draw\n','yellow'))
    elif( difference == 1 or difference == 2 ):
        stats = 1
        print(colored('Computer wins!\n', 'red'))
    elif ( difference == 4 or difference == 3 ):
        stats = 0
        print(colored('Player wins!\n', 'green'))
    r = requests.get(url=url+'update', params={'name':player_name, 'win': stats, 'choice': player_choice})
    
    
def playerSelection():
    while(True):
        player_sel = input('What do you want to do? ("h" or "help" for help):').lower()
        
        if player_sel == 'c':
            player_sel = input('Please input name:')
            if requests.get(url=url+player_sel).json()['name'] == player_sel:
                print(colored('This player exist already!', 'red'))
            else:
                requests.post(url = url + player_sel)
                print(colored('Have fun ' + player_sel + '\n\n\n', 'green'))
                return player_sel
        
        elif player_sel == 's':
            player_sel = input('Please choose a player:')
            if requests.get(url=url+player_sel).json()['name'] == player_sel:
                print(colored('Have fun ' + player_sel + '\n\n\n', 'green'))
                return player_sel
            else:
                print(colored('Please choose a player that already exists or create a new player!', 'red')) 
                
        elif player_sel == 'd':
            player_sel = input('Please choose a player:')
            if str(requests.get(url=url+player_sel).json()['name']) == player_sel:
                conformation = input('To Confirm please type (DELETE):')
                if conformation.upper() == 'DELETE':
                    requests.delete(url=url+player_sel)
                    print(colored('You succesfully deleted player ' + player_sel, 'green'))
                else:
                    print(colored('Input not Valid, Player still exists!', 'yellow'))
            else:
                print(colored('Player does not exist!', 'red'))
                
        elif player_sel == 'l':
            player_sel = input('Chose a player you would like to select (name/all):')
            r = requests.get(url=url+player_sel)
            data = r.json()
            if player_sel == 'all':
                for d in data:
                    print(colored(str(d) + '\n', 'magenta'))
            else:
                print(colored(str(data), 'magenta'))
            print('\n')
            
        elif player_sel in ['exit', 'leave', 'bye','e']:
            print(colored('goodbye', 'light_red'))
            quit()
            
        elif player_sel in ['h', 'help']:
            print('You have the following options:\n')
            print('Press "c" to create a player.\nPress "s" to select a player.\nPress "d" to delete a player.\nPress "l" to list Players.\n')
            print('You can leave the game by typing "exit", "leave", "bye" or "e".\n')
        
        else:
            print(colored('Input not valid!', 'red'))



def game(curr_player):
    while(True):
        player_in = input('What`s your next move? (type "help" or "h" for help):')
        if player_in in list_keys or player_in in ['0', '1', '2', '3', '4']:
            if player_in in list_keys:
                player_num = rpsls[player_in]
                player_in = player_in
            else:
                player_num = int(player_in)
                player_in = getString(int(player_in))
                
            print('Player-Choice: ' + player_in)
            comp_num = int(requests.get(url=url+'ai-choice/'+curr_player).json())
            print('AI-Choice: ' + getString(comp_num) + '\n')
            
            checkWinner(comp_num, player_num, curr_player)
            
        elif player_in in ['exit', 'leave', 'bye','e']:
                print(colored('goodbye\n', 'light_red'))
                quit()
        elif player_in in ['log out', 'logout', 'lo']:
            print(colored('see you soon\n\n', 'light_green'))
            break
        elif player_in in ['h', 'help']:
            print('You have the following options:\n')
            print('Play the game by choosing a number between 0 and 4 (rock= 0, spock= 1, paper= 2, lizard= 3, scissors= 4)\
                or by typing the name of the symbol you want to choose.\n')
            print('You can log out and select a new player by typing "logout", "log out" or "lo".\n')
            print('You can leave the game by typing "exit", "leave", "bye" or "e".\n')
        else:
            print(colored('\nInput not valid!\n', 'red'))
            

def main():
    while(True):
        curr_player = playerSelection()
        game(curr_player)
    


if __name__=='__main__':
    main()