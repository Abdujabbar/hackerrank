__author__ = 'abdujabbor'

s = ""
os = []
inputs = []
deletes = []
q = int(input())

commands = []
for x in range(q):
    values = input().split()
    command = int(values[0])

    if command == 1:
        s += values[1]
        inputs.append(values[1])
        commands.append(command)
        pass
    elif command == 2:
        deletes.append(s[len(s) - int(values[1]):])
        s = s[:len(s) - int(values[1])]
        commands.append(command)
        pass
    elif command == 3:
        print(s[int(values[1]) - 1])
    else:
        latest_command = commands.pop()
        if latest_command == 1:
            linput = inputs.pop()
            s = s[:len(s) - len(linput)]
            pass
        else:
            s = s + deletes.pop()
