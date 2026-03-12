# Code Challenge Gym

![Python](https://img.shields.io/badge/Python-Algorithms-blue)
![JavaScript](https://img.shields.io/badge/JavaScript-Algorithms-yellow)
![Tests](https://img.shields.io/badge/tests-automated-green)

Code Challenge Gym es un repositorio para practicar algoritmos, estructuras de datos y preparación para entrevistas técnicas usando Python y JavaScript.

Code Challenge Gym is a repository designed for practicing algorithms, data structures, and technical interview preparation using Python and JavaScript.

---

# Objetivo del proyecto / Project Goal

Este repositorio funciona como un entorno de entrenamiento estructurado para:

- Reforzar pensamiento algorítmico
- Practicar estructuras de datos
- Preparar entrevistas técnicas
- Mantener una biblioteca personal de soluciones
- Validar soluciones mediante tests automatizados

This repository acts as a structured training environment for:

- Strengthening algorithmic thinking
- Practicing data structures
- Preparing for coding interviews
- Maintaining a personal algorithm reference library
- Validating solutions using automated tests

---

# Idea central / Core Concept

Cada ejercicio tiene dos pistas de trabajo:

- `starter`: espacio donde escribes tu propia solución
- `solution`: referencia oficial del repositorio

Esto permite practicar sin ver la solución hasta haber intentado resolver el problema.

Each exercise provides two tracks:

- `starter`: your workspace to implement the solution
- `solution`: the official reference implementation

This ensures you can practice without immediately seeing the reference answer.

---

# Estructura del repositorio / Repository Structure
- `fundamentals/`: problemas organizados por patron de entrevista
- `python/`: 100 ejercicios por nivel
- `javascript/`: 100 ejercicios por nivel
- `templates/`: archivos base para crear nuevos ejercicios
- `tools/`: scripts para crear ejercicios y ejecutar tests
- `docs/`: documentacion de uso y plan de estudio

# Estructura de cada ejercicio / Exercise Structure
### Python
- `problem.md`: enunciado
- `starter.py`: aqui practicas tu solucion
- `solution.py`: solucion oficial de referencia
- `test_starter.py`: test para validar tu intento
- `test_solution.py`: test para validar la referencia oficial

### JavaScript
- `problem.md`: enunciado
- `starter.js`: aqui practicas tu solucion
- `solution.js`: solucion oficial de referencia
- `test_starter.test.js`: test para validar tu intento
- `test_solution.test.js`: test para validar la referencia oficial


# Flujo de estudio recomendado / Recommended Study Flow
1. Entra al ejercicio y lee `problem.md`.
2. Resuelve el problema en `starter.py` o `starter.js`.
3. Ejecuta el test del `starter`.
4. Si tu intento falla, corrigelo y vuelve a probar.
5. Cuando termines, abre `solution.py` o `solution.js` y compara.
6. Si quieres verificar la referencia oficial, corre el test de `solution`.

Study workflow:

1. Read the problem
2. Implement your solution
3. Run tests
4. Fix failing cases
5. Compare with the reference solution
6. Analyze improvements

---


### Regla simple
- `starter` = lo haces tu
- `solution` = lo consultas despues

## Instalacion local
### Python
Python usa `unittest`, asi que no necesitas instalar dependencias extra.

### JavaScript
Instala dependencias una sola vez:
```bash
npm install
```

## Comandos mas utiles
### Ejecutar todas las soluciones oficiales
```bash
python tools/run_all_tests.py
```

### Ejecutar solo soluciones oficiales de Python
```bash
python tools/run_all_tests.py --python --track solution
```

### Ejecutar solo soluciones oficiales de JavaScript
```bash
python tools/run_all_tests.py --javascript --track solution
```

### Ejecutar todos tus starters de Python
```bash
python tools/run_all_tests.py --python --track starter
```

### Ejecutar todos tus starters de JavaScript
```bash
python tools/run_all_tests.py --javascript --track starter
```

Atencion: los `starter` estan pensados para que los completes tu. Si no implementas nada, esos tests van a fallar.

## Probar un ejercicio puntual
### Python starter
```bash
python tools/run_exercise.py --language python --track starter --path fundamentals/arrays/two-sum/python
```

### Python solution
```bash
python tools/run_exercise.py --language python --track solution --path fundamentals/arrays/two-sum/python
```

### JavaScript starter
```bash
python tools/run_exercise.py --language javascript --track starter --path fundamentals/arrays/two-sum/javascript
```

### JavaScript solution
```bash
python tools/run_exercise.py --language javascript --track solution --path fundamentals/arrays/two-sum/javascript
```

## Crear un ejercicio nuevo
### Python
```bash
python tools/create_exercise.py --language python --level beginner --name "binary search warmup"
```

### JavaScript
```bash
python tools/create_exercise.py --language javascript --level intermediate --name "graph traversal review"
```

## Que esta resuelto y que no
- Todos los ejercicios ya tienen estructura completa para practicar.
- No todas las `solution` contienen una solucion avanzada real todavia.
- Algunas si ya fueron resueltas como referencia completa.
- La separacion `starter` / `solution` ya queda preparada en todo el repositorio.

## Recomendación práctica / Practical Recommendation

Empieza por fundamentals/.
Resuelve en starter, ejecuta el test del starter y recién después compara con solution.

Start with fundamentals/.
Solve using starter, run the tests, and only afterwards compare with the solution.

---

## Autor / Author

### Repositorio personal de entrenamiento para mejorar continuamente en:

- Algoritmos
- Estructuras de datos
- Ingeniería de software
- Preparación para entrevistas técnicas

### Personal training repository maintained for continuous improvement in:

- Algorithms

- Data structures

- Software engineering

- Technical interview preparation

---

## LICENSE

MIT.

---

## Roadmap de entrenamiento / Training Roadmap

### Fundamentals
- Arrays
- Strings
- Hash Maps
- Stacks
- Queues
- Recursion
- Trees
- Graphs
- Dynamic Programming

### Code Challenges
- Beginner: 40 exercises
- Intermediate: 40 exercises
- Advanced: 20 exercises

---