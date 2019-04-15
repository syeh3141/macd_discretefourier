# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 13:20:17 2018

@author: syeh3
Methods for Fourier signal analysis of MACD and Signal Line Differences
"""
import macd
import numpy as np
from scipy.fftpack import fft
import copy
import matplotlib.pyplot as plt
from collections import Counter

def macdFourier(stockData):
    """Takes in stockData in pandas.dataFrame type and returns index "cycle"
    of maximum frequency bin after performed Discrete Fourier Transform"""
    
    macd.macd(stockData)
    
    macdsignal = []
    
    for signalDifference in stockData['MACD Signal Difference']:
        
        macdsignal.append(signalDifference)
        
    fourierd = fft(np.array(macdsignal))
    
    norm = np.absolute(fourierd)
    
    return norm.argmax()


def macdFourierHalf(stockData):
    """DFT on Half of Sample Size
    Then increment each day to aggregate
    over the whole sample"""
    
    firstPoint = 0
    
    halfwayPoint = int(len(stockData)/2)
    
    allFrequencyBins = []
    
    while(firstPoint < int(len(stockData)/2)):
        
        partitionedStockData = copy.deepcopy(stockData[firstPoint:halfwayPoint])
        
        allFrequencyBins.append(macdFourier(partitionedStockData))
        
        firstPoint += 1
        
        halfwayPoint += 1
        
    frequencyBins = Counter(allFrequencyBins)
    
    return int(len(stockData)/2)/frequencyBins.most_common(1)[0][0]
        
    #return allFrequencyBins


def macdFourierTwoThird(stockData):
    """DFT on two third of Sample Size
    Then increment each day to aggregate
    over the whole sample"""
    
    
    firstPoint = 0
    
    twoThirdPoint = int(2*len(stockData)/3)
    
    allFrequencyBins = []
    
    while(firstPoint < int(len(stockData)/3)):
        
        partitionedStockData = copy.deepcopy(stockData[firstPoint:twoThirdPoint])
        
        allFrequencyBins.append(macdFourier(partitionedStockData))
        
        firstPoint += 1
        
        twoThirdPoint += 1
        
    frequencyBins = Counter(allFrequencyBins)
    
    return int(2*len(stockData)/3)/frequencyBins.most_common(1)[0][0]


def macdFourierOneThird(stockData):
    """DFT on one third of Sample Size
    Then increment each day to aggregate
    over the whole sample"""
    firstPoint = 0
    
    oneThirdPoint = int(len(stockData)/3)
    
    allFrequencyBins = []
    
    while(firstPoint < int(2*len(stockData)/3)):
        
        partitionedStockData = copy.deepcopy(stockData[firstPoint:oneThirdPoint])
        
        allFrequencyBins.append(macdFourier(partitionedStockData))
        
        firstPoint += 1
        
        oneThirdPoint += 1
        
    frequencyBins = Counter(allFrequencyBins)
    
    return int(len(stockData)/3)/frequencyBins.most_common(1)[0][0]


def showHistogramPlot(listOfFrequencyBins):
    """Shows histogram plot of frequency bins""""
    allFreqArray = np.array(listOfFrequencyBins)
    
    plt.hist(allFreqArray, bins = np.arange(allFreqArray.min(), allFreqArray.max() + 1))
    
    plt.show()
    
    
    
    
    
    
    
    
    
    
