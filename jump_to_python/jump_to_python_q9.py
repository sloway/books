f = open("./sample.txt", 'r')
lines = f.readlines()
f.close()

total = 0
for v in lines:
    total += int(v)

avg = total/len(lines)

f = open("./result.txt", "w")
f.write(str(avg))
f.close()