# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 18:19:45 2023

@author: mrn
"""

# =========== NORMALIZING COINS ==============

ini_eth = array_eth[0,0]
ini_btc = array_btc[0,0]
ini_bnb = array_bnb[0,0]
ini_bch = array_bch[0,0]

coef_eth = ini_eth / 102
coef_btc = ini_btc / 101
coef_bnb = ini_bnb / 100
coef_bch = ini_bch / 99

# Plotting both the curves simultaneously
plt.plot(values, array_eth/coef_eth, color='r', label='ETH')
plt.plot(values, array_btc/coef_btc, color='g', label='BTC')
plt.plot(values, array_bnb/coef_bnb, color='b', label='BNB')
plt.plot(values, array_bch/coef_bch, color='c', label='BCH')

# =========== PLOTTING ==============

# Naming the x-axis, y-axis and the whole graph
# plt.xlabel('time: from', time_from, 'till ', time_till)
#plt.ylabel('price (USD)')
plt.ylabel('price deviation (%)')

#plt.title(currentTime)
plt.title((" " + time_from + "   --- ETH BTC BNB BCH ---    " + time_till))

#plt.title('some real-time prices')
plt.grid(True)

# saving the plot, important: when SAVE is put after the LEGEND command, the saved image is empty.
#plt.savefig("test.png")
time_string = "_" + str (currentTime)[11:13] + "_" + str(currentTime)[14:16] + "_" + str(currentTime)[17:19] 
plt.savefig(directoryPath + time_string + ".png")
  
# Adding legend, which helps us recognize the curve according to it's color
plt.legend()
# To load the display window
plt.show()