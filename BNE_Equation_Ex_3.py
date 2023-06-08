import sympy as sy
import numpy as np

sy.init_printing()
b_i, C_i, a, H_1, H_2 = sy.symbols('b_i C_i a H_1 H_2')   #Define Symbols
solution = sy.solve(1/(b_i-C_i) - 1/(a*H_1 - b_i) - 1/(a*H_2 - b_i), b_i,         
         force=True, manual=True, set=True)

print("solution: ", solution)