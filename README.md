# Zombie Apocalypse Program

This project is built using Python 3.7.7. It takes a json file as an input with these variables:
1. number_of_dimensions
2. moves
3. zombie_start_position
4. creatures_position

The program has two functions, one to get list of moves made by zombie and another to perform rest of the logic. 
The program() function has following algorithm: It get all input variables from arguments and stores them locally in the function. Also keeps track of when to finish code execution.

1. Loop (until all creatures found) or (until no creature found in zombie's path)
2. For each zombie position found or given via input file:
    1. Get list of moves made by zombie
    2. Store the final position of zombie
    3. Check if zombie found any creatures in the path
        1. If found mark the creature as found, store the path as new zombie and increase zombie score by 1
        2. If not found finish code execution


## Installation / Usage

1. Make desired changes in input.json file
2. Run below docker commands

Docker

```bash
docker build -t python-zombie . 
docker run python-zombie
```








