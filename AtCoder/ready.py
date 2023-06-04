s = input()

import os
os.makedirs(f"./{s}",exist_ok=True)

ls = ["a","b","c","d","e","f","g","h","test"]
for i in ls:
    f = open(f'./{s}/{i}.py', 'x')
    f.close()