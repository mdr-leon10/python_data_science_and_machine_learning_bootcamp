
# Excercise nu. 1
print('exc # 1')
print(7**4)

# Excercise nu. 2
print('exc # 2')
s = "Hi there Sam!"
l = list(s.split())
print (l)

# Excercise nu. 3
print('exc # 3')
planet = "Earth"
diameter = 12742
print(" The diameter of {} is {} kilometers".format(planet, diameter))

# Excercise nu. 4
print('exc # 4')
lst = [1,2,[3,4],[5,[100, 200,["hello"]],23,11],1,7]
print(' ' + str(lst[3][1][2][0]))

# Excercise nu. 5
print('exc # 5')
d = {'k1' : [1,2,3, {'tricky': ['oh', 'man', 'inception', {'target' : [1,2,3,'hello']}]}]}
hello = d['k1'][3]['tricky'][3]['target'][3]
print(' ' + hello)

# Excercise nu. 6
print('exc # 6')
def domain (email):
	return email.split('@')[1]
print(' ' + str(domain('user@domain.com')))

# Excercise nu. 7
print('exc # 7')
def isThereDog (string):
	st = string.lower()
	return 'dog' in st
print(' ' + str(isThereDog('This dog runs faster than the other dog dude!'))) 

# Excercise nu. 8
print('exc # 8')
def countDog (string):
	st = string.split()
	count = 0
	for el in st:
		if el.lower() == 'dog':
			count +=1
	return count
print(' ' + str(countDog('This dog runs faster than the other dog dude!'))) 

# Excercise nu. 9
print('exc # 9')
seq = ['soup','dog','salad','cat','great']
l=list((filter(lambda word : 's' == word[0], seq)))
print (l)

# Excercise nu. 10
print('exc # 10')
def whatTicket (speed, birthday):
	noTicket = 60
	littleTicket = 61
	bigTicket = 80

	if(birthday):
		if (speed <= (noTicket + 5)):
			return 'No Ticket'
		elif (speed >= (littleTicket + 5) and speed <= (bigTicket + 5)):
			return 'Small ticket'
		else:
			return 'Big Ticket'

	else:
		if (speed <= (noTicket)):
			return 'No Ticket'
		elif (speed >= (littleTicket) and speed <= (bigTicket)):
			return 'Small ticket'
		else:
			return 'Big Ticket'

print(whatTicket(81, True))
print(whatTicket(81, False))