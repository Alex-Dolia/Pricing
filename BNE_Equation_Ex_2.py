import sympy as sy
sy.init_printing()
import numpy as np

b_i, C_i, a, H, L = sy.symbols('b_i C_i a H L')   #Define Symbols

solution = sy.solve((-2*b_i + a * H + C_i) / (a * (H-L)), b_i ,
         force=True, manual=True, set=True)
print("solution: ", solution)