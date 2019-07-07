# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 16:57:11 2019

@author: mohamed.h.osman
"""

import pandas as pd
#This code filters out the non-food products from the Instacart products 
#dataset and store the filtered data to a new csv file.  

productDF = pd.read_csv('..\\Instacart\\products.csv')
nonFoodAisleId = [6, 11, 20, 22, 40, 41, 44, 47, 54, 55, 56, 60, 73, 74,
                  75, 80, 82, 85, 87, 97, 101, 102, 109, 114, 118, 126, 
                  127, 132, 133]
nonFoodDeptId = [2, 11, 17]
foodProductDF = productDF[~productDF.aisle_id.isin(nonFoodAisleId) & 
                          ~productDF.department_id.isin(nonFoodDeptId)]

foodProductDF.to_csv('..\\wrangledData\\filteredFoodProducts.csv', 
                     encoding="utf-8", index=False)



