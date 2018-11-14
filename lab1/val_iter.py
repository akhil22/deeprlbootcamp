import numpy as np, numpy.random as nr
import os
class MDP(object):
    def __init__(self, P, nS, nA, desc=none):
        self.P = P
        self.nS = nS
        self.nA = nA
        self.desc = desc
def main():
    F = open("input.txt", "r")
    i = 0
    P = []
    num_states = 0
    num_actions = 0
    for line in F.readlines():
        if i == 0:
            num_states = int(line)
        elif i == 1:
            num_actions = int(line)
        else :

        i = i+1

    print(num_states)
    print(num_actions)
if __name__=="__main__":
    main()
