# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 17:20:41 2018

@author: syeh3
Script to run on stock data for DFTs
"""

import macdfourier as mf
import convertExceltoDataFrame
import copy

convertExceltoDataFrame.convertExcelToDataFrame('presentstockdata')

stocksDataListOutcome = copy.deepcopy(convertExceltoDataFrame.stocksDataList)

goodstockBins = {}

for stock in stocksDataListOutcome:
    
    print(stock)
    
    stockData = stocksDataListOutcome[stock]
    
    oneThird = int(len(stockData)/3)
    
    oneHalf = int(len(stockData)/2)
    
    twoThird = int(2*len(stockData)/3)
    
    listBins = ([oneThird/mf.macdFourierOneThird(stockData), oneHalf/mf.macdFourierHalf(stockData), twoThird/mf.macdFourierTwoThird(stockData)])
    
    sortedListBins = sorted(listBins)
    
    print(sortedListBins)
    
    low = sortedListBins[0]
    
    mid = sortedListBins[1]
    
    high = sortedListBins[2]
    
    if (low >= (int)(0.85*mid) and high <= ((int)(1.15*mid) + 1)) or low == mid or mid == high:
        
        goodstockBins[stock] = listBins
    
print(goodstockBins)
    
    
    
    
