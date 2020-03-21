from Automata import *
from DFA import *
        
def nextState(s,sim,trans):
    for a in trans:
        if a[0] == s and a[2] == sim:
            return a[1]

    return False

def simulacionAutomataDFA(Aut, exp):
    s = Aut.initial_state[0]
    trans = Aut.transitions
    c = 0
    while(c < len(exp)):
        s = nextState(s,exp[c],trans)
        if(s != False):
            c += 1
        else:
            return "No"
    if(s in Aut.final_states):
        return "Yes"
    else:
        return "No"

def simulacionAutomataNFA(Aut, exp):
    s = e_closure(Aut, Aut.initial_state)
    c = 0
    while(c < len(exp)):
        if(len(move(Aut, s, exp[c])) != 0):
            s = e_closure(Aut, move(Aut, s, exp[c]))
            c += 1
        else:
            return "No"

    if(Aut.final_states[0] in s):
        return "Yes"
    else:
        return "No"