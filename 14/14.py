import re

reindeers = {}

with open('data.txt') as f:
    for line in f:
        matches = re.match(r'(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.', line)

        if matches:
            reindeer, speed, flyTime, restTime = matches.groups()

            reindeers[reindeer] = {
                'speed': int(speed),
                'flyTime': int(flyTime),
                'restTime': int(restTime),
                'distance': 0,
                'points': 0
            }

for i in range(2503):
    for reindeer in reindeers:
        if i % (reindeers[reindeer]['flyTime'] + reindeers[reindeer]['restTime']) < reindeers[reindeer]['flyTime']:
            reindeers[reindeer]['distance'] += reindeers[reindeer]['speed']

    for reindeer in reindeers:
        if reindeers[reindeer]['distance'] == max([reindeers[r]['distance'] for r in reindeers]):
            reindeers[reindeer]['points'] += 1

maxDistance = max(reindeers[reindeer]['distance'] for reindeer in reindeers)
maxPoints = max(reindeers[reindeer]['points'] for reindeer in reindeers)

print(f'Part 1: {maxDistance} | Part 2: {maxPoints}')
