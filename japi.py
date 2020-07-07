# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 19:16:50 2020

@author: Kristyn
"""
import json

import urllib.request

Sym=[]
while True:
    y= input("Enter the company symbols you want to see the price of type quit to quit: ")
    Sym.append(y)
    if y == "quit":
        break
print(Sym)




#Where < URL> is the URL you want to connect to.

#nasdaqAppleURL = 'https://www.nasdaq.com/symbol/aapl'
#connection = urllib.request.urlopen(nasdaqAppleURL)
#responseString = connection.read().decode()

    
def getStockData(a):
    URL='https://www.alphavantage.co/query?function=BATCH_STOCK_QUOTES&symbols='+a+'&apikey=JD76E9W4O8RF93EG' 
    connection = urllib.request.urlopen(URL)
    responseString = connection.read().decode()

    print(responseString)
    y = json.loads(responseString)
    print("the price of "+y["1.symbol"]+" is: "+y["2.price"])


i=0
for i in range(len(Sym)-1):
    a=(Sym[i])
    getStockData(a)
    i +=1



#https://www.alphavantage.co/query?function=BATCH_STOCK_QOUTES&symbols=AAPL&apikey=JD76E9W4O8RF93EG
    
    
#Where < URL> is the URL you want to connect to.

#nasdaqAppleURL = 'https://www.nasdaq.com/symbol/aapl'
#connection = urllib.request.urlopen(nasdaqAppleURL)
#responseString = connection.read().decode()
      


