
class Automata:
    # Initializer / Instance Attributes
    def __init__(self):
        self.states = []
        self.symbols = []
        self.initial_state = []
        self.final_states = []
        self.transitions  = []

    def set_final(self, arr):
        self.final_states = arr
    
    def set_inicial(self, arr):
        self.initial_state = arr

    def set_transitions(self, arr):
        self.transitions = arr
    
    def add_transitions(self, arr):
        self.transitions.append(arr)
    
    def set_states(self, arr):
        self.states = arr
    
    def set_symbols(self, arr):
        self.symbols = arr

    def add_state(self, state):
        self.states.append(state)
    
    def add_finalState(self, state):
        self.final_states.append(state)
    
    def add_symbol(self, symbol):
        self.symbols.append(symbol)
    
    def sub_finaState(self, factor):
        for a in self.final_states:
            self.final_states[self.final_states.index(a)] = a+factor
    
    def sub_states(self, factor):
        for a in self.states:
            self.states[self.states.index(a)] = a+factor
    
    def sub_trans_states(self, factor):
        for a in self.transitions:
            a[0] = a[0] +factor
            a[1] = a[1] +factor
