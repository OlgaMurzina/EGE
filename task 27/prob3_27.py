def center(cl):
    xmax = -10 ** 20
    xmin = 10 ** 20
    ymax = -10 ** 20
    ymin = 10 ** 20
    for x1, y1 in cl:
        xmax = max(xmax, x1)
        xmin = min(xmin, x1)
        ymax= max(ymax, y1)
        ymin= min(ymin, y1)
        for x2, y2 in cl:
            a = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
            if a > l:
                l = a
    return max(abs(xmax - xmin), abs(ymax, ymin)), l