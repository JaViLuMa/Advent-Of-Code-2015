from itertools import product


def animate(grid, stuck=False):
    for _ in range(100):
        newGrid = []

        for i, row in enumerate(grid):
            newGrid.append([])

            for j, col in enumerate(row):
                count = sum(grid[i + x][j + y] for x, y in product([-1, 0, 1], repeat=2) if (x or y) and 0 <= i + x < len(grid) and 0 <= j + y < len(row))

                newGrid[-1].append(count in [2, 3] if col else count == 3)

        grid = newGrid

        if stuck:
            grid[0][0] = grid[0][-1] = grid[-1][0] = grid[-1][-1] = True

    return grid


grid = []

with open('data.txt') as f:
    lines = f.read().splitlines()
    
    for line in lines:
        grid.append([x == '#' for x in line])

animation = sum(sum(x) for x in animate(grid))
stuckAnimation = sum(sum(x) for x in animate(grid, stuck=True))

print(f'Part 1: {animation} | Part 2: {stuckAnimation}')
