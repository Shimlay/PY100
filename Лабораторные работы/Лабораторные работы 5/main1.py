from pprint import pprint
# TODO решить с помощью list comprehension и распечатать его
numbers = []
for i in range(16):
    number = {"dec": i, "bin": bin(i), "oct": oct(i), "hex": hex(i)}
    numbers.append(number)
pprint(numbers)
