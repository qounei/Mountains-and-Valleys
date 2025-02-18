Territory Explorer
Territory Explorer is a Python project developed as part of a university assignment for the Fundamentals of Programming course. The project focuses on analyzing and visualizing rectangular territories composed of vertical and horizontal paths. Each intersection in the territory can be either free or occupied by a mountain. The project provides various functions to explore the connections between intersections, identify mountain chains, and calculate valleys.

Features
Territory Validation: Check if a given structure represents a valid territory.

Intersection Operations: Validate intersections, check if they are free or occupied, and find adjacent intersections.

Chain and Valley Detection: Identify chains of connected mountains and the valleys associated with them.

Territory Visualization: Convert a territory into a human-readable string representation.

Statistical Analysis: Calculate the number of mountains, mountain chains, and the total size of valleys in a territory.

Usage
To use the Territory Explorer, simply import the provided functions into your Python script. Below are some examples of how to use the main functionalities:

Validating a Territory
python
Copy
from FP2324P1 import eh_territorio

territory = ((0, 1, 0, 0), (0, 0, 0, 0), (0, 0, 1, 0), (1, 0, 0, 0), (0, 0, 0, 0))
print(eh_territorio(territory))  # Output: True
Finding Adjacent Intersections
python
Copy
from FP2324P1 import obtem_intersecoes_adjacentes

territory = ((0, 1, 0, 0), (0, 0, 0, 0), (0, 0, 1, 0), (1, 0, 0, 0), (0, 0, 0, 0))
intersection = ('C', 3)
print(obtem_intersecoes_adjacentes(territory, intersection))  # Output: (('C', 2), ('B', 3), ('D', 3), ('C', 4))
Visualizing a Territory
python
Copy
from FP2324P1 import territorio_para_str

territory = ((0, 1, 0, 0), (0, 0, 0, 0), (0, 0, 1, 0), (1, 0, 0, 0), (0, 0, 0, 0))
print(territorio_para_str(territory))
Calculating Mountain Chains
python
Copy
from FP2324P1 import calcula_numero_cadeias_montanhas

territory = ((1, 1, 1, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 0), (0, 0, 0, 0))
print(calcula_numero_cadeias_montanhas(territory))  # Output: 2
Installation
Clone the repository to your local machine:

bash
Copy
git clone https://github.com/your-username/territory-explorer.git
Navigate to the project directory:

bash
Copy
cd territory-explorer
You can now import the functions from FP2324P1.py into your Python scripts.

Acknowledgments
This project was developed as part of the Fundamentals of Programming course at Instituto Superior Técnico.
