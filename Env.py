import random

def buildMap(x,y):
    env = []
    for i in range(x):
        row = []
        for j in range(y):
            row.append({})
        env.append(row)
    return env

def placeRandomThings(env, density, key, val):
    x = len(env)
    y = len(env[0])
    numToPlace = (x * y) * density
    print "placing", numToPlace
    for i in range(int(numToPlace)):
        pX = random.randint(0,x-1)
        pY = random.randint(0,y-1)
        env[pX][pY][key] = val
    return env


