def century(year):
    centuries = year // 100
    if year % 100 == 0:
        return centuries
    else:
        return centuries + 1

# double slash gives a integral result of your division, the % 100 guarantees the division left no decimals.
