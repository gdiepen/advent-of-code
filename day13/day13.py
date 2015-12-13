import itertools
import re



seatingHappinessInfo = {}

allPersons = []

with open('input-day13.txt') as f:
	for line in f:
		person1, _, direction, valuestr, _, _, _, _, _, _, person2 = re.split(" " , line.rstrip().replace('.' , ''))
		value = int(valuestr)
		signMultiplier=1
		if direction == "lose":
			signMultiplier = -1

		seatingHappinessInfo[ person1 + person2 ] = (signMultiplier * value)
		
		if person1 not in allPersons:
			allPersons.append(person1)
		

#Part 1
bestHappiness = None
bestSeating = []
for permutation in itertools.permutations(allPersons):
	totalHappiness = 0
	s=0
	while s < (len(permutation) -1):
		if ( permutation[s] + permutation[s+1] ) in seatingHappinessInfo.keys():
			totalHappiness += seatingHappinessInfo[ permutation[s] + permutation[s+1] ] 
		if ( permutation[s+1] + permutation[s] ) in seatingHappinessInfo.keys():
			totalHappiness += seatingHappinessInfo[ permutation[s+1] + permutation[s] ] 
		s+=1
			
	if ( permutation[0] + permutation[-1] ) in seatingHappinessInfo.keys():
		totalHappiness += seatingHappinessInfo[ permutation[0] + permutation[-1] ] 
	if ( permutation[-1] + permutation[0] ) in seatingHappinessInfo.keys():
		totalHappiness += seatingHappinessInfo[ permutation[-1] + permutation[0] ] 
	
	if totalHappiness > bestHappiness:
		bestHappiness = totalHappiness
		bestSeating = permutation
print bestSeating
print bestHappiness




#Part 2
for p in allPersons:
	seatingHappinessInfo[ p + 'Guido' ] = 0
	seatingHappinessInfo[ 'Guido' + p ] = 0
allPersons.append('Guido')



bestHappiness = None
bestSeating = []
for permutation in itertools.permutations(allPersons):
	totalHappiness = 0
	s=0
	while s < (len(permutation) -1):
		if ( permutation[s] + permutation[s+1] ) in seatingHappinessInfo.keys():
			totalHappiness += seatingHappinessInfo[ permutation[s] + permutation[s+1] ] 
		if ( permutation[s+1] + permutation[s] ) in seatingHappinessInfo.keys():
			totalHappiness += seatingHappinessInfo[ permutation[s+1] + permutation[s] ] 
		s+=1
			
	if ( permutation[0] + permutation[-1] ) in seatingHappinessInfo.keys():
		totalHappiness += seatingHappinessInfo[ permutation[0] + permutation[-1] ] 
	if ( permutation[-1] + permutation[0] ) in seatingHappinessInfo.keys():
		totalHappiness += seatingHappinessInfo[ permutation[-1] + permutation[0] ] 
	
	if totalHappiness > bestHappiness:
		bestHappiness = totalHappiness
		bestSeating = permutation
print bestSeating
print bestHappiness
