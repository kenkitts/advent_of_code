"""Solution for day 3, part 1 puzzle on adventofcode.com"""

inputList = []
with open("day3/input.txt","r") as f:
    for line in f:
        inputList.append(line)

xMax = int(len(inputList[0])-1)

def slope(xIncrement, yIncrement):
    posX = 0
    posY = 0
    trees = 0

    while posY < len(inputList):
        if inputList[posY][posX] == "#":
            trees += 1
        posX += xIncrement
        posY += yIncrement
        if posX >= xMax:
            posX -= xMax

    return trees

print("Part 1: "+str(slope(3,1)))
print("Part 2: "+str((int(slope(1,1)) * (int(slope(3,1))) * (int(slope(5,1))) * (int(slope(7,1))) * (int(slope(1,2))))))
