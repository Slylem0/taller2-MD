import numpy as np

print ("__________________________Punto 1_________________________________")
#1. Determinar el valor de verdad de las siguientes sentencias
#a)     {2} ∈ {{2, {2}}}
set1 = np.array([(2)])
set2 = np.array([((2, (2)))])
is_present = set1 in set2
print (f"A. {2} ∈ {{2, {2}}}:", is_present)

#b)     {2} ∈ {{2}, {2, {2}}}
set1 = np.array([(2)])
set2 = [2, (2,(2))]
is_present = set1 in set2
print (f"B. {2} ∈ {2, {2, 2}}:", is_present)

#c) {2} ∈ {{{2}}}
set1 = [(2)]
set2 = [(((2)))]
is_present = set1 in set2
print (f"C. {2} ∈ {{{2}}}{2} ∈ {{{2}}}:", is_present)

#d) {∅} ⊂ {∅, {∅}}
set1 = {frozenset()}
set2 = {frozenset(), frozenset({frozenset()})}
is_present = set1.issubset(set2)
print ("D. {∅} ⊂ {∅, {∅}}{∅} ⊂ {∅, {∅}: " + str(is_present) )

#e) {{∅}} ⊂ {∅, {∅}}
set1 = {frozenset({frozenset()})}
set2 = {frozenset(), frozenset({frozenset()})}
is_present = set1.issubset(set2)
print ("E. {{∅}} ⊂ {∅, {∅}}: " + str(is_present))

#d) {{∅}} ⊂ {{∅}, {{∅}}}
set1 = {frozenset({frozenset()})}
set2 = {frozenset({frozenset()}), frozenset({frozenset({frozenset()})}) }
is_present = set1.issubset(set2)
print ("F. {{∅}} ⊂ {{∅}, {{∅}}}: " + str(is_present)) 
print ("___________________________________________________________")

#2. Indicar la cardinalidad de los siguientes conjuntos