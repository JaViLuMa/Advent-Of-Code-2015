import re
import numpy as np

grid = np.array([{ 'state': 0, 'brightness': 0 } for _ in range(1000 * 1000)])
grid = grid.reshape((1000, 1000))

with open('data.txt') as f:
    instructions = f.read().splitlines()

pattern = re.compile(r"(turn on|turn off|toggle) (\d+),(\d+) through (\d+),(\d+)")

litLights = 0
totalLightBrightness = 0

for instruction in instructions:
    match = pattern.match(instruction)

    if match:
        action, x1, y1, x2, y2 = match.groups()

        for row in range(int(y1), int(y2) + 1):
            for col in range(int(x1), int(x2) + 1):
                if action == 'turn on':
                    grid[row][col]['state'] = 1
                    grid[row][col]['brightness'] += 1
                elif action == 'turn off':
                    grid[row][col]['state'] = 0

                    if not grid[row][col]['brightness'] <= 0:
                        grid[row][col]['brightness'] -= 1

                elif action == 'toggle':
                    grid[row][col]['state'] = 0 if grid[row][col]['state'] == 1 else 1
                    grid[row][col]['brightness'] += 2

for row in grid:
    for col in row:
        if col['state'] == 1:
            litLights += 1

        totalLightBrightness += col['brightness']

print(f'Part 1: {litLights} | Part 2: {totalLightBrightness}')
