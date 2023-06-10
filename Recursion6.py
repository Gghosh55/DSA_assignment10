def towerOfHanoi(n, source, destination, auxiliary):
    if n == 1:
        print(f"Move disc 1 from {source} to {destination}")
        return 1

    moves = 0

    moves += towerOfHanoi(n - 1, source, auxiliary, destination)

    print(f"Move disc {n} from {source} to {destination}")
    moves += 1

    moves += towerOfHanoi(n - 1, auxiliary, destination, source)

    return moves


n = 2  # Number of discs
total_moves = towerOfHanoi(n, "Rod 1", "Rod 3", "Rod 2")
print(f"Total moves: {total_moves}")
