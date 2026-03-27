print('Hel"l')

# print('Hel'l')<- error invalid syntax

print("Hr'sh")
# print('Hel"l")<- error invalid syntax

# We can use triple inverted commas for big strings

message='abcfgabdedfj'
print(len(message))# gives length of sring

print(message[1])# at particular pos char

print(message[:2])# we include the the position at the left of colon and exclufe the pos after colon

print(message.lower())
print(message.upper())

print(message.count('a'))
print(message.find('a'))#  guives 0  <-where the word or charcter appered first (or starts) in string 
print(message.find('bc')) # gives 1
msg='Hello world'
msg=msg.replace('world','universe')
print(msg)#-> Hello universe

greeting='Hello'
name='mike'
final_msg='{},{}. Welcome'.format(greeting,name)
print(final_msg) #-> Hello,mike. Welcome
final_msg_2=f'{greeting},{name}. Welcome'
print(final_msg_2)#-> Hello,mike. Welcome