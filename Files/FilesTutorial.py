file = open("file.txt", "r")

outfile = ""

for line in range(1, 10):
    if line % 2 == 0:
        outfile += file.readline()
    else:
        file.readline()

file = open("file.txt", "w")
file.write(outfile)
file.close()