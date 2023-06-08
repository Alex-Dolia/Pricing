import pandas as pd
from numpy.random import uniform
import numpy as np
#
np.random.seed(11)
Ci = 5   # cost of seller i
L  = 4
H  = 10  
# H is the upper bound for the cost of seller j
a  = 1.5
n  = 1000000 # n is the number of tenders
aCj = uniform(L, H, n)
#
abj = a * aCj
abi = range(int(max(abj))+1)
#
results = []
for bi in abi:
    P_win = len(abj[abj > bi]) / len(abj)
    EU    = (bi-Ci) * P_win
    elem = {}
    elem["optimal bi"       ] = np.round((Ci+a*H)/2,2)
    elem["considered bi"    ] = bi
    elem["estimated P_win"  ] = np.round(P_win, 2)
    if   (bi <= a*L): 
         elem["theoretical P_win"] = 1
         elem["maximum EU"       ] = np.round(a*L - Ci, 2)  
    elif (bi > a*L) and (bi <= a*H):
          elem["theoretical P_win"] = np.round((a*H-bi)/(a*(H-L)), 2)
          elem["maximum EU"       ] = np.round((a*H-Ci)**2 /(4*a*(H - L)), 2) 
    elem["estimated EU"     ] = np.round(EU, 2)
    results.append(elem)    
#
results_df = pd.DataFrame(results)
results_df[['optimal bi', 'considered bi', 'estimated P_win', 'theoretical P_win',
            'estimated EU', 'maximum EU']]