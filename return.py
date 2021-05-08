def func():
    a = list(range(1,11))
    b = []
    for d in a:
        b.append(d)
    return(b)

def func2():
    s = func()
    print(s)
func2()
