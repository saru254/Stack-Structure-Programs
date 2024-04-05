class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            raise IndexError("pop from empty stack")


def delimiters(expr):
    stack = Stack()
    errors = 0

    for pos, letter in enumerate(expr):
        if letter in "{[(":
            stack.push(letter)
        elif letter in "}])":
            if stack.isEmpty():
                print("Error:", letter, "at position", pos,
                      "has no matching left delimiter")
                errors += 1
            else:
                left = stack.pop()
                if not (left == "{" and letter == "}" or
                        left == "[" and letter == "]" or
                        left == "(" and letter == ")"):
                    print("Error:", letter, "at position", pos,
                          "does not match left delimiter", left)
                    errors += 1

    if stack.isEmpty() and errors == 0:
        print("Delimiters balance in expression", expr)
    elif not stack.isEmpty():
        print("Expression missing right delimiters for", stack)


expr = input("Expression to check: ")
delimiters(expr)
