def number_candles(candles):
    candles.sort()
    p = candles[-1]
    highest = []
    for i in candles:
        if i == p:
            highest.append(i)
    print(len(highest))


number_candles([18, 90, 90, 13, 90, 75, 90, 8, 90, 43])
number_candles([82,49,82,82,41,82,15,63,38,25])
number_candles([44,53,31,27,77,60,66,77,26,36])
number_candles([1000,1000,1000,1000,1000,800,1000,1000,1000,
                1000,1000,1000,1000 ,900, 1000 ,1000 ,1000 ,1000 ,1000 ,
                1000 ,1000, 1000 ,1000 ,1000 ,1000 ,1000])

