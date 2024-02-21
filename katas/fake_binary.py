def fake_bin(x):
    bin = ''
    
    for num in x:
        if int(num) < 5:
            bin += '0' 
        else:
            bin += '1'
    return bin