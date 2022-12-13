import json
import heapq
import random

def create(player_name, outfile):
    #Reihenfolge der choices: rock, spock, paper, lizard, scissors
    player_dic = {'name': player_name, 'wins': 0, 'loss': 0, 'draw': 0, 'games': 0, 'ratio': 0, 'choices':[0,0,0,0,0]}
    with open(outfile, 'r') as out:
        data = json.load(out)
    data.append(player_dic)
    with open(outfile, 'w') as out:
        json.dump(data, out, indent=4, separators=(',',': '))


def exists(player_name, outfile):
    with open(outfile, 'r') as out:
        data = json.load(out)
    
    for d in data:
        if d['name'] == player_name:
            return True
    return False

def delete(player_name, outfile):
    with open(outfile, 'r') as out:
        data = json.load(out)
    for d in data:
        if d['name'] == player_name:
            i = data.index(d)
    data.pop(i)
    with open(outfile, 'w') as out:
        json.dump(data, out, indent=4, separators=(',',': '))

def getPlayers(player_name, outfile):
    with open(outfile, 'r') as out:
        data = json.load(out)
        
    if player_name in ['a', 'all']:
        for d in data:
            print('\n', d)
            
    elif exists(player_name, outfile):
        for d in data:
            if d['name'] == player_name:
                print('\n', d, '\n')
                
    else:
        print('Player does not exist!')

def updateStats(player_name, outfile, statsArr, choice):
    with open(outfile, 'r') as out:
        data = json.load(out)
    for d in data:
        if d['name'] == player_name:
            i = data.index(d)
    data[i]['wins'] += statsArr[0]
    data[i]['loss'] += statsArr[1]
    data[i]['draw'] += statsArr[2]
    data[i]['games'] += statsArr[3]
    data[i]['ratio'] = round(data[i]['wins'] / data[i]['games'], 3)
    data[i]['choices'][choice] += 1
    with open(outfile, 'w') as out:
        json.dump(data, out, indent=4, separators=(',',': '))


def compChoice(player_name, outfile):
    with open(outfile, 'r') as out:
        data = json.load(out)
    for d in data:
        if d['name'] == player_name:
            if d['games'] > 10:
                most_used = getHighestIndizes(d['choices'])
                if len(most_used) == 2:
                    best_choices = [(most_used[0]+1) % 5, (most_used[0]+2) % 5, (most_used[1]+1) % 5, (most_used[1]+2) % 5]
                    best_choices.sort()
                    print(best_choices)
                    if best_choices[1] == best_choices[2]:
                        return best_choices[1]
                    for i in range(len(best_choices)):
                        if best_choices[i] in most_used:
                            return best_choices[i]
                else:
                    return random.randrange(0, 4)
            else:
                return random.randrange(0, 4)
 

def getHighestIndizes(input_list):
    high = heapq.nlargest(2, input_list)
    high_index = [index for index in range(len(input_list)) if input_list[index] in high]

    return high_index
    

               