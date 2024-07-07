from typing  import Dict

a : Dict[str, int] = {
    "harry" : 3,
    "fareed": 5,
    "rahul" : 7
                }
b : Dict[str, int] = {
    "harry" : 78,
    "resham": 5,
    "rahul" : 3
                }

merged = b | a
print (merged)