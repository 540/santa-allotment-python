# El Huerto de Santa Claus

<p align="center">
    <img src="_images/santa.jpeg" alt="Error al añadir un número repetido en una columna" style="width:400px"/>
</p>

## Instrucciones

Santa Claus quiere aumentar el número de árboles de Navidad que tiene en su huerto.

- Santa quiere plantar **N** árboles de Navidad en su huerto.
- Su huerto siempre es un cuadrado de **N** parcelas por **N** parcelas.
- Una parcela puede contener un árbol de Navidad.

Sin embargo, debido a su estructura radicular, estos árboles no crecerán si hay otro árbol alineado **horizontal**, **vertical** o **diagonalmente** con el árbol.

Dado un tamaño de parcela **N**, intenta encontrar una solución válida para colocar los **N** árboles en el huerto. Si no hay una solución válida, devuelve un array vacío.

### Salida válida - Ejemplo n=4
```
-0--
---0
0---
--0-
```

### Salida válida - Matriz vacía
```
[]
```

### Salida inválida - Ejemplo n=4
```
0---
--0-
0---
--0-
```
```
--0-
0---
-0--
---0
```

