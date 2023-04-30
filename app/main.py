import random

print('''
 ad8888888888ba
 dP'         `"8b,
 8  ,aaa,       "Y888a     ,aaaa,     ,aaa,  ,aa,
 8  8' `8           "88baadP""""YbaaadP"""YbdP""Yb
 8  8   8              """        """      ""    8b
 8  8, ,8         ,aaaaaaaaaaaaaaaaaaaaaaaaddddd88P
 8  `"""'       ,d8""
 Yb,         ,ad8"    Normand Veilleux
  "Y8888888888P" 
  
  Project created to learn Python

''')
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "x", "y", "z"]

symbols = ["@", "!", "#", "$", "%", "&", "*", "(", ")", "%"]

num_of_letters = int(input("How many letters would you like in your password? \n"))

num_of_symbols = int(input("How many symbols would you like?"))

num_of_numbers = int(input("How many numers would you ike?"))

letter_counter = 0

array_of_password = []

for letter in range(1, num_of_letters + 1):
  selected_letter = random.choice(letters)
  is_capitalized = random.choice(range(0, 2))

  if is_capitalized == 0:
    array_of_password.append(selected_letter[0])
  else:
    array_of_password.append(selected_letter[0].upper())

for sym in range(1, num_of_symbols + 1):
  selected_symbol = random.choice(symbols)
  array_of_password.append(selected_symbol[0])

for num in range(1, num_of_numbers + 1):
  selected_number = random.choice(range(1, 10))
  array_of_password.append(selected_number)

array_of_answer = []

for n in array_of_password:
  array_of_answer.append(str(n))

random.shuffle(array_of_answer)

print(f"Here is your password: {''.join(map(str, array_of_answer))}")


