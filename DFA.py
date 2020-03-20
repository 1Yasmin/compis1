from Automata import *

# Regresa un array de estados
def e_closure(Aut,states):
    trans = Aut.transitions
    new_state = states
    for s in states:
        for t in trans:
            if ((t[0] == s and t[2] == "3") and t[1] not in new_state):
                new_state.append(t[1])
    new_state.sort()
    return new_state

#Regresa un array de estados
def move(Aut, estados, simb):
    trans = Aut.transitions
    new_state = []
    for s in estados:
        for t in trans:
            if ((t[0] == s and t[2] == simb) and t[1] not in new_state):
                new_state.append(t[1])
    new_state.sort()
    return new_state

def createDFA(Autom):
    #Inicializando variables
    count_states = 0
    new_states =[]
    # Primer e-closure
    inicial = e_closure(Autom, Autom.initial_state)
    new_states.append(inicial)
    Aut = Automata()
    Aut.set_inicial([0])
    Symbols = Autom.symbols
    if ("3" in Symbols):
        Symbols.remove("3")
    Symbols.sort()
    Aut.set_symbols(Symbols)
    while count_states < len(new_states):
        for sim in Symbols:
            #print("simbolo: ", sim)
            temp = e_closure(Autom, move(Autom, new_states[count_states], sim))
            if(temp != []):
                if(temp in new_states):
                    #print("igual", temp, new_states)
                    pos = new_states.index(temp)
                    #print(pos)
                    Aut.add_transitions([count_states,pos,sim])
                else: 
                    #print("diferente", temp, new_states)
                    new_states.append(temp)
                    #print(count_states, len(new_states)-1)
                    Aut.add_transitions([count_states, len(new_states)-1,sim])
        count_states += 1
    
    for st in new_states:
        if Autom.final_states[0] in st:
            pos = new_states.index(st)
            Aut.add_finalState(pos)

    states = list(range(0,count_states))
    Aut.set_states(states)
    
    return Aut
