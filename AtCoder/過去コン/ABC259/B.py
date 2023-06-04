a,b,d = map(int, input().split())
import math

x = math.radians(-d)

print(a*math.cos(x)+b*math.sin(x),-a*math.sin(x)+b*math.cos(x))