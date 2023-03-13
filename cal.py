#Love calculator 

yourname = input('Enter your name \n')
hername = input('Enter her name \n')
combined = yourname + hername 
lowercased = combined.lower()
t = lowercased.count('t')
r = lowercased.count('r')
u = lowercased.count('u')
e = lowercased.count('e')


true = t+r+u+e

l = lowercased.count('l')
o = lowercased.count('o')
v = lowercased.count('v')
e = lowercased.count('e')

love = l+o+v+e

truelove =str(true) + str(love)

print(f'{truelove}% Love ' )


if (truelove < '10')  or (truelove > '90'):
    print(f'Like coke and mentos {truelove}')
elif (truelove >='40') and (truelove <='50'):
    print(f'You are alright together {truelove}')
else:
    print(f' Your score is :{truelove}%')

    

