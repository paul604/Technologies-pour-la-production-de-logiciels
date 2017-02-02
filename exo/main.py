import sys

from premier import estPremier

userInput = input('Choisissez un nombre : ')

n = int(userInput)

if estPremier(n) :
    print("{} est un nombre premier".format(n))
else :
    print("{} n'est pas un nombre premier".format(n))