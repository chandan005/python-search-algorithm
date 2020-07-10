import json

def program(n_dimensions,moves,zombie_start_position,creatures_position):
    zombies_final_positions = list()
    zombies_positions = set()
    zombies_positions.add(zombie_start_position)
    zombies_score = 0
    creature_not_found = False
    
    while not creature_not_found:
        zombies_discovered_positions = set()
        for zombie_position in zombies_positions:
            list_of_moves = get_adjacent_moves(n_dimensions= n_dimensions, moves=moves, postion=zombie_position)
            zombies_final_positions.append(list_of_moves[-1])

            list_of_moves = set(list_of_moves)
            new_zombie_position = list_of_moves.intersection(creatures_position)
            if not new_zombie_position:
                creature_not_found = True
                print("Breaking because no creature found in path")
                break
            else:
                for new_z in new_zombie_position:
                    zombies_score += 1
                    creatures_position.remove(new_z)
                    zombies_discovered_positions.add(new_z)
        zombies_positions = zombies_discovered_positions

    print("Zombies Score: ", zombies_score)
    print("Zombies Positions: ")
    print(*zombies_final_positions, sep=' ')

def get_adjacent_moves(n_dimensions,moves,postion):
    x = postion[0]
    y = postion[1]
    list_of_moves = list()
    for move in moves:
        if move == "D":
            y = y + 1
        if move == "L":
            x  =  x - 1
        if move == "U":
            y = y - 1
        if move == "R":
            x = x + 1
        if y < 0:
            y = n_dimensions - 1
        if x < 0:
            x = n_dimensions - 1
        if y >= n_dimensions:
            y = 0
        if x >= n_dimensions:
            x = 0
        list_of_moves.append((x,y))
    return list_of_moves

if __name__ == '__main__':
    with open("input.json") as file:
        data = json.load(file)
        n_dimensions = data["number_of_dimensions"]
        moves = data["moves"]
        zombie_start_position = eval(data["zombie_start_position"])
        creatures_position = set(list(map(eval, data["creatures_position"])))
        program(n_dimensions=n_dimensions,moves=moves, zombie_start_position=zombie_start_position, creatures_position=creatures_position)