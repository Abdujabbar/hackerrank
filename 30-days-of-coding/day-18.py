__author__ = 'abdujabbor'


class Palindrome:
    stack = []
    stack_index = 0
    queue = []

    def pushCharacter(self, ch):
        self.queue.append(ch)

    def enqueueCharacter(self, ch):
        self.stack.append(ch)
        self.stack_index += 1

    def popCharacter(self):
        return self.queue.pop()

    def dequeueCharacter(self):
        result = self.stack.pop(len(self.stack) - self.stack_index)
        self.stack_index -= 1
        return result


W = input()
# Create the Palindrome class object
p = Palindrome()

l = len(W)
# push all the characters of string s to stack
for i in range(l):
    p.pushCharacter(W[i])
# enqueue all the characters of string s to queue
for i in range(l):
    p.enqueueCharacter(W[i])
f = True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
'''
for i in range(l):
    poped = p.popCharacter()
    dequeued = p.dequeueCharacter()
    if poped != dequeued:
        f = False
        break
# finally print whether string s is palindrome or not.
if f:
    print("The word, " + W + ", is a palindrome.")
else:
    print("The word, " + W + ", is not a palindrome.")
