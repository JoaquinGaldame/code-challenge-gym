# Number Of Recent Calls

## English
You are given a sequence of ping times in milliseconds. For each ping time `t`, return how many calls happened in the inclusive range `[t - 3000, t]`.

Implement `solve(data)` in `python/solution.py`, where `data` is a list of integers representing ping times in increasing order.

Return a list where each position contains the number of recent calls after processing that ping.

### Example
- Input: `[1, 100, 3001, 3002]`
- Output: `[1, 2, 3, 3]`

## Espanol
Se te da una secuencia de tiempos de ping en milisegundos. Para cada tiempo `t`, devuelve cuantas llamadas ocurrieron dentro del rango inclusivo `[t - 3000, t]`.

Implementa `solve(data)` en `python/solution.py`, donde `data` es una lista de enteros con tiempos de ping en orden creciente.

Devuelve una lista donde cada posicion contiene la cantidad de llamadas recientes luego de procesar ese ping.
