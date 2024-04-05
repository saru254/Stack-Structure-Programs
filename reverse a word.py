#a program to reverse a word

#from SimpleStack import *

stack = Stack(100)   #create a stack to hold the letters

word = input("Word to reverse: ")

for letter in Word:  #loop over letters in word
    if not stack.isFull(): #push letters on stack if not full
        stack.push(letter)
reverse = ''   #build the reversed  version by popping the stack untill empty
while not stack.isEmpty(): 
    reverse += stack.pop()

print('the reverse of', word, 'is', reverse)