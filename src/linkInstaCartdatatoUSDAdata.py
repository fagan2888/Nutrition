import unicodecsv as csv
import requests
import json
#import time

#This code links the filtered instaCart products data set with the USDA 
#nutrition data by the Unique ID of the food using the usda food search api

#Need API key. It is available locally per request
api_key = ''
url = 'https://api.nal.usda.gov/fdc/v1/search?api_key={}'.format(api_key)
headers =  {'Content-Type': 'application/json'}
requestNum = 0
badReqProds = []
noDataRespProds= []
with open('..\\wrangledData\\filteredFoodProducts.csv', 'rb') as productFile:
    with open('..\\wrangledData\\linkedFoodProducts.csv', 'wb') as productFileOutput:
        with open('..\\wrangledData\\badReqFoodProducts.csv', 'wb') as badReqProds:
            with open('..\\wrangledData\\noDataRespFoodProducts.csv', 'wb') as noDataRespProds:
                
                product_reader = csv.reader(productFile, delimiter=',')
                product_writer = csv.writer(productFileOutput, delimiter=',', quotechar='"')
                badReq_writer = csv.writer(badReqProds, delimiter=',', quotechar='"')
                noDataResp_writer = csv.writer(noDataRespProds, delimiter=',', quotechar='"')
                
                for row in product_reader:
                    #FoodData Central currently limits the number of API requests to a
                    #default rate of 3,600 requests per hour per IP address. 
                    #Exceeding this limit will cause the API key to be temporarily
                    #blocked for 1 hour.
                    #Sample 300 
                    if requestNum > 300:
                        break
                    if row[0] == 'product_id':                
                        product_writer.writerow(['product_id','product_name','fdcId'])
                    else:
                        productid = row[0]
                        productName = row[1]
                        data = json.dumps({"generalSearchInput":productName}) 
                        #time.sleep(1)
                        resp = requests.post(url = url, headers = headers, data = data)
                        requestNum += 1
                        if resp.status_code != 200:
                            badReq_writer.writerow([productid,productName])
                            continue 
                        if resp.json()['foods']:
                            fdcId = resp.json()['foods'][0]['fdcId']
                            product_writer.writerow([productid,productName,fdcId])
                        else:
                            noDataResp_writer.writerow([productid,productName])
                            
                            
