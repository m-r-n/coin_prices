# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 21:32:50 2023
Updated version 2023 10.10: storing into nX60min files, automatically naming the files

@author: mrnpa
"""
# recording the price in 10-min or 60-min files, adding time stamps to file names.
# ToDo: to index the files and to record the time stamps into a seperate file.


# Import numpy library
import numpy as np
import matplotlib.pyplot as plt
import datetime
import time

# print(currentTime)

directoryPath = "Eth"
newFileCounter = str(101)

# initializing our vectors
num_frames_to_record = 3
num_samples_to_record = 60      # an hour is 60 x 2 samples = 120s/h 
num_secs_to_wait = 55           # if delay=25secs, then saving 2 samples per minute
num_samples_recorded = 0        # if delay=55secs, then saving 1 sample per minute

# initializing our vectors
array_eth = np.zeros((num_samples_to_record,1))
array_btc = np.zeros((num_samples_to_record,1))
array_bnb = np.zeros((num_samples_to_record,1))
array_bch = np.zeros((num_samples_to_record,1))

# this is the coinmarketcap init part
import requests

values = range (num_samples_to_record)
frame__indices = range (num_frames_to_record)

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
parameterA = {'symbol': 'ETH'}
parameterB = {'symbol': 'BTC'}
parameterC = {'symbol': 'BNB'}
parameterD = {'symbol': 'BCH'}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'here-comes-your-coinmarketcap-string                          '
}
# end of the coinmarketcap init part

# get the very first starting time
currentTime = datetime.datetime.now()

# ======== OUTER loop of a 10min frame =======
for ii in frame__indices :

    time_from = str (currentTime) [11:19]
    
    print("\n" + "Processing frame nr.: " + str(ii) + "/" + str(num_frames_to_record))
    #    this was redundant, if getting it in the higher loop.
    #    currentTime = datetime.datetime.now()
    print ("-- Datum--  -- Time --  -- SampleNr. --  -- Prices --")
    # ======== INNER loop of a 10min frame =======
    for i in values :
        response1 = requests.get(url, headers=headers, params=parameterA).json()
        response2 = requests.get(url, headers=headers, params=parameterB).json()
        response3 = requests.get(url, headers=headers, params=parameterC).json()
        response4 = requests.get(url, headers=headers, params=parameterD).json()
        
        eth_price = response1['data']['ETH']['quote']['USD']['price']
        btc_price = response2['data']['BTC']['quote']['USD']['price']
        bnb_price = response3['data']['BNB']['quote']['USD']['price']
        bch_price = response4['data']['BCH']['quote']['USD']['price']
        #print("The current price of Ethereum is: $" + str(eth_price))
        
        currentTime = datetime.datetime.now()
        # print ("pontos idö es daatum:")
        #print(currentTime, " Ethereum is: $" + str(eth_price))
        print(currentTime, "Ind:" + str(i),"/", str(num_samples_to_record), " ETH: $" + str(round(eth_price,2)), "BTC: $" + str(round(btc_price,2)), "BNB: $" + str(round(bnb_price,2)), "BCH: $" + str(round(bch_price,2)))
        
        array_eth[i, 0] = round(eth_price,2)
        array_btc[i, 0] = round(btc_price,2)
        array_bnb[i, 0] = round(bnb_price,2)
        array_bch[i, 0] = round(bch_price,2)
        
        num_samples_recorded = i
        
        #print(i)
        time.sleep(num_secs_to_wait)
        
    # ------------- end of recording loop -------------
    time_till = str (currentTime) [11:19]   
      
    # =============== SAVING ====================
    date_string = "_" + str (currentTime)[0:10] 
    time_string = "_" + str (currentTime)[11:13] + "." + str(currentTime)[14:16] + "." + str(currentTime)[17:19] 
    newFile = open (directoryPath + date_string + time_string + ".txt", "w") 
    for i in values :  
        # f.write('%d' % number)
        newFile.write('%d' % array_eth[i,0] + " ")
        newFile.write('%d' % array_btc[i,0] + " ")
        newFile.write('%d' % array_bnb[i,0] + " ")
        newFile.write('%d' % array_bch[i,0] + "\n")
        #newFile.write(str(array_eth[i,0])) 
        
    newFile.close()
    
    # =============== PLOTTING ====================
    # no plotting in order not to inject delay in-between the 60-min frames.
    
    
        
