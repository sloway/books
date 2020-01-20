input_string = input()

prev = ""
count = 0

result = ""
for v in input_string:
    if v == prev:
        count += 1
    else:
        if count:
            result += str(count)
        result += v
        count = 1
        prev = v

if count:
    result += str(count)

print(result)
