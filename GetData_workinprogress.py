import numpy as np
import talib 
from nsepy import get_history as gh
import datetime as dt 


#import values from nsepy and print technical indicator values
symbol = 'BANKNIFTY'
start = dt.date(2018,1,1)
end = dt.date(2020,12,31)


#get data
data = gh(symbol, start, end, index=True)

bnf_open = list((data["Open"]))
bnf_high = list((data["High"]))
bnf_low = list((data["Low"]))
bnf_close = list((data["Close"]))
bnf_vol = list((data["Volume"]))

'''
for i in range(len(bnf_close)):
    ohlclist = list((bnf_open[i],bnf_high[i],bnf_low[i],bnf_close[i]))
    print((ohlclist))
'''

open_arr = np.array(bnf_open)
high_arr = np.array(bnf_high)
low_arr = np.array(bnf_low)
close_arr = np.array(bnf_close)

############### CALCULATION ############### 

relative_calc = np.ndarray.tolist(talib.RSI(close_arr, timeperiod=11))

for i in range(len(bnf_close)):
    print(close_arr[i])
    if relative_calc[i] >= 80:
        print(relative_calc[i],":Overbought\n")
    elif relative_calc[i] <= 20:
        print(relative_calc[i],":Oversold\n")
    elif relative_calc[i] > 20 and relative_calc[i]<80:
        print(relative_calc[i],"===\n")
    i = i +1
print("Value of i is:",i)
print("LENGHT:",len(close_arr))

#atr_calc = np.ndarray.tolist(ta.ATR(high_arr,low_arr,close_arr,timeperiod=14))
