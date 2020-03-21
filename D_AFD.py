from Thompson import joinList
from Automata import *
import copy

def nullable(arbol, node):
    #print(arbol[node][1])
    if(arbol[node][1] == "3" or arbol[node][1]== "*"):
        return True
    elif(arbol[node][1] == "|"):
        return nullable(arbol, node-2) or nullable (arbol, node-1)
    elif (arbol[node][1]  == "."):
        return nullable(arbol, node-2) and nullable (arbol, node-1)
    else:
        return False

def firstpos(arbol, node):
    if(arbol[node][1] == "3"):
        return []
    elif(arbol[node][1] == "|"):
        return joinList(firstpos(arbol, node-2), firstpos(arbol, node-1))
    elif (arbol[node][1] == "."):
        if(nullable(arbol, node-2)):
            return joinList(firstpos(arbol, node-2), firstpos(arbol, node-1))
        else:
            return firstpos(arbol, node-2)
    elif(arbol[node][1] == "*"):
        return firstpos(arbol, node-1)
    else:
        return [arbol[node][2]]

def lastpos(arbol, node):
    if(arbol[node][1] == "3"):
        return []
    elif(arbol[node][1] == "|"):
        return joinList(lastpos(arbol, node-2), lastpos(arbol, node-1))
    elif (arbol[node][1] == "."):
        if(nullable(arbol, node-1)):
            return joinList(lastpos(arbol, node-2), lastpos(arbol, node-1))
        else:
            return lastpos(arbol, node-1)
    elif(arbol[node][1] == "*"):
        return lastpos(arbol, node-1)
    else:
        return [arbol[node][2]]

def followpos(arbol, node):
    if (arbol[node][1] == "*"):
        for i in arbol[node][3]:
            for h in arbol:
                if h[2] == i:
                    if(len(h) == 6):
                        arbol[h[0]][5] = joinList(h[5], firstpos(arbol, node))
                    else:
                        arbol[h[0]].append(firstpos(arbol, node))
    elif(arbol[node][1] == "."):
        for i in lastpos(arbol, node-2):
            for h in arbol:
                if h[2] == i:
                    if(len(h) == 6):
                        arbol[h[0]][5] = joinList(h[5], firstpos(arbol, node-1))
                    else:
                        arbol[h[0]].append(firstpos(arbol, node-1))


def D_DFA(arbol):
    complete_tree = copy.copy(arbol)

    # Tabla base con fistpos y lastpos de cada nodo importante y 3
    pos_nodes = 0
    pos = 0
    for node in complete_tree:
        if (node != "*" and node != "|" and node != "."):
            if(node == "3"):
                complete_tree[pos] = [pos, node, [], []]
            else:
                complete_tree[pos] = [pos, node, pos_nodes, [pos_nodes], [pos_nodes]]
            pos_nodes += 1
        else:
            complete_tree[pos] = [pos, node]
        pos +=1

    # Firstpos y lastpos de cada nodo
    pos = 0
    for node in complete_tree:
        if (node[1] == "*" or node[1] == "." or node[1] == "|"):
            complete_tree[pos] = [pos, complete_tree[pos][1], firstpos(complete_tree, pos), lastpos(complete_tree, pos)]
        pos += 1

    # Followpos
    for node in complete_tree:
        followpos(complete_tree, node[0])

    print("******** Table ALL************")
    print("id\tSymbol\tPos n\tfirstpos\tlastpos\tfollowpos")
    for a in complete_tree:
        if(len(a) == 6):
            print(a[0],"\t",a[1],"\t",a[2],"\t\t",a[3],"\t",a[4],"\t",a[5])
        elif(len(a) == 5):
            print(a[0],"\t",a[1],"\t",a[2],"\t\t",a[3],"\t",a[4],"\t"," --")
        elif(len(a) == 4):
            print(a[0],"\t",a[1],"\t",a[2],"\t\t",a[3],"\t","--","\t"," --")
        else:
            print(a[0],"\t",a[1],"\t",a[2],"\t\t","--","\t","--","\t"," --")


    print("******** Table DFA************")
    print("Symbol\tPos n\tfirstpos\tlastpos\tfollowpos\t")
    table = []
    symbols = []
    for a in complete_tree:
        if (isinstance(a[2], int)):
            if(a[1] != "#"):
                if a[1] not in symbols:
                    symbols.append(a[1])
            table.append(a)

    for a in table:
        if(len(a) == 6):
            print(a[1],"\t",a[2],"\t",a[3],"\t",a[4],"\t",a[5],"\t")
        else:
            print(a[1],"\t",a[2],"\t",a[3],"\t",a[4],"\t"," --")

    # Creando el nuevo automata
    Aut = Automata()
    states = []
    if (len(complete_tree[len(complete_tree)-1]) == 4):
        initial = complete_tree[len(complete_tree)-1][2]
    else:
        initial = complete_tree[len(complete_tree)-1][4]

    states.append(initial)
    Aut.set_inicial(initial)  
    Aut.set_symbols(symbols)  
    print("Inicial", initial)
    count_states = 0
    while count_states < len(states):
        for sim in symbols:
            temp_state = []
            for pos in states[count_states]:
                for a in table:
                    if(a[2] == pos):
                        if(sim == a[1]):
                            temp_state = joinList(temp_state, a[5])
            if (temp_state not in states):
                states.append(temp_state)
                Aut.add_transitions([count_states, len(states)-1 ,sim])
            else:
                pos = states.index(temp_state)
                Aut.add_transitions([count_states, pos,sim])
        count_states +=1
    
    for st in states:
        for a in table:
            if (a[1] == "#"):
                if a[2] in st:
                    pos = states.index(st)
                    Aut.add_finalState(pos)

    all_states = list(range(0,count_states))
    Aut.set_states(all_states)
    
    return Aut


