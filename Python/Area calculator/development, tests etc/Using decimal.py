from decimal import *

# Decimal(10) will give the number 10, but it is a decimal, which is different.
test = Decimal(10)
print(test, "\n") # the \n is just to jump a line

a = getcontext()
print(a, "\n")

# decimal vs float:
b = Decimal(2.44) * Decimal(2.399)  #decimal operations are more precise
print(b, "\n")

c = 2.44 * 2.399
print(c, "\n")


# A use for decimals:
# float:
d = 1.4 - 1.3
print(d, "\n")

# decimal:
d2 = Decimal("1.4") - Decimal("1.3") # if the numbers aren't inside quotes, the value will use all the precision specified.
# d2 = getcontext().prec = 28  #here I'm saying that the precision of the oparation is 28
print(d2, "\n")

# float gives: 0.09999999999999987
# decimal gives: 0.1 (but only if the numbers are inside quotes for some reason)
