import re
import json


def sumNumbersByRedRule(data):
    if type(data) == int:
        return data

    if type(data) == list:
        return sum([sumNumbersByRedRule(x) for x in data])

    if type(data) == dict:
        if "red" in data.values():
            return 0
        else:
            return sumNumbersByRedRule(list(data.values()))

    return 0


with open('data.txt') as f:
    data = f.read()

matches = re.findall(r'-?\d+', data)

dataCopy = json.loads(data)


print(f"Part 1: {sum(map(int, matches))} | Part 2: {sumNumbersByRedRule(dataCopy)}")
