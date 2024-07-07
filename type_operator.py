# it is basically used ti define the statements... like integerand all for user friendly..

# eg
a : int = 5 
# print(a.bit_length())\
# print(a.numerator)
# print(a.denominator)
# print(a.real)
b : str = "fareed"
# print(b.capitalize())

# in functions 
def sum(a : int, b : int) -> int :
    return a +b

# print(sum(3,4))

# more functions lets import 

from typing import List,Union,Tuple

number : List[int] = [1,2,4,5]
number.append(4)
print(number)