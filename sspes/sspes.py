import random
import json
import playerHandeling as ph

rpsls = {'rock': 0, 'spock': 1, 'paper': 2, 'lizard': 3, 'scissors': 4}
list_keys = list(rpsls.keys())
jsonfile = 'player_data.json'



def getString(my_input):
    for s in list_keys:
        if list_keys[list(rpsls.values()).index(my_input)] == s:
            return list_keys[list(rpsls.values()).index(my_input)]
    return 'not valid'

def checkWinner(comp_choice, player_choice, player_name):
    stats = [0,0,0,1]
    difference = (comp_choice - player_choice) % 5
    if(difference == 0):
        stats[2] = 1
        print('draw\n')
    elif( difference == 1 or difference == 2 ):
        stats[1] = 1
        print( "Computer wins!\n")
    elif ( difference == 4 or difference == 3 ):
        stats[0] = 1
        print( "Player wins!\n")
    ph.updateStats(player_name, jsonfile, stats, player_choice)
    
    
def playerSelection():
    while(True):
        player_sel = input('Do you want to create/select/delete/list a player?(c/s/d/l):')
        
        if player_sel == 'c':
            player_sel = input('Please input name:')
            if not ph.exists(player_sel, jsonfile):
                ph.create(player_sel, jsonfile)
                print('Have fun ' + player_sel + '\n\n\n')
                return player_sel
            else:
                print('That player already exists, please create another one or choose a player that already exists.')
                
        elif player_sel == 's':
            player_sel = input('Please choose a player:')
            if ph.exists(player_sel, jsonfile):
                print('Have fun ' + player_sel + '\n\n\n')
                return player_sel
            else:
                print('Please choose a player that already exists or create a new player!') 
                
        elif player_sel == 'd':
            player_sel = input('Please choose a player:')
            if ph.exists(player_sel, jsonfile):
                conformation = input('To Confirm please type (DELETE):')
                if conformation == 'DELETE':
                    ph.delete(player_sel, jsonfile)
                    print('You succesfully deleted player ' + player_sel)
            else:
                print('Player does not exist')
                
        elif player_sel == 'l':
            player_sel = input('Chose a player you would like to select (name/all):')
            ph.getPlayers(player_sel, jsonfile)
            
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
            comp_num = ph.compChoice(curr_player, jsonfile)
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