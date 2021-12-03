file = open('input.txt', 'r')
lines = file.readlines()


def function(prefix, common):
    rowCount = 0
    oneCount = 0
    finalRow = ''

    for line in lines:
        row = line.strip()

        if row.startswith(prefix):
            rowCount += 1
            finalRow = row

            if len(prefix) == len(row):
                return row

            if row[len(prefix)] == '1':
                oneCount += 1
        
    if rowCount == 1:
        return finalRow
    else:
        newPrefix = prefix
        if oneCount >= (rowCount / 2.0):
            newPrefix += ('1' if common else '0')
        else:
            newPrefix += ('0' if common else '1')
        return function(newPrefix, common)

print('Final:')
print(int(function('', True), 2) * int(function('', False), 2))