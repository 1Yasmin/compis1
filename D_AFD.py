from Thompson import joinList
import copy

def nullable(node, c1=0, c2=0):
    if(node == "3" and node == "*"):
        return True
    elif(node == "|"):
        return nullable(c1) or nullable (c2)
    elif (node  == "."):
        return nullable(c1) and nullable (c2)
    else:
        return False

def firstpos(node, c1=0, c2=0, arbol=0, pos=0):
    print("node, ", node, "c1", c1, "c2", c2)
    if(node == "3"):
        print("3")
        return []
    elif(node == "|"):
        print(joinList(c1, c2))
        return joinList(c1, c2)
    elif (node  == "."):
        print(arbol[pos])
        print(c1,c2)
        if(nullable(arbol[pos])):
            print(joinList(c1,c2))
            return joinList(c1,c2)
        else:
            print(c1)
            return c1
    elif(node == "*"):
        print(c1)
        return c1
    else:
        print(node)
        return [node]

def lastpos(node):
    if(node == "3"):
        return []
    elif(node == "|"):
        return joinList(lastpos(c1),lastpos(c2))
    elif (node  == "."):
        if(nullable(c2)):
            return joinList(firstpos(c1),firstpos(c2))
        else:
            return lastpos(c2)
    elif(node == "*"):
        return lastpos(c1)
    else:
        return [node]


def D_DFA(arbol):
    complete_tree = copy.copy(arbol)
    for node in arbol:
        if(node == "|"):
            arbol.remove("|")
    
    pos_nodes = 0
    pos = 0
    for node in complete_tree:
        if (node != "*" and node != "|" and node != "."):
            complete_tree[pos] = [node, pos_nodes, [pos_nodes], [pos_nodes]]
            pos_nodes += 1
        pos +=1
        
    pos = 0
    for node in complete_tree:
        print(">>>>>>",node)
        print(pos)
        print("wow", complete_tree[pos])
        print(complete_tree[pos-1])
        if (node == "*"):
            if (complete_tree[pos-1][0] == "|"):
                complete_tree[pos] = [node, complete_tree[pos-1][1]]
            else:
                complete_tree[pos] = [node, firstpos(node, complete_tree[pos-1][2])]
        elif (node == "."):
            if(complete_tree[pos-1][0] == "*"):
                complete_tree[pos] = [node, firstpos(node, complete_tree[pos-1][1], complete_tree[pos-2][2], complete_tree[pos-1], 1)]
            elif(complete_tree[pos-2][0] == "|" or complete_tree[pos-2][0] == "*"):
                complete_tree[pos] = [node, firstpos(node, complete_tree[pos-1][2], complete_tree[pos-2][1], complete_tree[pos-1], 1)]
            else:
                complete_tree[pos] = [node, firstpos(node, complete_tree[pos-1][2], complete_tree[pos-2][2]), complete_tree[pos-1], 1]
        elif (node == "|"):
            if(complete_tree[pos-1][0] == "." or complete_tree[pos-1][0] == "*"):
                complete_tree[pos] = [node, firstpos(node, complete_tree[pos-1][1], complete_tree[pos-2][2], arbol, pos)]
            elif(complete_tree[pos-2][0] == "." or complete_tree[pos-2][0] == "*"):
                complete_tree[pos] = [node, firstpos(node, complete_tree[pos-1][2], complete_tree[pos-2][1])]
            else:
                complete_tree[pos] = [node, firstpos(node, complete_tree[pos-2][2], complete_tree[pos-1][2])]
        print(complete_tree)
        pos += 1
    
    for a in complete_tree:
        print(a)
    # Computing followpos
    pos = 0
    """
    for node in arbol:
        if(node == "."):
            for a in lastpos(arbol[pos-2]):
                followpos(a) = joinList(followpos(a), firstpos(c2))
        elif(node == "*"):
            for a in lastpos(arbol[pos]):
                followpos(a) = joinList(followpos(a), firstpos(node))
    """


