#7. El sucesor del conjunto A es el conjunto A ∪ {A}. Encuentra los sucesores de los siguientes
#conjuntos:

#a) {1, 2, 3}
a = {1, 2, 3}
subset_a = frozenset(a)

union = a.union({subset_a})
print (union)

#b) {∅, {∅}}

a = {frozenset(), frozenset({frozenset()})}
subset_a = frozenset(a)

union = a.union({subset_a})
print(union)
