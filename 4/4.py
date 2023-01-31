from hashlib import md5


def findNumber(zeros):
    n = 0

    while True:
        digestedHash = md5(f'ckczppom{n}'.encode()).hexdigest()  
        
        if digestedHash.startswith(zeros):
            return n
        
        n += 1


print(f'Part 1: {findNumber("00000")} | Part 2: {findNumber("000000")}')
