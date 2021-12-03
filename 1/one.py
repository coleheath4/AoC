file = open('input1.txt', 'r')
lines = file.readlines()

count = 0
previous = 0

for line in lines:
    if line.strip() > previous:
        count += 1
    previous = line.strip()

print(count)

count = 0
index = 0

for line in lines:
    if index > 1 and index < (len(lines) - 1):
        groupOne = int(lines[index].strip()) + int(lines[index - 1].strip()) + int(lines[index - 2].strip())
        groupTwo = int(lines[index + 1].strip()) + int(lines[index].strip()) + int(lines[index - 1].strip())

        if groupOne < groupTwo:
            count += 1
    index += 1

print(count)