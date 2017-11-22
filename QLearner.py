import Env
import random

actions = ["up", "down", "left", "right"]

x = 8
y = 8

iterations = 10000
exploreRatio = 1


start = (0,0)
goal = (x-1,y-1)

site = Env.buildMap(8, 8)
site = Env.placeRandomThings(site, 0.1, "barrier", True)
site = Env.placeRandomThings(site, 0.2, "water", True)

def printMapPoorly(env):
    dx = len(env)
    dy = len(env[0])
    for i in range(dx):
        for j in range(dy):
            print env[i][j],
        print ""

def initializeRewardTable(x, y):
    reward = {}
    for i in range(x):
        for j in range(y):
            for k in actions:
                reward[(i,j,k)] = None
    return reward

printMapPoorly(site)

reward = initializeRewardTable(x,y)
#we could probably not intialize this


def computeReward(state):
    i = state[0]
    j = state[1]
    if "barrier" in site[i][j]:
        return -999
    else:
        return (goal[0] - i) + (goal[1] - j)

def getValidActions(i,j):
    act = []
    if i > 0:
        act.append("left")
    if i < x-1:
        act.append("right")
    if j < y-1:
        act.append("up")
    if j > 0:
        act.append("down")
    return act

def performMove(oldState, action):
    newPos = None
    i = oldState[0]
    j = oldState[1]
    if a == "up":
        newPos = (i, j+1)
    elif a == "down":
        newPos = (i, j-1)
    elif a == "left":
        newPos = (i-1, j)
    elif a == "right":
        newPos = (i+1, j)
    else:
        raise ValueError("UnknownAction")
    if newPos[0] < 0 or newPos[0] >= x or newPos[1] < 0 or newPos[1] >= y:
        raise ValueError("MovedOutOfBounds", newPos)
    return newPos


for step in range(iterations):
    at = start
    while at != goal:
        print at
        proposedAction = None
        validActions = getValidActions(at[0], at[1])
        if random.random() < exploreRatio:
            for a in validActions:
                if (at,a) not in reward:
                    proposedAction = a
        if proposedAction == None:
            maxVal = -float('inf')
            maxAction = None
            for a in validActions:
                if reward[at,a] > maxVal:
                    maxVal = reward[at,a]
                    maxAction = a
            proposedAction = maxAction
        if proposedAction == None:
            raise "NeverPickedAnAction"
        oldState = at
        newState = performMove(oldState, proposedAction)
        rew = computeReward(newState)
        reward[oldState, proposedAction] = rew
        at = newState