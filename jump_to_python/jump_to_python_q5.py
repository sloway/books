def show_pivonach(max_value):
    v1 = 0
    v2 = 1
    print(v1)
    print(v2)
    while True:
        n = v1 + v2
        if n >= max_value:
            break
        print(n)
        v1 = v2
        v2 = n


show_pivonach(20)
