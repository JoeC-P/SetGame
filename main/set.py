"""
Author: Joseph Chilson-Purvis
GitHub: JoeC-P
File: set.py
This is the code that will create a set game.
Will include code to shuffle and start a new game.
"""


"""
creates the dictionary representation of a Set deck
precondition: nothing
postcondition: a dictionary containing the 81 elements of a Set deck
returns: the dictionary containg the deck
"""
def createSetDeck():
    setDeck = {} # dictionary of numbers 1 - 81 as the key
                 # and the D = Z_3 x Z_3 x Z_3 x Z_3 representation
                 # of each card
    x = 1
    for y in range(0,3):
        for z in range(0,3):
            for w in range(0,3):
                for v in range(0,3):
                    setDeck[x] = (y,z,w,v)
                    x += 1
    return setDeck

"""
finds final element that would complete the D-set of two cards
parameters:
x - a card tuple (q,w,e,r)
y - a card tuple (t,o,u,i)
returns the card that would complete the D-set
"""
def findDset(x,y):
    xy = []
    # xy = (2(s1 + s2)mod3, 2(c1 + c2)mod3), 2(n1 + n2)mod3, 2(f1 + f2)mod3)
    for i in range(0,4): 
        xy.append(2*(x[i]+y[i]) % 3)
    return xy[0], xy[1], xy[2], xy[3]


setDeck = createSetDeck()
print(setDeck[1])
print(setDeck[1])
print(findDset(setDeck[1], setDeck[1]))
    



