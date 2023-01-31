with open('data.txt') as f:
    totalWrappingPaperSquareFeet = 0
    totalRibbonFeet = 0

    for present in f.readlines():
        l, w, h = map(int, present.split('x'))
        
        surfaceArea = (2 * l * w) + (2 * w * h) + (2 * h * l)
        
        totalWrappingPaperSquareFeet += surfaceArea + min(l * w, w * h, h * l)

        volume = l * w * h

        totalRibbonFeet += volume + (2 * min(l + w, w + h, h + l))

    print(f'Part 1: {totalWrappingPaperSquareFeet} | Part 2: {totalRibbonFeet}')
