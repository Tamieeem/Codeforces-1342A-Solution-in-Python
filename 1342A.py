for i in range(int(input())):
    x, y = map(int, input().split())
    a, b = map(int, input().split())
    if x == 0 and y == 0:
        print(0)
    else:
        path1 = a*(abs(x-y)) + (b*min(x,y))

        path2 = ((a*x)+(a*y))
        print(min(path1, path2))


