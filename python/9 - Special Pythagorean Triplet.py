for a in range(332,0,-1):
    for b in range(500,a,-1):
        if a**2 + b**2 == (1000-a-b)**2:
            c = 1000-a-b
            product = a*b*c
            print("""
a: {}
b: {}
c: {}
abc: {}""".format(str(a),str(b),str(c),str(product)))

