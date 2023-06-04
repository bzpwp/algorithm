h1,h2,h3,w1,w2,w3 = map(int,input().split())
x = 0


for a in range(1,h1-1):
    for b in range(1,h1-a):
        c = h1-a-b
        if w1-a >=2:
            for d in range(1,w1-a):
                g = w1-a-d
                if h2-d>=2:
                    for e in range(1,h2-d):
                        f = h2-d-e
                        if w2-e-b>=1:
                            h = w2-e-b
                            i = h3-h-g
                            if i > 0 and i == w3-c-f:
                                x += 1

print(x)
