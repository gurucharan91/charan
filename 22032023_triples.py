triples = []
for x in range(1,4):
    print(f"the value of x is {x}")
    for y in range(2,5):
        print(f"the value of y is {y}")
        for z in range(5,8):
            print(f"the value of z is {z}")
            if x+y > z:
                print(f"sum of x+y is {x+y}")
                triples.append((x,y,z))
print(triples)
