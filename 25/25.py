code = 20151125

row = 1
col = 1

while row != 2981 or col != 3075:
    if row == 1:
        row = col + 1
        col = 1
    else:
        row -= 1
        col += 1

    code = (code * 252533) % 33554393

print(f'Code: {code} | Merry Christmas :D')
