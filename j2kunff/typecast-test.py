from j2kunff.modp import *
from j2kunff.polynomial import *


mod3 = IntegersModP(3)
Polynomial = polynomialsOver(mod3)
x = mod3(1)
p = Polynomial([1,2])

x+p
p+x

