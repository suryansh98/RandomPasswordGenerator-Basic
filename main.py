import random


def shuffle(string):
  tempList = list(string)
  random.shuffle(tempList)
  return ''.join(tempList)


upperCaseLetter1 = chr(random.randint(65,90))
upperCaseLetter2 = chr(random.randint(65,90))

lowerCaseLetter1 = chr(random.randint(97,122))
lowerCaseLetter2 = chr(random.randint(97,122))

digit1 = (random.randint(0,9))
digit2 = (random.randint(0,9))

symbol1 = chr(random.randint(32, 47))
symbol2 = chr(random.randint(32, 47))

password = upperCaseLetter1 + upperCaseLetter2 + lowerCaseLetter1 + lowerCaseLetter2 + str(digit1) + str(digit2) + symbol1 + symbol2

print(shuffle(password))
