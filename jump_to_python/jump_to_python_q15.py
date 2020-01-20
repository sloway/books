input_string = input()

count = []
for i in range(0, 10):
    count.append(False)

for i in input_string:
    count[int(i)] = True

if count.count(False) >= 1:
    print("false")
else:
    print("true")