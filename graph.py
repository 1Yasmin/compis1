from graphviz import Digraph

def graficar(final_states, transitions, name):
    f = Digraph('finite_state_machine', filename=name)
    f.attr(rankdir='LR', size='8,5')

    f.attr('node', shape='doublecircle')
    for a in final_states:
        f.node(str(a))
    
    f.attr('node', shape='circle')
    for a in transitions:
        f.edge(str(a[0]), str(a[1]), label= str(a[2]))

    f.view()