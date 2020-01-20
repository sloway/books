input_string = input()
print(input_string)

result = []
for i, v in enumerate(input_string):
    result.append(v)
    if i == len(input_string) - 1:
        break

    v0 = int(v)
    v1 = int(input_string[i + 1])

    if v0 % 2 == 1 and v1 % 2 == 1:
        result.append("-")
    elif v0 % 2 == 0 and v1 % 2 == 0:
        result.append("*")
    else:
        pass

print("".join(result))


