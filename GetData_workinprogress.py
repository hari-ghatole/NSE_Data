import numpy as np
import talib as ta 
from nsepy import get_history as gh
import datetime as dt 


#import values from nsepy and print technical indicator values
symbol = 'BANKNIFTY'
start = dt.date(2020,10,1)
end = dt.date(2021,1,29)

#get data
data = gh(symbol, start, end, index=True)

bnf_open = list((data["Open"]))
bnf_high = list((data["High"]))
bnf_low = list((data["Low"]))
bnf_close = list((data["Close"]))

#print("Open:", bnf_open,"\n")
#print("High:", bnf_high,"\n")
#print("Low:", bnf_low,"\n")
#print("Close:", bnf_close,"\n")

open_arr = np.array(bnf_open)
high_arr = np.array(bnf_high)
low_arr = np.array(bnf_low)
close_arr = np.array(bnf_close)

#print(len(close_arr))

####### CALCULATION ####### : relative_calc = np.ndarray.tolist(ta.RSI(close_arr[ix], timeperiod=4))

'''
ix = 20
for ix in close_arr:
    relative_calc = np.ndarray.tolist(ta.RSI(bnf_close[ix], timeperiod=4))
    print(close_arr[ix])
    ix = ix + 1
'''


for x in range (15,len(close_arr)):
    #print(close_arr[x])
    relative_calc = np.ndarray.tolist(ta.RSI(bnf_close[x], timeperiod=4))