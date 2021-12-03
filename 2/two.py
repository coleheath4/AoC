file = open('input.txt', 'r')
lines = file.readlines()

horizontal = 0
depth = 0
aim = 0

for line in lines:
    lineList = line.strip().split()
    if lineList[0] == 'forward':
        horizontal += int(lineList[1])
        depth += int(lineList[1]) * aim
    if lineList[0] == 'down':
        aim += int(lineList[1])
    if lineList[0] == 'up':
        aim -= int(lineList[1])

print(horizontal)
print(depth)
print(aim)
print(horizontal * depth)