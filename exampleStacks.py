# Example of creating and using functions with Stacks

stack = []

# we use the append() built in already in Python as our push()
stack.append("Hello")
stack.append("World")
stack.append("Python")
stack.append("is")

print(stack)
#adds the word "awesome" to the right of the list or at the top of the stack
stack.append("awesome")

print(stack)
# we remove the word "awesome" since it's the one on top
stack.pop()

print(stack)
# we add a new word, being "boring" to the top
stack.append("boring")

print(stack)

#shows the size of the stack
print(len(stack))

