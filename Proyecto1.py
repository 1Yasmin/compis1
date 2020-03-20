"""
   Entrada de datos
   *** Implementación de Thompson

   Construcción de NFA --> Simulación (si o no de una cadena w)
   
   Contrucción de subconjuntos
        Tabla con:    NFA | DFA  | Variables....
    Construcción de AFD dada r
    Graficar el AFD

    Simulación de AFD --> (si o no de una cadena w)
    
    Extra:  Minimización de los AF

    Imprimir para cada AF generado a partir de r, 
        -un SÍ o NO según si la cadena pertenece al lenguaje
    Tiempo que tarda cada AF en realizar la validacion de una cadena
    -Generar archivo por cada AF con 
            -Estados, simbolos, inicio, acepación, transcisión
"""

import os
import numpy as np
from copy import deepcopy
import time
from graphviz import Digraph
from Thompson import Thompson
from DFA import createDFA
from graph import graficar 
from D_AFD import D_DFA


class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]
        
def infixTopostfix(exp):

    mod = exp[0]
    for i in range(1,len(exp)):
        if( (((exp[i].isalpha() or exp[i].isdigit()) and exp[i-1] != '(') or exp[i] == '(') and (exp[i-1] != '|' or exp[i-1] == ')') ):
            mod += '.'+exp[i]
        else:
            mod += exp[i]

    regex = mod
    prec = {}
    prec["?"] = 4
    prec["*"] = 4
    prec["+"] = 4
    prec["."] = 3
    prec["|"] = 2
    prec["("] = 1
    tokens = list(regex)
    output = []
    stack = Stack()
    for token in tokens:
        if (token.isalpha() or token.isdigit() or token == ' '):
            output.append(token)
        elif (token == '('):
            stack.push(token)
        elif (token == ')'):
            top = stack.pop()
            while(top != '('):
                output.append(top)
                top = stack.pop()
        else:
            while (not stack.isEmpty()) and (prec[stack.peek()] >= prec[token]):
                  output.append(stack.pop())
            stack.push(token)
    while(not stack.isEmpty()):
        output.append(stack.pop())
    
    return ''.join(output)

if __name__== "__main__":
    exp = input("Expresión regular: ")
    regex = ""
    for v in exp:
        if v == "+" or v == "?":
            if(exp[exp.index(v)-1] == ")"):
                inicio = exp.index(v)-1
                pos = exp[exp.index(v)-1]
                while (pos != "("):
                    pos = exp[inicio]
                    inicio -= 1
                values = exp[inicio+1:exp.index(v)]
                if (v == "+"):
                    new_regex = exp[:exp.index(v)] + values + "*"+ exp[exp.index(v)+1:] 
                elif (v == "?"):
                    new_regex = exp[:exp.index(v)-(len(values)-1)] + values + "|3)"+ exp[exp.index(v)+1:] 
                exp = new_regex
            else:
                val = exp[exp.index(v)-1]
                if (v == "+"):
                    new_regex = exp[:exp.index(v)] + val + "*"+ exp[exp.index(v)+1:]  
                elif(v == "?"):
                    new_regex = exp[:exp.index(v)-1] +"(" + exp[exp.index(v)-1] + "|3)"+ exp[exp.index(v)+1:]
                exp = new_regex
    
    if(("+" not in exp) and ("?" not in exp)):
        regex = exp

    postfix = infixTopostfix(regex)
    #print(postfix)
    tokens = []
    for a in postfix:
        tokens.append(str(a))
    print(tokens)
    #Stack general
    
    #Contrucción del NFA 
    countState = 0
    if(len(tokens) == 1):
        tokens, countState = Thompson(tokens, countState)
    while(len(tokens) > 1):
        tokens, countState = Thompson(tokens, countState)

    # Automata generado
    Aut = tokens[0]
    
    # Guardar NFA en un archivo
    file = open("NFA.txt", "w")
    file.write("Estado inicial:  "+ str(Aut.initial_state)+"\n")
    file.write("Estado(s) de aceptación:  "+ str(Aut.final_states)+"\n")
    file.write("Estados:  "+ str(Aut.states)+"\n")
    file.write("Símbolos:  "+ str(Aut.symbols)+"\n")
    file.write("Transiciones:  "+ str(Aut.transitions)+"\n")
    file.close()
    # Graficar NFA
    graficar(Aut.final_states, Aut.transitions, "NFA")
    #print("NFA: ", Aut.initial_state, "\n", Aut.final_states, "\n", Aut.states, "\n", Aut.symbols, "\n", Aut.transitions, "\n")
    
    # Del AFN a AFD
    AFD = createDFA(Aut)
    #print("En proyecto DFA: ", "\n estado incial: ", AFD.initial_state, "\n","Estado final: ", AFD.final_states, "\n", "Estados", AFD.states, "\n", "Simbolos", AFD.symbols, "\n","Transiciones", AFD.transitions, "\n")
    
    # Guardar AFD en un archivo
    file = open("AFD.txt", "w")
    file.write("Estado inicial:  "+ str(AFD.initial_state)+"\n")
    file.write("Estado(s) de aceptación:  "+ str(AFD.final_states)+"\n")
    file.write("Estados:  "+ str(AFD.states)+"\n")
    file.write("Símbolos:  "+ str(AFD.symbols)+"\n")
    file.write("Transiciones:  "+ str(AFD.transitions)+"\n")
    file.close()
    # Graficar AFD
    graficar(AFD.final_states, AFD.transitions, "AFD")
    
    """
    #Construccion de AFD directo
    tokens.append("#")
    tokens.append(".")
    print(tokens)
    D_DFA(tokens)
    """