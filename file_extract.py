def file_extract(filename):
    file = open(filename)
    count = 0
    maxcap = 0.0
    for line in file.readlines():
        if (line[0] == 'u' or line[0] == 'v') and 'user' not in line:
            count += 1
            line = float(line.split()[1])
            if line >= maxcap:
                maxcap = line
    
    print(count)
    print(maxcap)
    
file_extract("777.txt")