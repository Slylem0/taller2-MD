#2. Indicar la cardinalidad de los siguientes conjuntos

def cardinalidad(set):
    contador = 0
    for i in set:
        contador += 1
    return contador

def set_3():
    global set3
    set3 = set()
    for i in range(-9, 46):
        if i % 2 == 0:
                set3.add(i)
        else:
             continue
    return set3

def set_4():
    global set4
    set4 = set()
    for i in range(20, 201):
        if (i % 3 == 0) or (i % 5 == 0):
            set4.add(i)
        else:
            continue
    return set4
    

if __name__ == "__main__":
    a = " the cardinilaty is: "
    b = """D) {x | 20 ≤ x ≤ 200 y x es multiplo de 3 o 5 } """

    set_a = {frozenset(), frozenset({frozenset()})}
    print ("a) {∅, {∅}} " + a + str(cardinalidad(set_a)))

    set_b = {frozenset(), frozenset({frozenset()}), 
             (frozenset(), frozenset({frozenset()}))}
    print ("b) {∅, {∅}, {∅, {∅}}}" + a + str(cardinalidad(set_b)))

    set_3()
    print ("c) {x | −9 ≤ x ≤ 45 y x es par }  " + a   + str(cardinalidad(set3)))

    set_4()
    print (b + a + str(cardinalidad(set4)))

