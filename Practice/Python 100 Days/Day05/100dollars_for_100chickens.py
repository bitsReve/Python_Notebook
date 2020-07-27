for cocks in range(0, 101):
    for hens in range(0, 101):
        chicks = 100 - hens - cocks
        if cocks*5 + hens*3 + chicks/3 == 100:
            print('cocks = %d, hens = %d, chicks = %d' % (cocks, hens, chicks))
