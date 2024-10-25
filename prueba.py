from matplotlib_venn import venn2
import matplotlib.pyplot as plt

# Ejemplo de conjuntos
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Crear el diagrama de Venn
venn2([set1, set2], set_labels=('Set 1', 'Set 2'))

# Mostrar el diagrama
plt.show()
