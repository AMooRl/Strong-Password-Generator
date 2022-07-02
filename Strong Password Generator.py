import string
import random

s1 = list(string.ascii_lowercase)
s2 = list(string.ascii_uppercase)
s3 = list(string.digits)
s4 = list(string.punctuation)

caracters_number = input ('How Many Caracters for the Password?: ')

while True:
    try:
        caracters_number = int(caracters_number)
        if caracters_number < 6 :
            print ('you need at last 6 caracters')
            caracters_number = input ('please enter the Number again: ')
        else:
            break
    except:
        print ('Please enter numbers only')
        caracters_number = input ('How Many Caracters for the Password?: ')

random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)

part1 = round (caracters_number * (30/100))
part2 = round (caracters_number * (20/100))


password = []

for i in range(part1):
    password.append(s1[i])
    password.append(s2[i])

for i in range(part2):
    password.append(s3[i])
    password.append(s4[i])

random.shuffle(password)

password = ''.join(password[0:])

print (password)