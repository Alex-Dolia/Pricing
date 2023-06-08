import pandas as pd
from numpy.random import uniform
import numpy as np
#
np.random.seed(11)
Ci = 5   # cost of seller i
H  = 10  # H is the upper bounf for the cost of seller j
a  = 1.5
n  = 1000000 # n is the number of tenders
aCj = uniform(0, H, n)
#
abj = a  aCj
abi = range(int(max(abj))+1)
#
results = []
for bi in abi
    P_win = len(abj[abj  bi])  len(abj) # estimated probability of win
    EU    = (bi-Ci)  P_win
    elem = {}
    elem[optimal bi       ] = np.round((Ci+aH)2,2)
    elem[considered bi    ] = bi
    elem[estimated P_win  ] = np.round(P_win, 2)
    elem[theoretical P_win] = np.round(1-bi(aH), 2)
    elem[estimated EU     ] = np.round(EU, 2)
    elem[maximum EU       ] = np.round((aH-Ci)2 (4aH), 2) 
    results.append(elem) 
    #
results_df = pd.DataFrame(results)
results_df