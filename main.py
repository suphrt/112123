for a in range(500, 0, -1):
    for x in range(500):
        for y in range(500):
            if not (((x<=11) <= (x*x<=a)) and ((y*y) < a) <= (y <= 12)):
                break
        if not (((x <= 11) <= (x * x <= a)) and ((y * y) < a) <= (y <= 12)):
            break
    else:
        print(a)
        break