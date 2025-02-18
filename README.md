# Territory Analysis Project

## Overview
This project is developed for the "Fundamentals of Programming" course and aims to analyze a rectangular territory composed of vertical and horizontal paths. The intersections of these paths may or may not be occupied by mountains, forming chains of mountains and valleys.

## Features
The program provides functionalities to:
- Validate and represent territories and intersections.
- Identify mountain chains and valleys.
- Retrieve adjacency and connectivity information.
- Calculate the number of mountains, mountain chains, and valley sizes.

## Territory Representation
- The territory is represented as a tuple of tuples, where each inner tuple represents a vertical path and contains integers (0 for free intersections and 1 for mountains).
- Each intersection is represented as a tuple (Vertical Path, Horizontal Path).

## Implemented Functions
### Territory and Intersection Functions
- `eh_territorio(arg)`: Checks if the given argument is a valid territory.
- `obtem_ultima_intersecao(t)`: Returns the top-rightmost intersection of the territory.
- `eh_intersecao(arg)`: Checks if the argument is a valid intersection.
- `eh_intersecao_valida(t, i)`: Checks if an intersection is valid within a given territory.
- `eh_intersecao_livre(t, i)`: Checks if an intersection is free (not occupied by a mountain).
- `obtem_intersecoes_adjacentes(t, i)`: Returns a tuple of valid adjacent intersections.
- `ordena_intersecoes(tup)`: Sorts intersections according to reading order.
- `territorio_para_str(t)`: Converts the territory into a human-readable string format.

### Mountain Chains and Valleys Functions
- `obtem_cadeia(t, i)`: Returns all connected intersections forming a chain.
- `obtem_vale(t, i)`: Returns all intersections forming a valley of a given mountain.

### Territory Information Functions
- `verifica_conexao(t, i1, i2)`: Checks if two intersections are connected.
- `calcula_numero_montanhas(t)`: Counts the number of mountains in the territory.
- `calcula_numero_cadeias_montanhas(t)`: Counts the number of mountain chains.
- `calcula_tamanho_vales(t)`: Calculates the total size of all valleys.

## Execution Instructions
1. Ensure you have Python 3 installed.
2. Run the Python script: `python FP2324P1.py`
3. Use the defined functions to analyze a given territory.

