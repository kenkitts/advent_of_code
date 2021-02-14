from collections import defaultdict
from timeit import timeit
from pprint import pprint

map = dict()
cube_d = {'-x':0,'x':7,'-y':0,'y':7,'-z':0,'z':0}

with open('input.txt','rt') as file:
    for x,line in enumerate(file):
        for y,char in enumerate(line.strip("\n")):
            if char == '.':
                map.update({(x,y,0):False})
            else:
                map.update({(x,y,0):True})


def expand_cube(map,cube_d):
    for x in range(cube_d.get("-x") - 1,cube_d.get("x") + 2):
        for y in range(cube_d.get("-y") -1,cube_d.get("y") + 2):
            for z in range(cube_d.get("-z") -1,cube_d.get("z") + 2):
                if (x,y,z) in map:
                    continue
                else:
                    map[(x,y,z)] = False
    cube_d['-x'] -= 1
    cube_d['-y'] -= 1
    cube_d['-z'] -= 1
    cube_d['x'] += 1
    cube_d['y'] += 1
    cube_d['z'] += 1
    return map

def cycle(map,iterations=6):
    while iterations > 0:
        expand_cube(map,cube_d)
        new_map = dict()
        for i in map:
            x,y,z = i[0], i[1], i[2]
            active_neighbors = 0
            for xx in range(x-1, x+2):
                for yy in range(y-1,y+2):
                    for zz in range(z-1,z+2):
                        if (xx,yy,zz) == (x,y,z):
                            continue
                        if map.get((xx,yy,zz)) is True:
                            active_neighbors += 1
            if map.get((x,y,z)) is True:
                if active_neighbors == 2 or active_neighbors == 3:
                    new_map[(x,y,z)] = True
                else:
                    new_map[(x,y,z)] = False
            if map.get((x, y, z)) is False:
                if active_neighbors == 3:
                    new_map[(x,y,z)] = True
                else:
                    new_map[(x,y,z)] = False
        map = new_map.copy()
        iterations -= 1
    return map

map = cycle(map)

count = 0
for i in map.values():
    if i is True:
        count += 1

print(count)
