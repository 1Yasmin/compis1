from Automata import *

def joinList(lista_a, lista_b):
    new_list = lista_a
    for element in lista_b:
        if(element not in lista_a):
            new_list.append(element)
    return new_list

def Thompson(tokens, countStates):
    for token in tokens:
        if(token == "*"):
            countStates +=1
            A1 = tokens[tokens.index(token)-1]
            A1.set_final([countStates])
            A1.add_state(countStates-1)
            A1.add_state(countStates)
            A1.set_symbols(joinList(A1.symbols,["3"]))
            A1.sub_trans_states(1)
            A1.add_transitions([A1.initial_state[0], A1.initial_state[0]+1, "3"])
            A1.add_transitions([A1.final_states[0]-1, A1.final_states[0], "3"])
            A1.add_transitions([A1.initial_state[0], A1.final_states[0], "3"])
            A1.add_transitions([A1.final_states[0]-1, A1.initial_state[0]+1 , "3"])
            tokens.pop(tokens.index(token)-1)
            tokens[tokens.index(token)] = A1
            countStates +=1
            #print(A1.initial_state, A1.final_states, A1.states, A1.symbols, A1.transitions)
            return tokens, countStates
        elif(token == "."):
            A1 = tokens[tokens.index(token)-2]
            A2 = tokens[tokens.index(token)-1]
            # Cambios en los estados del segundo autómata
            if (A1.final_states != A2.initial_state):
                A2.set_inicial(A1.final_states)
                A2.sub_finaState(-1)
                A2.sub_states(-1)
                A2.sub_trans_states(-1)
                countStates -=1
            #print(A1.initial_state, A1.final_states, A1.states, A1.symbols, A1.transitions)
            #print(A2.initial_state, A2.final_states, A2.states, A2.symbols, A2.transitions)
            #Creación del nuevo autómata
            Aut = Automata()
            Aut.set_inicial(A1.initial_state)
            Aut.set_final(A2.final_states)
            Aut.set_states(joinList(A1.states, A2.states))
            Aut.set_symbols(joinList(A1.symbols, A2.symbols))
            Aut.set_transitions(joinList(A1.transitions, A2.transitions))
            #print(Aut.initial_state, Aut.final_states, Aut.states, Aut.symbols, Aut.transitions)
            tokens.pop(tokens.index(token)-1)
            tokens.pop(tokens.index(token)-1)
            tokens[tokens.index(token)] = Aut
            return tokens, countStates
        elif(token == "|"):
            countStates +=1
            A1 = tokens[tokens.index(token)-2]
            A2 = tokens[tokens.index(token)-1]
            Aut = Automata()
            Aut.set_inicial(A1.initial_state)
            Aut.set_final([countStates])
            Aut.set_states(joinList(A1.states, A2.states))
            Aut.add_state(countStates-1)
            Aut.add_state(countStates)
            Aut.set_symbols(joinList(A1.symbols, A2.symbols))
            Aut.set_symbols(joinList(Aut.symbols,["3"]))
            A1.sub_trans_states(1)
            A2.sub_trans_states(1)
            Aut.set_transitions(joinList(A1.transitions, A2.transitions))
            Aut.add_transitions([Aut.initial_state[0], A1.initial_state[0]+1 , "3"])
            Aut.add_transitions([Aut.initial_state[0], A2.initial_state[0]+1 , "3"])
            Aut.add_transitions([A1.final_states[0]+1, Aut.final_states[0], "3"])
            Aut.add_transitions([A2.final_states[0]+1, Aut.final_states[0] , "3"])
            #Actualizar array
            tokens.pop(tokens.index(token)-1)
            tokens.pop(tokens.index(token)-1)
            tokens[tokens.index(token)] = Aut
            countStates +=1
            #print("Creacion", Aut.initial_state, Aut.final_states, Aut.states, Aut.symbols, Aut.transitions)
            return tokens, countStates
        elif(isinstance(token, str)):
            Aut = Automata()
            Aut.add_symbol(token)
            Aut.set_inicial([countStates])
            countStates +=1
            Aut.set_final([countStates])
            countStates +=1
            Aut.set_states([Aut.initial_state[0], Aut.final_states[0]])
            Aut.add_transitions([Aut.initial_state[0],Aut.final_states[0] ,token])
            tokens[tokens.index(token)] = Aut
            #print("Creacion", Aut.initial_state, Aut.final_states, Aut.states, Aut.symbols, Aut.transitions)
            return tokens, countStates
        

        
