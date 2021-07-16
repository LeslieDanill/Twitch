# Automate the Boring Stuff With Python #
# Learning Concepts #

'''
# --- Five Times --- #
print('My name is')
i = 0

for i in range(5):

while i < 5:
    print('Jimmy Five Times ' + str(i))
    i = i + 1

# --- YourName --- #
name = ''
while True:
    print('Please type your name')
    name = input()
    if name == 'your name':
            break
print('Thank you!')

# --- SysExit --- #
import sys
print('Hello')
sys.exit()
print('Goodbye')

# --- Total --- #
total = 0
for num in range(101):
    total = total + num
print(total)

# --- Lists --- #
spam = 100
print(spam // 1)
# : says I am the walrus
# := crag says careful this walrus will bite
print(spam:=1)
print(spam)
spam = 'spam'
print(spam.index('p'))

listoflists = [[5,4,3,2,1], [1,2,3,4,5], [1,0], [0,1], [1,0,3]]
listofboolean = [True, False, False, True]
multitypelist = [1,'one',[1,'one'], True]

#False=0 True=1
listofboolean.sort()
print(str(listofboolean))
print(str(True))
print(int(True))
print(str(listofboolean[0]))

sortedlob = sorted(listofboolean)
print(sortedlob)

listoflists.sort()
print(listoflists)

multitypelist.sort()
print(multitypelist)

appendtest = [1,2,3,4]
appendtest.append(5)
print(appendtest)
#Doing this prints None
appendtest = appendtest.append(6)
print(appendtest)

spam = [0, 1 , 2, 3, 4]
print(type(spam))
spam = 0
print(type(spam))
spam = "zero"
print(type(spam))
print(spam)

# --- Dictionaries & Tuples --- #

spam = {'key1': 'one', 'key2': 'two', 'key3': 'three'}
print(type(spam))

print(spam.keys())
print(list(spam.keys()))
print(list(spam.values()))
print(list(spam.items()))


for k in spam.keys():
    print(k)

for v in spam.values():
        print(str(v))

for k, v in spam.items():
    print(k, v)

for i in spam.items():
    print(i)

print('one' in spam.values())


# Validate Dict items the long way
if 'key1' in spam:
    print(spam['key1'])
# OR the short way ...
    print(spam.get('key1',''))

# Set Dict Defaults the long way
if 'key1' not in spam:
    spam['key1'] = 'one'
    print(spam['key1'])
# OR the short way
    print(spam.setdefault('key1','one'))

# --- Character Counting Program --- #

message = "It was a bright, cold day in April and the clocks were striking thirteen."
count = {}

for character in message.lower():
    #if exists, increment by +1
    if count.get(character):
        count[character] += 1
    #else, create a key eg. 'a' & set default value to 1
    else:
        count[character] = 1

print(count)

# --- Alternate Version Character Counting Program (MrSpaar_) --- #

message = 'Some Text'                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
count = {}

for char in message.lower():
    count[char] = count.get(char, 0) + 1
'''


















