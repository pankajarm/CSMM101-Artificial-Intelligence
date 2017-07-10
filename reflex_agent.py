# An example of reflex agent, here it's a vaccum agent which react based
# upon actions present in lookup table
def VaccumAgent(location, state):

    action = ['suck', 'right', 'left']
    if state == 'dirty':
        return action[0]
    elif location == 'A':
        return action[1]
    else:
        return action[2]


if __name__ == '__main__':
    print (VaccumAgent('A', 'dirty'))
    print (VaccumAgent('A', 'clean'))
    print (VaccumAgent('B', 'dirty'))
    print (VaccumAgent('B', 'clean'))
