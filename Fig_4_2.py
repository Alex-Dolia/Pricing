import numpy  as np
import pandas as pd
def recommended_price_fun(random_max_values, low_price, high_price, 
                          step = 0.01, order_best_utility = 0):
    output = []
    max_utility = 0
    interval = np.arange(low_price, high_price, step)
    if len(interval) == 0:
       interval = [low_price]
    #
    for price in interval:
        prob = 1
        for i in random_max_values:   
            if len(random_max_values[i]) > 0:
               num = len(random_max_values[i][random_max_values[i] > price])
               P_j = float(num) / len(random_max_values[i]) 
               prob = prob * P_j
        utility = price * prob    
        elem = {"price": price, "probability": prob, "utility": utility}
        output.append(elem)
        #
    output_df = pd.DataFrame(output)
    output_df.sort_values(by = "utility", ascending = False, inplace = True)
    output_df = output_df.head(order_best_utility + 1)
    output_df = output_df.tail(1)
    #
    recommended_price = output_df["price"].values[0]
    recommended_prob  = output_df["probability"].values[0]
    max_utility       = output_df["utility"].values[0]
    #
    return output, recommended_price, recommended_prob, max_utility
#
random_max_values = {}
random_max_values["Medical Valley Invest"] = np.array([6.24, 7.71, 7.71, 7.71, 4.26,  7.7,  7.7,  7.7, 6.43,  7.4])
random_max_values["KRKA Sverige"         ] = np.array([7.56, 5.57, 7.56, 7.56, 7.56,  6.8, 4.71, 3.76, 7.56, 4.54])
random_max_values["Pfizer"               ] = np.array([7.57] * 10)
random_max_values["Mylan"                ] = np.array([7.52] * 10)
random_max_values["Ebb Medical"          ] = np.array([7.56, 7.04, 6.63, 4.64, 7.52, 7.52, 4.61, 7.56, 5.91, 7.56])
random_max_values["Accord Helthcare"     ] = np.array([5.16, 5.16, 5.16, 5.91, 7.56, 5.33, 7.52, 7.52, 7.52, 7.52])
#
step = 0.01
order_best_utility = 0
#
low_price  = None
high_price = None
#
for company in random_max_values:
    if (low_price is None ) or (low_price > np.min(random_max_values[company])):
        low_price = np.min(random_max_values[company])
    if (high_price is None ) or (high_price < np.max(random_max_values[company])):
        high_price = np.max(random_max_values[company])
#        
low_price =  low_price - 0.01        
#
output, price, prob, utility = recommended_price_fun(random_max_values,
                               low_price, high_price, step, order_best_utility)
print("Recommended price: ", price)
print("Probability of recommended price: ", prob)
print("Utility of recommended price: ", utility)
output_df = pd.DataFrame(output)
display(output_df)