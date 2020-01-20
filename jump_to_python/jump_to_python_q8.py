f = open('./abc.txt', 'r')
lines = f.readlines()
f.close()

lines.reverse()

f = open('./abc_output.txt', 'w')
for line in lines:
    line = line.strip()
    f.write(line)
    f.write('\n')
f.close()





