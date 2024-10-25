# a) {a,b, {a,b}}

set_a = {"a", "b", ("a", "b")}
print(f"Conjunto original: {set_a}")
total = len(set_a)
potencia = 2 ** total


list_a = list(set_a)

for i in range(potencia):
    subset = []
    for j in range(total):
        if i & (1 << j):
            subset.append(list_a[j])
    print(subset)

print ("___________________________________________")
#b) {∅,a, {a}, {{a}}}
set_a = [frozenset(), "a", ("a"), (("a"))]
print(f"Conjunto original: {set_a}")
total = len(set_a)
potencia = 2 ** total


list_a = list(set_a)

for i in range(potencia):
    subset = []
    for j in range(total):
        if i & (1 << j):
            subset.append(list_a[j])
    print(subset)

print ("_____________________________________________")
set_a = [frozenset()]
print(f"Conjunto original: {set_a}")
total = len(set_a)
potencia = 2 ** total


list_a = list(set_a)

for i in range(potencia):
    subset = []
    for j in range(total):
        if i & (1 << j):
            subset.append(list_a[j])
    print(subset)
