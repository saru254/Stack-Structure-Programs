class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from empty stack")

def reverse_word(word):
    stack = Stack()
    reversed_word = ''

    # Push each character of the word onto the stack
    for char in word:
        stack.push(char)

    # Pop characters from the stack to reverse the word
    while not stack.is_empty():
        reversed_word += stack.pop()

    return reversed_word

# Get user input
word_to_reverse = input("Enter a word to reverse: ")

# Call the function to reverse the word
reversed_word = reverse_word(word_to_reverse)

# Print the reversed word
print("Reversed word:", reversed_word)
