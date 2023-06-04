x = int(input())

import math
from decimal import Decimal


print(math.floor(Decimal(str(x))/Decimal("10")))