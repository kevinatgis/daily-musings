# simulation of monty hall paradox
# try using sets instead
from random import randint

switch_win = 0
stay_win  = 0
doors = {}

def init(x):
	x['door1'] = 'goat'
	x['door2'] = 'goat'
	x['door3'] = 'goat'

def cadillac(x):
	x['door'+str(randint(1,3))] = 'cadillac'

def host_chooses

for i in range(10000):
	init(doors)
	cadillac(doors)
	
	player_choice = 'door'+str(randint(0,2))

	host_goat = [x for x in goats if x != player_choice]
	if doors[player_choice] == 'cadillac':
		stay_win+=1



stay_win = (stay_win/10000.0)*100 # formatting
print('Stay %: {0:.2f}%'.format(stay_win))

'''
if player_choice == cadillac:								# player chooses the cadillac
	host_goat = goats[randint(0,1)]							# host chooses one of the two goats left
else:														# if player chooses a goat door
	

if player_choice == cadillac:
	stay_win+=1
elif:
	host_offers == cadillac: 
'''