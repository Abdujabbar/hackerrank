class Person:
    _age = 0

    def __init__(self,initial_Age):
        self._age = initial_Age
        if self._age < 0:
            self._age = 0
        # Add some more code to run some checks on initial_Age

    def amIOld(self):
        if self._age <= 0:
            print("This person is not valid, setting age to 0.")
            print("You are young.")
        elif self._age > 0 and self._age < 13:
            print("You are young.")
        elif self._age < 18:
            print("You are a teenager.")
        else:
            print("You are old.")
        # Do some computations in here and print out the correct statement to the console

    def yearPasses(self):
        self._age += 1
        #self.amIOld()
        # Increment the age of the person in here


T = int(input())
for i in range(0, T):
    age = int(input())
    p = Person(age)
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()
    p.amIOld()
    print("")