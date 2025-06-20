import numpy as np

x = np.arange(6)
condlist = [x < 3, x > 3]
choicelist = [-x, x ** 2]
result = np.select(condlist, choicelist, default=42)
print(result)  # Output: [ 0 -1 -2 42 16 25]