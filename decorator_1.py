
#Decorators Problems:
# Problem 1:
#You are given some information about  people. Each person has a first name, last name, age and sex.
#Print their names in a specific format sorted by their age in ascending order 
#i.e. the youngest person's name should be printed first.
#For two people of the same age, print them in the order of their input.


import operator

t = int (input())

sorted_list = []
for i in range(t):
	j = list( input().split() )
	sorted_list.append (j)
    
byage = operator.itemgetter(2)
sorted_list = sorted (sorted_list, key = byage)

for human in sorted_list:
	if human[3] == 'M':
		s = "Mr."
	else:
		s = "Ms."
	print(s, human[0], human[1])