import random
import json
import playerHandeling as ph
import requests

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
        print('draw\n')
    elif( difference == 1 or difference == 2 ):
        stats = 1
        print( "Computer wins!\n")
    elif ( difference == 4 or difference == 3 ):
        stats = 0
        print( "Player wins!\n")
    r = requests.get(url=url+'update', params={'name':player_name, 'win': stats, 'choice': player_choice})
    
    
def playerSelection():
    while(True):
        player_sel = input('Do you want to create/select/delete/list a player?(c/s/d/l):')
        
        if player_sel == 'c':
            player_sel = input('Please input name:')
            requests.post(url = url + player_sel)
            print('Have fun ' + player_sel + '\n\n\n')
            return player_sel
        elif player_sel == 's':
            player_sel = input('Please choose a player:')
            if str(requests.get(url=url+player_sel) == player_sel):
                print('Have fun ' + player_sel + '\n\n\n')
                return player_sel
            else:
                print('Please choose a player that already exists or create a new player!') 
                
        elif player_sel == 'd':
            player_sel = input('Please choose a player:')
            if str(requests.get(url=url+player_sel) == player_sel):
                conformation = input('To Confirm please type (DELETE):')
                if conformation == 'DELETE':
                    requests.delete(url=url+player_sel)
                    print('You succesfully deleted player ' + player_sel)
            else:
                print('Player does not exist')
                
        elif player_sel == 'l':
            player_sel = input('Chose a player you would like to select (name/all):')
            r = requests.get(url=url+player_sel)
            data = r.json()
            for d in data:
                print(d)
            
        elif player_sel in ['exit', 'leave', 'bye','e']:
            print('goodbye')
            quit()



def game(curr_player):
    while(True):
        player_in = input('What you gonna do? (rock= 0, spock= 1, paper= 2, lizard= 3, scissors= 4):')
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
                print('goodbye')
                quit()
        elif player_in in ['log out', 'logout', 'lo']:
            print('see you soon')
            break
        else:
            print('\ntry again!\n')
            

def main():
    while(True):
        curr_player = playerSelection()
        game(curr_player)
    


if __name__=='__main__':
    main()