s = input()

from collections import deque
q = deque(list(s))

x = ""

decide = []
kari = []

while q:
    c = q.popleft()
    if c == "A":
        if x == "":
            x = "A"
        elif x == "A":
            kari.append("A")
        elif x == ""