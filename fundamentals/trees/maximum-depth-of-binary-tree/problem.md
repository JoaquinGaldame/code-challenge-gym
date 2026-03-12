# Maximum Depth Of Binary Tree

## English
Given the root of a binary tree, return its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Implement `solve(data)` in `python/solution.py`, where `data` is either `None` or a dictionary with the shape:
- `val`: node value
- `left`: left child or `None`
- `right`: right child or `None`

### Example
- Input: `{"val": 3, "left": {"val": 9, "left": null, "right": null}, "right": {"val": 20, "left": {"val": 15, "left": null, "right": null}, "right": {"val": 7, "left": null, "right": null}}}`
- Output: `3`

## Espanol
Dada la raiz de un arbol binario, devuelve su profundidad maxima.

La profundidad maxima es la cantidad de nodos a lo largo del camino mas largo desde la raiz hasta la hoja mas lejana.

Implementa `solve(data)` en `python/solution.py`, donde `data` es `None` o un diccionario con la forma:
- `val`: valor del nodo
- `left`: hijo izquierdo o `None`
- `right`: hijo derecho o `None`
