inputList = []
with open("input.txt","r") as f:
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