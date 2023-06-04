a,b  = map(int, input().split())

from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN
f = b/a
print(Decimal(str(f)).quantize(Decimal('0.001'), rounding=ROUND_HALF_UP))
